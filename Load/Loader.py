from typing import Any
from Commons.AthenaDataBase import AthenaDataBase
from DataVersion import DataVersion


class Loader:
    @staticmethod
    def load(file) -> None:
        version = DataVersion()
        try:
            data_base: AthenaDataBase = AthenaDataBase()
            connect: Any = data_base.connect()
            cursor: Any = connect.cursor()

            sql_file = open(file, 'r')
            cursor.execute(sql_file.read().format(dir=version.get_version()))
        except Exception as error:
            print(error)
