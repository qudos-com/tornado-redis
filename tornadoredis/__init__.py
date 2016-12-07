from .client import Connection, Client
from .exceptions import (RedisError, ConnectionError, ResponseError,
                         InvalidResponse)
from .connection import ConnectionPool

__version__ = '99.4.21'
VERSION = tuple(int(s) for s in __version__.split('.'))