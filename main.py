from Commons.ChannelsID import ChannelsID
from Commons.ReaderJSON import ReaderJSON
from Commons.StorageS3 import StorageS3


def main():
    storage: StorageS3 = StorageS3()
    storage.download_folder('RES')

    reader_channel: ReaderJSON = ReaderJSON('RES/YouTube/tmp/dataChannels.json')
    reader_video_id: ReaderJSON = ReaderJSON('RES/YouTube/tmp/dataVideos.json')
    reader_video_category: ReaderJSON = ReaderJSON('RES/YouTube/tmp/videoCategory.json')

    json_channel = reader_channel.get_json()
    json_video_id = reader_video_id.get_json()
    json_video_category = reader_video_category.get_json()

    channel_id: dict = ChannelsID('channels.txt').get_channels_id()

