import inspect

from flask import Flask

import www.logic.user

app = Flask(__name__)

WWW_MODULES = [www.logic.user]


def init_app():
    for module in WWW_MODULES:
        module_name = module.__name__.split('.')[-1]
        for func_name in [para_name for para_name in dir(module) if not para_name.startswith('_')]:
            func = getattr(module, func_name)
            if inspect.isfunction(func):
                app.route('/api/{}/{}'.format(module_name, func_name), methods=['GET'])(www.logic.user.ping)


def run():
    app.run()


if __name__ == '__main__':
    init_app()
    run()
