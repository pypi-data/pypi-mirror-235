import json


class ToolsUtil:
    """Tools工具类"""

    @staticmethod
    def is_json_string(data) -> bool:
        try:
            json.loads(data)
            return True
        except json.JSONDecodeError:
            return False
