from utils.db import get_connection


class SchemaReader:

    def read_schema(self):

        conn = get_connection()
        cursor = conn.cursor()

        schema = {}

        # Get all table names
        cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        AND name NOT LIKE 'sqlite_%';
        """)

        tables = cursor.fetchall()

        for table in tables:

            table_name = table[0]

            cursor.execute(f"PRAGMA table_info({table_name})")

            columns = cursor.fetchall()

            schema[table_name] = {
                "columns": [col[1] for col in columns]
            }

        conn.close()

        return schema