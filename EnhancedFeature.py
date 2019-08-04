import itertools
from Images import Images


class Feature:
    def __init__(self, im):
        self.images = im
        self.rows = len(im[0])
        self.columns = len(im[0][0])-1

    def __feature_containers(self):
        no_of_images = len(self.images)
        containers = [[0 for i in range((self.rows//2) * (self.columns//2))] for i in range(no_of_images)]
        return containers

    def extract_features(self):
        temp = [[] for i in range(len(self.images))]

        for i in temp:
            for k in range(self.rows):
                i.append([0 for i in range(self.columns)])

        for n in range(len(self.images)):
            for r in range(self.rows):
                for c in range(self.columns):
                    if self.images[n][r][c] == '\n':
                        continue
                    elif self.images[n][r][c] == "#":
                        temp[n][r][c] = 1
                    elif self.images[n][r][c] == " ":
                        temp[n][r][c] = 0
                    elif self.images[n][r][c] == "+":
                        temp[n][r][c] = 0.5

        temp_one = [[] for i in range(len(self.images))]
        for i in temp_one:
            for k in range(self.rows//2):
                i.append([0 for i in range(self.columns)])
        for i in range(len(temp_one)):
            for c in range(self.columns):
                l = 0
                r = 0
                while r < self.rows:
                    temp_one[i][l][c] = temp[i][r][c] + temp[i][r + 1][c]
                    r += 2
                    l += 1

        temp_two = [[] for i in range(len(self.images))]
        for i in temp_two:
            for k in range(self.rows // 2):
                i.append([0 for i in range(self.columns//2)])
        for i in range(len(temp_two)):
            for r in range(self.rows//2):
                l = 0
                c = 0
                while c < self.columns:
                    temp_two[i][r][l] = temp_one[i][r][c] + temp_one[i][r][c + 1]
                    c += 2
                    l += 1

        temp_three = [[] for i in range(len(self.images))]
        for i in temp_three:
            for k in range(self.rows // 2):
                i.append([0 for i in range(self.columns // 4)])
        for i in range(len(temp_three)):
            for r in range(self.rows // 2):
                l = 0
                c = 0
                while c < self.columns //2:
                    temp_three[i][r][l] = temp_two[i][r][c] + temp_two[i][r][c + 1]
                    c += 2
                    l += 1



        features = self.__feature_containers()

        for i in range(len(temp_two)):
            features[i] = list(itertools.chain.from_iterable(temp_two[i]))

        return features



