from .client import Connection, Client
from .exceptions import (RedisError, ConnectionError, ResponseError,
                         InvalidResponse)
from .connection import ConnectionPool

__version__ = '99.4.20'
VERSION = tuple(int(s) for s in __version__.split('.'))