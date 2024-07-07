from PIL import Image


class GenerateVersions:
    """- генератор версий картинок """

    # def __init__(self):
    #     self.__im = Image()

    # Image.Resampling.LANCZOS.
    # image.thumbnail((width, height))

    @staticmethod
    def open():
        """- открыть картинку """
        with Image.open("test.jpg") as img:
            img.thumbnail()





