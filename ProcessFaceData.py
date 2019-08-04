from Images import Images
from Feature import Feature


class ProcessFaceData:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def main(self):
        return Feature(Images(self.name, self.size).get_images()).extract_features()




