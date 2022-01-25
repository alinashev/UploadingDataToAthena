from typing import Any
from Commons.AthenaDataBase import AthenaDataBase

from Commons.DataVersion import DataVersion


class Loader:
    @staticmethod
    def load(file) -> None:
        try:
            data_base: AthenaDataBase = AthenaDataBase()
            connect: Any = data_base.connect()
            cursor: Any = connect.cursor()

            sql_file = open(file, 'r')
            cursor.execute(sql_file.read().format(database="a-test-db-01",
                                                  bucket="a-test-01-bucket"))
        except Exception as error:
            print(error)
