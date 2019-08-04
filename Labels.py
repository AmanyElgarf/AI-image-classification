class Labels:
    def __init__(self, file_name):
        self.file_name = file_name

    def __open_file(self):
        f = open(str(self.file_name), 'r')
        readlines = f.readlines()
        f.close()
        readlines[len(readlines)-1] = readlines[len(readlines)-1] + '\n'
        return readlines

    def get_labels(self):
        return self.__open_file()




