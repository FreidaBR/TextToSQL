import pandas as pd
from utils.db import get_connection


class SQLExecutor:

    def execute(self, sql):

        conn = get_connection()

        try:
            df = pd.read_sql_query(sql, conn)
            conn.close()
            return df

        except Exception as e:
            conn.close()
            raise Exception(str(e))