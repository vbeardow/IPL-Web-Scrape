import sqlite3
import pandas as pd


class SQLite:
    def __init__(self, name) -> None:
        print(f"SQLite instance {name} created")
        self.name = name
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()

    def insert_record(self, table_name, data) -> None:
        print(f"Record inserted into table {table_name}")
        data.to_sql(table_name, self.connection, if_exists="replace", index=False)

    def commit(self) -> None:
        print("Changes commited to db")
        self.connection.commit()

    def close_connection(self) -> None:
        print("SQLite instance closed")
        self.connection.close()
