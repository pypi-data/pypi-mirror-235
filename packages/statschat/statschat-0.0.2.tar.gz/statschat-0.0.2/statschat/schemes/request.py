import os
from typing import List

from pydantic import BaseModel, Field, validator


class MessageRecords(BaseModel):
    """
    历史消息参数
    """
    role: str
    content: str


class SendMsgIn(BaseModel):
    """
    发送文本消息入参
    """
    msg: str
    messages: List[MessageRecords] = Field(default=[])


class SendAnalysisTaskIn(BaseModel):
    """
    发送分析任务入参
    """
    msg: str
    messages: List[MessageRecords] = Field(default=[])


class UploadAnalysisFileIn(BaseModel):
    """
    发送分析任务入参
    """
    file_path: str
    messages: List[MessageRecords] = Field(default=[])

    @validator('file_path')
    def validate_file_exists(cls, value):
        if not os.path.exists(value):
            raise ValueError(f"文件 '{value}' 不存在")
        return value
