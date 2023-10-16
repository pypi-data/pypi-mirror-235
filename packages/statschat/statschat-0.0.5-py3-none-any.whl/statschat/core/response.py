import inspect
from typing import TypeVar
from functools import wraps
import logging
from pydantic import BaseModel, ValidationError
from statschat.core.code import ResponseCode
from statschat.schemes.response import ResponseOut

RT = TypeVar('RT')  # 返回类型
logger = logging.getLogger(__name__)


# 通用装饰器，验证传入参数是否符合指定的 Pydantic 模型，以及固定返回结果
def unified_response(func):
    @wraps(func)
    async def decorator(*args, **kwargs) -> ResponseOut:
        # 获取被装饰函数的参数信息
        signature = inspect.signature(func)
        # 将传入的参数与函数签名的参数进行匹配，进行验证
        try:
            bound_args = signature.bind(*args, **kwargs)
        except Exception as e:
            # 处理不传参数的情况
            return ResponseOut(
                **{'code': ResponseCode.PARAMS_INVALID.code, 'msg': ResponseCode.PARAMS_INVALID.msg, 'data': [],
                   'error': str(e)})

        bound_args.apply_defaults()
        # 遍历函数签名的参数
        for param_name, param_value in bound_args.arguments.items():
            param_type = signature.parameters[param_name].annotation
            if isinstance(param_type, type) and issubclass(param_type, BaseModel):
                # 如果参数类型是 Pydantic 模型
                try:
                    # 将参数值构造成一个包含字段名的字典，然后传递给 Pydantic 模型的构造函数
                    validated_data = param_type(**param_value)
                    bound_args.arguments[param_name] = validated_data
                except ValidationError as e:
                    # 如果验证失败,返回错误信息
                    return ResponseOut(
                        **{'code': ResponseCode.PARAMS_INVALID.code, 'msg': ResponseCode.PARAMS_INVALID.msg,
                           'error': e.json(), 'data': []})
        try:
            if inspect.iscoroutinefunction(func):
                resp = await func(**bound_args.arguments) or []
            else:
                resp = func(**bound_args.arguments) or []
            # 返回成功信息
            response = {'code': ResponseCode.SUCCESS.code, 'msg': ResponseCode.SUCCESS.msg, 'data': resp}
        except AssertionError as e:
            # 处理断言错误，返回错误信息
            response = {'code': ResponseCode.FAILED.code, 'msg': ResponseCode.FAILED.msg, 'data': [], 'error': str(e)}
        except TimeoutError as e:
            # 处理请求超时错误，返回错误信息
            response = {'code': ResponseCode.TIMEOUT_ERROR.code, 'msg': ResponseCode.TIMEOUT_ERROR.msg, 'data': [],
                        'error': str(e)}
        except Exception as e:
            # 处理其他程序错误，返回内部服务器错误信息
            response = {'code': ResponseCode.SYSTEM_ERROR.code, 'msg': ResponseCode.SYSTEM_ERROR.msg, 'data': [],
                        'error': str(e)}
        return ResponseOut(**response)

    return decorator
