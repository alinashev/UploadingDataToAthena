from Commons.ReaderJSON import ReaderJSON
from Commons.StorageS3 import StorageS3
from Transform.ChannelParser import ChannelParser
from Transform.VideoIDParser import VideoIDParser
from Transform.VideoParser import VideoParser


def main():
    channel: str = "BringMeTheHorizon UCAayZDDj3uom0QpSJiwLoUw"
    ch_name: str = channel.split()[0]
    ch_id: str = channel.split()[1]

    channel_id: dict = {ch_name: ch_id}

    storage: StorageS3 = StorageS3(bucket_name="a-test-01-bucket")

    chd_file_name: str = "chd" + ch_id + ".json"
    vd_file_name: str = "vd" + ch_id + ".json"
    ctd_file_name: str = "ctd" + ch_id + ".json"

    storage.download_file("Resources/2022-01-24/20h/channelData/" + chd_file_name,
                          chd_file_name)

    storage.download_file("Resources/2022-01-24/20h/videoData/" + vd_file_name,
                          vd_file_name)

    storage.download_file("Resources/2022-01-24/20h/categoryData/" + ctd_file_name,
                          ctd_file_name)

    chd_reader: ReaderJSON = ReaderJSON(chd_file_name)
    vd_reader: ReaderJSON = ReaderJSON(vd_file_name)
    ctd_reder: ReaderJSON = ReaderJSON(ctd_file_name)

    chd_json: dict = chd_reader.get_json()
    vd_json: dict = vd_reader.get_json()
    ctd_json: dict = ctd_reder.get_json()

    chd_parser: ChannelParser = ChannelParser()
    vd_id_parser: VideoIDParser = VideoIDParser()
    ctd_parser: VideoParser = VideoParser()

    chd_parser.parse(chd_json, channel_id)
    video_id_list = vd_id_parser.parse(vd_json, channel_id)
    ctd_parser.parse(ctd_json, video_id_list)


if __name__ == '__main__':
    main()
