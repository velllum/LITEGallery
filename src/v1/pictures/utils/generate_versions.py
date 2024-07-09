from PIL import Image


class PictureVersions:
    """- версии картинок """

    def __init__(self):
        self.__im_original = None

    # Image.Resampling.LANCZOS.
    # image.thumbnail((width, height))

    def init(self, original_file):
        self.__open_original(original_file)

    def __open_original(self, file):
        with Image.open(file) as img:
            self.__im_original = img




