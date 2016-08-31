import inspect

import webrpc.logic.user

func_map = {func.__name__: func for func in
            [getattr(webrpc.logic.user, func_name) for func_name in dir(webrpc.logic.user) if
             not func_name.startswith('_')] if inspect.isfunction(func)}


class Client:
    def __init__(self):
        pass

    def __getattr__(self, item):
        func = func_map.get(item, None)
        if func:
            return func
        raise AttributeError('{} object has no attribute {}'.format(self.__class__, item))
