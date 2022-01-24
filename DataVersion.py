from datetime import datetime


class DataVersion:
    def __init__(self) -> None:
        self.folder_name = None

    def get_version(self) -> str:
        if not self.folder_name:
            self.folder_name = str(datetime.now().date()) + "-" + \
                               str(datetime.now().hour) + "-" + \
                               str(datetime.now().minute)

        return self.folder_name
