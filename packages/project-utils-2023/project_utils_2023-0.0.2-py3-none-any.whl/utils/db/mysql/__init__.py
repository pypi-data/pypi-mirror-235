from utils.db.mysql._pool import MysqlPool
from utils.db.mysql._result import MysqlResult

mysql_pool = pool = MysqlPool
mysql_result = result = MysqlResult

__all__ = [
    "mysql_pool",
    "pool",
    "MysqlPool",
    "mysql_result",
    "result",
    "MysqlResult"
]
