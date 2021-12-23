from typing import Any

from Entities.VideoID import VideoID
from Transform.Parser import Parser


class VideoIDParser(Parser):
    def parse(self, json_string: Any, ChannelsID: Any) -> list[VideoID]:
        obj_list = list()
        for channelID in ChannelsID:
            for i in range(0, 5):
                try:
                    res: str = (json_string[channelID]['items'][i]['id']['videoId'])
                except KeyError:
                    res = str(None)

                obj_list.append(VideoID(channelID,
                                        ChannelsID[channelID],
                                        res))
        return obj_list
