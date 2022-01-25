from Commons.StorageS3 import StorageS3


def main():
    channel_id = "UC05WaqA-0OLM5Y7NmmHq1hw"
    storage = StorageS3(bucket_name="a-test-01-bucket")
    storage.download_file("Resources/2022-01-24/20h/channelData/" + "chd" + channel_id + ".json",
                          "chd" + channel_id + ".json")

    storage.download_file("Resources/2022-01-24/20h/videoData/" + "vd" + channel_id + ".json",
                          "vd" + channel_id + ".json")

    storage.download_file("Resources/2022-01-24/20h/categoryData/" + "ctd" + channel_id + ".json",
                          "ctd" + channel_id + ".json")


if __name__ == '__main__':
    main()
