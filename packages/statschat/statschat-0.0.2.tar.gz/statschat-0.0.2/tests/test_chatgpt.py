import json

from statschat.stats_chat import StatsCHAT
import unittest


class TestCases(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        # 初始化模型
        self.model = StatsCHAT.get_model({
            "model": "ChatGPT",
            "config": [
                {
                    "key": "api_key",
                    "value": "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",
                },
                {
                    "key": "msg_prompt",  # 普通消息提示词
                    "value": "The user now asks you to perform an analysis task with no provided data. Write executable python codes in the 'code' field.",
                },
                {
                    "key": "upload_prompt",  # 上传文件提示词
                    "value": "Output a paragraph in Chinese that: (1) identify the likely subject or field of the dataset, (2) what analysis can be done using this dataset, (3) what visualization task that the user might be interested, (4) what models or methods can be applied to the data to draw insightful conclusions. \n Below is the abstract of the data:\n",
                },
                {
                    "key": "schema_prompt",  # 分析概要描述词
                    "value": "Please respond with JSON format containing the following two fields. {{\"code\":\"Python codes that needs to be run in a python subprocess to achieve the user's request (all environmental variables will be lost after execution). You must also include a line to print a message that will be sent back to you in a subsequent API call. If any modification or creation of datasets or figures happens, always save the output files in a folder called '{output_dir}', don't print the image like plt.show(). Use English for all texts in generated images.\",\n\"content\":\"If no codes need to be run to answer the user's request, write plain text in Chinese that replies to the USER in this field.\"}}\nFill in \"\" If no content to output for a field.\n"
                },
                {
                    "key": "analysis_prompt",  # 分析描述词
                    "value": "The user now asks you to perform an analysis task. Write executable python codes in the 'code' field."
                },
                {
                    "key": "debug_prompt",  # debug描述词
                    "value": "This is a debugging task. Please review the error message that appeared after running the code you provided in your last message. Rewrite the correct code in the 'code' field."
                },
                {
                    "key": "feedback_prompt",  # 反馈描述词
                    "value": "Here is the result of your previous code. Write a report to the user based on the result in natural Chinese."
                },
            ],
            "output_dir": './output/',
            "input_dir": './input/',
        })

    async def testSendMsg(self):
        """
        chatgpt 测试发送普通消息
        :return:
        """
        assert self.model, '模型获取失败'
        response = await self.model.send_text_msg({
            "msg": "讲个笑话",
            "messages": [
                {
                    "role": "user",
                    "content": "你好"
                },
                {
                    "role": "assistant",
                    "content": "你好！有什么我可以帮忙的吗？"
                }
            ]
        })
        print(response.code)
        print(response.msg)
        print(response.data)
        print(response.error)

    async def testCodeMsg(self):
        """测试返回代码"""
        response = await self.model.send_text_msg({
            "msg": "打印hello word"
        })
        print(response.code)
        print(response.msg)
        print(response.data)
        print(response.error)
        # python\nprint("Hello World")\n

    async def testUploadAnalysisFile(self):
        """测试上传文件开始分析"""
        response = await self.model.upload_analysis_file({
            "file_path": './input/dt.xlsx'
        })
        print(response.code)
        print(response.msg)
        print(response.error)
        print(response.data)

    async def testSendAnalysisTask(self):
        """测试分析任务"""
        response = await self.model.send_analysis_task({
            "msg": '画一个年龄的分布图',
            "messages": [
                {
                    "role": "user",
                    "content": '''Dataset1 contains 248 rows and 5 columns.
The column 'age' is a continuous variable, with a mean of 47.42, standard deviation of 13.59, maximum value of 75.00, and minimum value of 18.00
The column 'sex' contains categorical variables, with unique categories: Male, Female
The column '肾小管损伤程度' contains categorical variables, with unique categories: No, Yes
The column 'eGFR' is a continuous variable, with a mean of 34.71, standard deviation of 20.17, maximum value of 100.05, and minimum value of 3.71
The column '尿蛋白' contains categorical variables, with unique categories: 阴性, 阳性'''
                },
                {
                    "role": "assistant",
                    "content": "该数据集可能涉及肾脏疾病领域。可以使用该数据集进行以下分析：（1）根据年龄、性别、肾小管损伤程度和尿蛋白等变量，研究肾脏疾病的发病情况和相关因素。（2）可以通过统计分析，比较不同性别、年龄和肾小管损伤程度对eGFR和尿蛋白的影响。（3）用户可能对绘制关于年龄、eGFR和尿蛋白的分布图表感兴趣，以便更直观地了解数据的特征。（4）可以应用线性回归模型或者分类模型，以eGFR和尿蛋白为目标变量，探索与年龄、性别和肾小管损伤程度等因素之间的关系，并得出有洞察力的结论。"
                }
            ]
        })
        print(response.code)
        print(response.msg)
        print(response.error)
        print(response.data)
        data_as_dict = [{'role': record.role, 'content': record.content, "original_content": record.original_content, "code": record.code, "system": record.system, "file_url": record.file_url} for record in response.data]
        json_string = json.dumps(data_as_dict)
        print(json_string)


if __name__ == "__main__":
    unittest.main()
