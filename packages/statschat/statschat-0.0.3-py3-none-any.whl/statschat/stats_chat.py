import sys
from statschat.drive.ChatGPT import *
from pydantic import ValidationError
from statschat.schemes.model import ModelDataIn


class SingletonDecorator(object):
    _instance = None

    def __init__(self, cls):
        self._cls = cls

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = self._cls(*args, **kwargs)
        return self._instance

    @staticmethod
    def get_model(model_data: dict):
        try:
            # 将参数值构造成一个包含字段名的字典，然后传递给 Pydantic 模型的构造函数
            model_data_in = ModelDataIn(**model_data)
            # 反射类
            model_class = getattr(sys.modules[__name__], model_data_in.model.value)
            # 实例化并返回类
            return model_class(model_data_in)
        except ValidationError as e:
            # 如果验证失败,终止继续往下执行，打印错误信息
            logger.info(f"Invalid parameter: {e.json()}")
        except Exception as e:
            # 如果验证失败,终止继续往下执行，打印错误信息
            logger.info(f"error: {e}")


@SingletonDecorator
class StatsCHAT(object):
    pass
