import numpy as np


class ReadData:
    def __init__(self):
        pass

    def open_file(self, file_name):
        f = open(str(file_name), 'r')
        readlines = f.readlines()
        f.close()
        return readlines

    def split_images(self, readlines):
        images = [[] for i in range(len(readlines) // 70)]
        i = 0
        for image in images:
            for k in range(70):
                image.append(readlines[i])
                i += 1
        return images

    


    def main(self, file_name):
        readlines = self.open_file(file_name)
        self.split_images(readlines)










ReadData().main('Data/facedata/facedatatest.txt')
