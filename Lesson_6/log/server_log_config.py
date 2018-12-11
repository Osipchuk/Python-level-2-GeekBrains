import logging
from logging.handlers import TimedRotatingFileHandler

server_log = logging.getLogger('server')

_format = logging.Formatter("%(asctime)s\t%(levelname)s\t%(module)s\t%(message)s\t")

fh = TimedRotatingFileHandler('server_log', when='D', interval=1, backupCount=5, encoding='utf-8')
fh.setLevel(logging.INFO)
fh.setFormatter(_format)

server_log.addHandler(fh)
server_log.setLevel(logging.INFO)
