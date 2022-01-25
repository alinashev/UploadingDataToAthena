from Commons.DataVersion import DataVersion
from Commons.ReaderJSON import ReaderJSON
from Commons.StorageS3 import StorageS3
from Load.ParquetFormat import ParquetFormat
from Transform.ChannelParser import ChannelParser
from Transform.VideoIDParser import VideoIDParser
from Transform.VideoParser import VideoParser


def main():
    version = DataVersion()

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

    ParquetFormat.load(chd_parser.get_fact_channel_obj_list(), "FC-" + ch_id + ".parquet")
    ParquetFormat.load(chd_parser.get_dim_channel_obj_list(), "DC-" + ch_id + ".parquet")
    ParquetFormat.load(chd_parser.get_dim_date_obj_list(), "DDC-" + ch_id + ".parquet")
    ParquetFormat.load(chd_parser.get_dim_time_obj_list(), "DTC-" + ch_id + ".parquet")

    ParquetFormat.load(ctd_parser.get_fact_video_obj_list(), "FV-" + ch_id + ".parquet")
    ParquetFormat.load(ctd_parser.get_dim_video_obj_list(), "DV-" + ch_id + ".parquet")
    ParquetFormat.load(ctd_parser.get_dim_date_obj_list(), "DDV-" + ch_id + ".parquet")
    ParquetFormat.load(ctd_parser.get_dim_time_obj_list(), "DTV-" + ch_id + ".parquet")

    storage.upload("FC-" + ch_id + ".parquet",
                   "Data/Channel/FactCahnnel/" + version.get_date() + "/" + version.get_hour())
    storage.upload("DC-" + ch_id + ".parquet",
                   "Data/Channel/DimChannel/" + version.get_date() + "/" + version.get_hour())
    storage.upload("DDC-" + ch_id + ".parquet",
                   "Data/Channel/DimDateChannel/" + version.get_date() + "/" + version.get_hour())
    storage.upload("DTC-" + ch_id + ".parquet",
                   "Data/Channel/DimTimeChannel/" + version.get_date() + "/" + version.get_hour())

    storage.upload("FV-" + ch_id + ".parquet",
                   "Data/Video/FactVideo/" + version.get_date() + "/" + version.get_hour())
    storage.upload("DV-" + ch_id + ".parquet",
                   "Data/Video/DimVideo/" + version.get_date() + "/" + version.get_hour())
    storage.upload("DDV-" + ch_id + ".parquet",
                   "Data/Video/DimDateVideo/" + version.get_date() + "/" + version.get_hour())
    storage.upload("DTV-" + ch_id + ".parquet",
                   "Data/Video/DimTimeVideo/" + version.get_date() + "/" + version.get_hour())


if __name__ == '__main__':
    main()
