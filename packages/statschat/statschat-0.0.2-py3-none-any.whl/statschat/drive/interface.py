import asyncio
from abc import ABCMeta, abstractmethod
from typing import List

from statschat.core.timeout import timeout
from statschat.schemes.model import ModelDataIn
from statschat.schemes.request import MessageRecords
from statschat.schemes.response import MessageBodyOut


class LLM(metaclass=ABCMeta):
    @abstractmethod  # 调用 @abstractmethod规定子类必须有__init__方法
    def __init__(self, config: ModelDataIn):
        # 存储messages
        self.messages, self.new_messages = [], []

    @abstractmethod  # 调用 @abstractmethod规定子类必须有send_text_msg方法
    async def send_text_msg(self, msg: str):
        pass

    @abstractmethod  # 调用 @abstractmethod规定子类必须有send_analysis_task方法
    async def send_analysis_task(self, file_path: str):
        pass

    @abstractmethod
    async def request(self) -> MessageBodyOut:
        pass

    @timeout(60)  # 调用timeout设置超时时间
    async def send(self, func, params):
        return await asyncio.to_thread(func, **params)

    # 添加消息
    def add_message(self, msg: str, original_msg: str = '', code: str = '', role: str = 'user', system: bool = False):
        original_msg = original_msg if original_msg else msg
        message = MessageRecords(**{"role": role, "content": msg})
        self.messages.append(message)
        new_message = MessageBodyOut(
            **{"role": role, "content": msg, "code": code, "system": system, "original_content": original_msg})
        self.new_messages.append(new_message)

    # 获取消息
    def get_messages(self):
        return self.messages

    # 清空消息
    def clear_messages(self):
        self.messages.clear()

    # 获取消息长度
    def get_messages_len(self):
        return len(self.messages)

    # 获取指定索引的消息
    def get_message(self, index):
        return self.messages[index]

    def update_file_url(self, new_files: List):
        self.new_messages[-1].file_url = new_files
