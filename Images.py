class Images:
    def __init__(self, file_name, size):
        self.size = size
        self.file_name = file_name

    def __open_file(self):
        f = open(str(self.file_name), 'r')
        readlines = f.readlines()
        f.close()
        return readlines

    def __split_images(self, readlines):
        images = [[] for i in range(len(readlines) // self.size)]
        i = 0
        for image in images:
            for k in range(self.size):
                image.append(readlines[i])
                i += 1
        return images

    def get_images(self):
        return self.__split_images(self.__open_file())















