from typing import Any

from DWHEntities.Video.DimDateVideo import DimDateVideo
from DWHEntities.Video.DimTimeVideo import DimTimeVideo
from DWHEntities.Video.DimVideo import DimVideo
from DWHEntities.Video.FactVideo import FactVideo
from Transform.Parser import Parser


class VideoParser(Parser):
    def __init__(self) -> None:
        self.fact_video_obj_list: list = list()
        self.dim_video_obj_list: list = list()
        self.dim_date_obj_list: list = list()
        self.dim_time_obj_list: list = list()

    def parse(self, json_string: Any, video_obj_list: Any) -> None:
        for obj in video_obj_list:
            res_title: str = str(json_string[obj.get_video_id()]['items'][0]['snippet']['localized']['title'])
            res_description: str = str(json_string[obj.get_video_id()]['items'][0]['snippet']['localized']['description'])
            res_view_count: int = int(json_string[obj.get_video_id()]['items'][0]['statistics']['viewCount'])
            res_like_count: int = int(json_string[obj.get_video_id()]['items'][0]['statistics']['likeCount'])
            res_category_id: str = str(json_string[obj.get_video_id()]['items'][0]['snippet']['categoryId'])

            try:
                res_comment_count: int = int(json_string[obj.get_video_id()]['items'][0]['statistics']['commentCount'])
            except KeyError:
                res_comment_count = int(0)

            self.dim_video_obj_list.append(
                DimVideo(str(obj.get_video_id()),
                         str(obj.get_channel_id()),
                         str(obj.get_channel_name()),
                         res_title,
                         res_description,
                         res_category_id
                         ))

            date: DimDateVideo = DimDateVideo()
            time: DimTimeVideo = DimTimeVideo()

            self.dim_date_obj_list.append(date)
            self.dim_time_obj_list.append(time)

            self.fact_video_obj_list.append(
                FactVideo(
                    str(obj.get_video_id()),
                    str(date.get_date_id()),
                    str(time.get_time_id()),
                    res_view_count,
                    res_like_count,
                    res_comment_count
                )
            )

    def get_fact_video_obj_list(self) -> list:
        return self.fact_video_obj_list

    def get_dim_video_obj_list(self) -> list:
        return self.dim_video_obj_list

    def get_dim_date_obj_list(self) -> list:
        return self.dim_date_obj_list

    def get_dim_time_obj_list(self) -> list:
        return self.dim_time_obj_list
