from Commons.ChannelsID import ChannelsID
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


if __name__ == '__main__':
    main()
