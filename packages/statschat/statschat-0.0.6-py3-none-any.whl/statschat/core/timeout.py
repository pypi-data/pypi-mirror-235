import asyncio


def timeout(seconds):
    """超时装饰器"""

    def decorator(func):
        async def wrapper(*args, **kwargs):
            try:
                # 使用asyncio.wait_for来设置超时时间
                return await asyncio.wait_for(func(*args, **kwargs), timeout=seconds)
            except asyncio.TimeoutError:
                raise TimeoutError("Task timed out after {} seconds.".format(seconds))
            except Exception as e:
                raise Exception(e)

        return wrapper

    return decorator
