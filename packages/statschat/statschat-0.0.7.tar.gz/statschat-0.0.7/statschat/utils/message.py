import logging
import re
from typing import List

from statschat.schemes.request import MessageRecords

logger = logging.getLogger(__name__)


class MessageUtil:
    """Message工具类"""

    @staticmethod
    def getCheckTokensMessages(messages: List[MessageRecords], max_tokens: int = 0) -> List[MessageRecords]:
        """获取校验tokens之后的messages"""
        while MessageUtil.getTokens(messages) > max_tokens:
            messages.pop(0)
        return messages

    @staticmethod
    def getTokens(messages: List[MessageRecords]) -> int:
        """获取tokens数量"""
        column = [item.content for item in messages]
        return len("".join(column))

    @staticmethod
    def extractCode(message: str) -> List:
        """提取chatgpt返回文本中的代码"""
        pattern = r"```(.*?)```"
        return re.findall(pattern, message, re.DOTALL)
