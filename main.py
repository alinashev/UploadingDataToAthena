from Commons.ChannelsID import ChannelsID
from Load.Loader import Loader

from Load.ParquetFormat import ParquetFormat
from Commons.ReaderJSON import ReaderJSON
from Commons.StorageS3 import StorageS3
from Transform.ChannelParser import ChannelParser
from Transform.VideoIDParser import VideoIDParser
from Transform.VideoParsesr import VideoParser
from DataVersion import DataVersion


def main():
    storage: StorageS3 = StorageS3()
    storage.download_folder('RES', "2021-12-25-1-57")
    version = DataVersion()

    reader_channel: ReaderJSON = ReaderJSON('RES/dataChannels.json')
    reader_video_id: ReaderJSON = ReaderJSON('RES/dataVideos.json')
    reader_video_category: ReaderJSON = ReaderJSON('RES/videoCategory.json')

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

    ParquetFormat.load(channel_parser.get_fact_channel_obj_list(), "factChannel.parquet")
    ParquetFormat.load(channel_parser.get_dim_channel_obj_list(), "dimChannel.parquet")
    ParquetFormat.load(channel_parser.get_dim_date_obj_list(), "dimDateChannel.parquet")
    ParquetFormat.load(channel_parser.get_dim_time_obj_list(), "dimTimeChannel.parquet")

    ParquetFormat.load(video_parser.get_fact_video_obj_list(), "factVideo.parquet")
    ParquetFormat.load(video_parser.get_dim_video_obj_list(), "dimVideo.parquet")
    ParquetFormat.load(video_parser.get_dim_date_obj_list(), "dimDateVideo.parquet")
    ParquetFormat.load(video_parser.get_dim_time_obj_list(), "dimTimeVideo.parquet")

    storage.upload("factChannel.parquet", "Parquet/" + version.get_version() + "/Channel/factChannel")
    storage.upload("dimChannel.parquet", "Parquet/" + version.get_version() + "/Channel/dimChannel")
    storage.upload("dimDateChannel.parquet", "Parquet/" + version.get_version() + "/Channel/dimDateChannel")
    storage.upload("dimTimeChannel.parquet", "Parquet/" + version.get_version() + "/Channel/dimTimeChannel")

    storage.upload("factVideo.parquet", "Parquet/" + version.get_version() + "/Video/factVideo")
    storage.upload("dimVideo.parquet", "Parquet/" + version.get_version() + "/Video/dimVideo")
    storage.upload("dimDateVideo.parquet", "Parquet/" + version.get_version() + "/Video/dimDateVideo")
    storage.upload("dimTimeVideo.parquet", "Parquet/" + version.get_version() + "/Video/dimTimeVideo")

    Loader.load("Tables/factChannel.sql")
    Loader.load("Tables/dimChannel.sql")
    Loader.load("Tables/dimDateChannel.sql")
    Loader.load("Tables/dimTimeChannel.sql")

    Loader.load("Tables/factVideo.sql")
    Loader.load("Tables/dimVideo.sql")
    Loader.load("Tables/dimDateVideo.sql")
    Loader.load("Tables/dimTimeVideo.sql")


if __name__ == '__main__':
    main()
