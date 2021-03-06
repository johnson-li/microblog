import importlib

import config

db_conf = config.conf.get('db', None)


def get_client():
    module_str = db_conf['module']
    class_str = db_conf['class']

    if not module_str.startswith('db.impl.'):
        raise AttributeError('db client should be located in db.impl: ' + module_str)

    module = importlib.import_module(module_str)
    cls = getattr(module, class_str)
    return cls()
