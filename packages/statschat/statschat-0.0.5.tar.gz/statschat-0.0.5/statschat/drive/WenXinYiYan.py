"""
文心一言 驱动
"""
from typing import List

from statschat.drive.interface import LLM
from statschat.schemes.model import ConfigIn
from statschat.schemes.request import MessageRecords


class WenXinYiYan(LLM):
    def __init__(self, config: ConfigIn):
        pass

    async def send_text_msg(self, msg: str):
        pass

    async def request(self, messages: List[MessageRecords]):
        pass
