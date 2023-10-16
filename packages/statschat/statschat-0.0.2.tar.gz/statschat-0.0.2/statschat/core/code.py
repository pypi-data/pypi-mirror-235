from collections import namedtuple

HttpCode = namedtuple('HttpResp', ['code', 'msg'])


class ResponseCode:
    """响应结果
    """
    SUCCESS = HttpCode(1, '处理成功')
    FAILED = HttpCode(101, '处理失败')
    PARAMS_INVALID = HttpCode(102, '参数错误')
    TIMEOUT_ERROR = HttpCode(103, '请求超时')
    SYSTEM_ERROR = HttpCode(500, '系统错误')
