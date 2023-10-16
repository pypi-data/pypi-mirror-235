from typing import Any, Optional

from pymysql.cursors import Cursor, DictCursor
from dbutils.pooled_db import PooledDB
from dbutils.steady_db import SteadyDBConnection
from utils.db.mysql._collection import MysqlCollection
from utils.db.mysql._result import MysqlResult
from utils.db.mysql._types import RES_TYPE


class MysqlPool(MysqlCollection):
    pool: Optional[PooledDB] = None

    def __init__(self, creator: Any, *args, **kwargs):
        super().__init__(max_connections=10, min_cached=5, max_cached=10, max_shared=10)
        if self.pool is None:
            self.pool = PooledDB(
                creator,
                self.min_cached,
                self.max_cached,
                self.max_shared,
                self.max_connections,
                self.blocking,
                setsession=self.set_session,
                ping=self.ping,
                *args, **kwargs
            )

    def running(self, sql: str, data: Any = None, many: bool = False) -> MysqlResult:
        conn: SteadyDBConnection = self.pool.connection()
        cursor: DictCursor = conn.cursor(DictCursor)
        result: MysqlResult = self.execute(conn, cursor, sql, data, many)
        return result


if __name__ == '__main__':
    import pymysql

    pool = MysqlPool(creator=pymysql, host="localhost", port=3306, user="root", password="zyhyyp941224",
                     database="dev-lc-lm-business")
    pool.running("select * from faq_info where status=%s;", data=("published",))
