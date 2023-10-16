"""
chatgpt 驱动
"""
import json
import logging
import os
import subprocess

import openai

from ..core.response import unified_response
from ..drive.interface import LLM
from ..schemes.model import ModelDataIn
from ..schemes.request import SendMsgIn, SendAnalysisTaskIn, UploadAnalysisFileIn
from ..schemes.response import MessageBodyOut
from ..utils.excel import ExcelUtil
from ..utils.message import MessageUtil
from statschat.utils.tools import ToolsUtil

logger = logging.getLogger(__name__)


class ChatGPT(LLM):

    def __init__(self, model_data: ModelDataIn):
        # 初始化成员属性
        self.api_key = None
        self.temperature = 0
        self.auto_run = True  # Debug and continue
        self.model = 'gpt-3.5-turbo-16k-0613'  # Default
        self.context_window = 16000
        self.max_tokens = 5000
        self.max_debug_iter = 5
        self.allowed_extensions = {'csv', 'xls', 'xlsx'}
        self.dataset_count = 0
        self.msg_prompt = ""  # 对话描述
        self.upload_prompt = ""  # 上传文件描述 upload_prompt
        self.schema_prompt = ""  # 描述 schema_prompt
        self.analysis_prompt = ""  # 分析描述词
        self.debug_prompt = ""  # debug描述词
        self.feedback_prompt = ""  # feedback描述词
        self.input_dir = model_data.input_dir  # 输入目录
        self.output_dir = model_data.output_dir  # 输出目录

        for config_item in model_data.config:
            # 只有定义过的才执行赋值
            if hasattr(self, config_item.key):
                setattr(self, config_item.key, config_item.value)
        # 设置api_key
        openai.api_key = self.api_key
        super().__init__(model_data)

    @unified_response
    async def send_text_msg(self, params: SendMsgIn):
        """发送文本消息"""
        # 存储变量
        self.messages, msg = params.messages, params.msg
        # 添加prompt
        content = f"{self.msg_prompt}{msg}"
        # # 添加至 messages
        self.add_message(content, msg)
        return await self.request()

    @unified_response
    async def upload_analysis_file(self, params: UploadAnalysisFileIn):
        """上传分析文件"""
        # 分析文件获取 abstract
        self.messages, abstract = params.messages, ExcelUtil.get_abstract(params.file_path)
        # 添加prompt
        msg = f"{self.upload_prompt}{abstract}"
        # 添加至 messages
        self.add_message(msg, abstract, system=True)
        return await self.request()

    @unified_response
    async def send_analysis_task(self, params: SendAnalysisTaskIn):
        """发送分析任务 上传文件之后调用的方法"""
        # 存储变量
        self.messages, msg, input_dir, output_dir = params.messages, params.msg, self.input_dir, self.output_dir
        # 列出目录下的文件
        input_files = os.listdir(input_dir)
        input_files_str = ', '.join(input_files) if input_files else None
        output_files = os.listdir(output_dir)
        output_files_str = ', '.join(output_files) if output_files else None
        # 组装prompt
        prompt = f"{self.analysis_prompt}"
        if input_files_str:
            prompt += f" Available datasets are located in a folder titled '{input_dir}'. Filenames of datasets in the input folder are: {input_files_str}"
        if output_files_str:
            prompt += f" Filenames of datasets in the output folder are: {output_files_str}"
        prompt += "\nHere is the user's request:\n"
        # 替换schema_prompt 的模板变量
        schema_prompt = self.schema_prompt.format(output_dir=output_dir)
        content = schema_prompt + prompt + msg
        # 添加至 messages
        self.add_message(content, msg)
        return await self.request()

    async def request(self) -> MessageBodyOut:
        # 验证token是否超出 超出则去除最早的数据直至达到期望值
        MessageUtil.getCheckTokensMessages(self.messages, self.max_tokens)
        # 将 messages 转换为 List[dict]
        messages_as_dict = [{'role': record.role, 'content': record.content} for record in self.messages]
        chat_params = {
            "model": self.model,
            "messages": messages_as_dict,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens
        }
        # 发送请求
        completion = await self.send(openai.ChatCompletion.create, chat_params)
        # 取出 content
        response_message = completion.choices[0].message['content']
        # 判断是否为json字符串
        if ToolsUtil.is_json_string(response_message):
            json_response = json.loads(response_message)
        else:
            json_response = {"content": response_message, "code": ""}
            # code_block = MessageUtil.extractCode(response_message)
            # json_response = {"content": response_message, "code": "".join(code_block)}

        self.add_message(response_message, code=json_response.get('code'), role='assistant')
        # 不存在代码
        if not json_response.get("code"):
            return self.new_messages

        # 存在代码
        if json_response.get("code"):
            original_files = set(os.listdir(self.output_dir))
            output = await self.runCode(json_response.get("code"))
            current_files = set(os.listdir(self.output_dir))
            new_files = current_files - original_files
            if new_files:
                self.update_file_url(list(new_files))
            if output:
                await self.sendFeedback(output)
            else:
                await self.sendFeedback('Output has been generated.')
            return self.new_messages

        return self.new_messages

    # 运行返回的代码
    async def runCode(self, code):
        debug_iter = 0
        while debug_iter < self.max_debug_iter:
            result = subprocess.run(['python', '-c', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode != 0:
                err_message = result.stderr
                debug_response = await self.task_debug(err_message)
                code = debug_response.get('code', '')
                debug_iter += 1
            else:
                output = result.stdout
                break
        else:
            output = "It seems that the codes written by LLM reached maximum debug iterations. This issue has been reported to our team and we apologize for the inconvenience."
        return output

        # 代码执行之后的结果再次发送给gpt请求返回结果

    async def sendFeedback(self, output):
        # 存储变量
        msg = f"{self.feedback_prompt}{output}"
        # 添加prompt
        msg = f"{self.msg_prompt}{msg}"
        # 添加至 messages
        self.add_message(msg, output, system=True)
        return await self.request()

    async def task_debug(self, err_message):
        """
        Return error message back to LLM if bug after running.
        """
        msg = self.debug_prompt + err_message
        # 添加至 messages
        self.add_message(msg, err_message, system=True)
        # 发送请求
        return await self.request()
