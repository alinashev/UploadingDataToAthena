from typing import Any

import pandas
from pandas import DataFrame


class Parquet:
    @staticmethod
    def load(entity: Any, file_name: str) -> None:
        data_frame: DataFrame = pandas.DataFrame([e.to_dict() for e in entity])
        data_frame.to_parquet(file_name, engine='fastparquet')

    @staticmethod
    def read(file_name) -> DataFrame:
        return pandas.read_parquet(file_name)
