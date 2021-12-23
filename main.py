from Commons.ChannelsID import ChannelsID
from Commons.Parquet import Parquet
from Commons.ReaderJSON import ReaderJSON
from Commons.StorageS3 import StorageS3
from Transform.ChannelParser import ChannelParser
from Transform.VideoIDParser import VideoIDParser
from Transform.VideoParsesr import VideoParser


def main():
    storage: StorageS3 = StorageS3()
    storage.download_folder('RES')

    reader_channel: ReaderJSON = ReaderJSON('RES/YouTube/tmp/dataChannels.json')
    reader_video_id: ReaderJSON = ReaderJSON('RES/YouTube/tmp/dataVideos.json')
    reader_video_category: ReaderJSON = ReaderJSON('RES/YouTube/tmp/videoCategory.json')

    json_channel: dict = reader_channel.get_json()
    json_video_id: dict = reader_video_id.get_json()
    json_video_category: dict = reader_video_category.get_json()

    channel_id: dict = ChannelsID('channels.txt').get_channels_id()

    channel_parser: ChannelParser = ChannelParser()
    video_id_parser: VideoIDParser = VideoIDParser()
    video_parser: VideoParser = VideoParser()

    channel_parser.parse(json_channel, channel_id)
    video_id_list: list = video_id_parser.parse(json_video_id, channel_id)
    video_parser.parse(json_video_category, video_id_list)

    Parquet.load(channel_parser.get_fact_channel_obj_list(), "factChannel.parquet")
    Parquet.load(channel_parser.get_dim_channel_obj_list(), "dimChannel.parquet")
    Parquet.load(channel_parser.get_dim_date_obj_list(), "dimDateChannel.parquet")
    Parquet.load(channel_parser.get_dim_time_obj_list(), "dimTimeChannel.parquet")

    Parquet.load(video_parser.get_fact_video_obj_list(), "factVideo.parquet")
    Parquet.load(video_parser.get_dim_video_obj_list(), "dimVideo.parquet")
    Parquet.load(video_parser.get_dim_date_obj_list(), "dimDateVideo.parquet")
    Parquet.load(video_parser.get_dim_time_obj_list(), "dimTimeVideo.parquet")


if __name__ == '__main__':
    main()
