from minio import Minio


class StorageManager:
    __client = None

    @property
    def client(self) -> Minio:
        return self.__client

    def init(self, **kwargs):
        if not self.__client:
            self.__client = Minio(**kwargs)

    def make_buckets(self, buckets: list):
        for bucket in buckets:
            if not self.__client.bucket_exists(bucket):
                self.__client.make_bucket(bucket)


storage_manager = StorageManager()
