import os
from enum import Enum
from typing import List
from pydantic import BaseModel, validator


class ModelEnum(str, Enum):
    """
    模型入参 Enum
    """
    ChatGPT = 'ChatGPT'  # chatgpt
    WenXinYiYan = 'WenXinYiYan'  # 文心一言
    TongYi = 'TongYi'  # 通义千问


class ConfigIn(BaseModel):
    """
        配置入参
        """
    key: str
    value: str


class ModelDataIn(BaseModel):
    """
    模型入参
    """
    model: ModelEnum
    config: List[ConfigIn]
    input_dir: str
    output_dir: str

    @validator('input_dir')
    def validate_input_dir_exists(cls, value):
        if not os.path.exists(value):
            raise ValueError(f"目录 '{value}' 不存在")
        return value

    @validator('output_dir')
    def validate_output_dir_exists(cls, value):
        if not os.path.exists(value):
            # 校验目录是否存在 不存在则创建目录
            os.makedirs(value)
        return value