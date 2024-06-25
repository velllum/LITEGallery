from minio import Minio


class StorageManager:
    __client = None

    @property
    def client(self) -> Minio:
        return self.__client

    def init(self, **kwargs):
        if not self.__client:
            self.__client = Minio(**kwargs)

    def make_buckets(self, buckets: list | str):
        if isinstance(buckets, list):
            for bucket in buckets:
                self.__make(bucket)
        else:
            self.__make(buckets)

    def __make(self, bucket: str):
        if not self.client.bucket_exists(bucket):
            self.client.make_bucket(bucket)


storage_manager = StorageManager()
