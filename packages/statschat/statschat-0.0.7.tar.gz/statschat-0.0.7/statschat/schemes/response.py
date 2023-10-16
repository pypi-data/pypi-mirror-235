from enum import Enum
from typing import Union, List, Set

from pydantic import BaseModel, Field


class MessageBodyOut(BaseModel):
    """
    返回消息参数
    """
    role: str = Field(default= 'user')  # 身份
    content: str = Field(default='')  # 返回的内容
    original_content: str = Field(default='')  # 原字符串
    code: str = Field(default='')  # 返回的代码
    system: bool = Field(default=False)  # 是否系统代替用户发送请求
    file_url: List = Field(default=[])  # 返回的文件地址


class ResponseOut(BaseModel):
    """
    返回数据
    """
    code: int
    msg: str
    error: str = Field(default='')
    data: List[MessageBodyOut] = Field(default=[])
