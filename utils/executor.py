import pandas as pd

from utils.db import get_connection


class SQLExecutor:

    def execute(self, sql):

        conn = get_connection()

        df = pd.read_sql_query(sql, conn)

        conn.close()

        return df