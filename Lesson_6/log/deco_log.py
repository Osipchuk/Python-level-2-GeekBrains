import logging
from logging.handlers import RotatingFileHandler
import inspect


def log(filename):

    def deco(func):

        def warp(*args, **kwargs):

            deco_log = logging.getLogger('deco')

            _format = logging.Formatter('%(asctime)s\t%(levelname)s\t%(message)s"%(filename)s"')

            deco_fh = logging.FileHandler(filename, encoding='utf-8')
            deco_fh.setLevel(logging.INFO)
            deco_fh.setFormatter(_format)

            deco_log.addHandler(deco_fh)
            deco_log.setLevel(logging.INFO)

            f = inspect.stack()[1][3]
            if f != '<module>':
                message = f'Функция "{func.__name__}" вызвана из функции "{f}" файла '
            else:
                message = f'Функция "{func.__name__}" вызвана из файла '

            deco_log.info(message)

            return func(*args, **kwargs)
        return warp
    return deco
