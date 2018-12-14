import logging
from logging.handlers import RotatingFileHandler

client_log = logging.getLogger('client')

_format = logging.Formatter("%(asctime)s\t%(levelname)s\t%(module)s\t%(message)s\t")


fh = RotatingFileHandler('client_log', maxBytes=2**15, backupCount=2, encoding='utf-8')
fh.setLevel(logging.INFO)
fh.setFormatter(_format)

client_log.addHandler(fh)
client_log.setLevel(logging.INFO)
