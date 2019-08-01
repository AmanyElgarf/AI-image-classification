
import pickle
import numpy as np

class ProcessData:
    def __init__(self):
        pass

    def loadFaceImages(self, fileName):
        pass

    def makeFaceLabels(self, fileName):
        pass

    def loadDigitImages(self, fileName):
        fileName = '/Users/bhartimehta/PycharmProjects/AI-Image-Classification/Data/digitdata/'+fileName
        f = open(fileName)
        lines = f.readlines()
        f.close()

        images = [np.zeros((28, 28)) for i in range( len(lines)//28 ) ]
        for image in images:
            x = np.nditer(image, op_flags=['writeonly'])
            for line in lines:
                for c in line:
                    if c == '\n':
                        continue
                    elif c == '#':
                        x[0] = 1
                    elif c == '+':
                        x[0] = .5
                    x.iternext()
                    if (x.finished): break
                if (x.finished): break


        features = self.extractFeatures(images)

        return features


    def makeDigitLabels(self, fileName):
        fileName = '/Users/bhartimehta/PycharmProjects/AI-Image-Classification/Data/digitdata/'+fileName
        f = open(fileName)
        lines = f.readlines()
        f.close()

        integers = list(map(int, lines))

        labels = [np.zeros((10, 1)) for i in range(len(lines))]

        for i, vector in zip(integers, labels):
            vector[i][0] = 1

        return labels

    def extractFeatures(self, images):

        features = [np.zeros( (img.size//4, 1) ) for img in images]

        for image,ft in zip(images,features):
            x = np.nditer(ft, op_flags=['writeonly'])
            for i in range(0, 8, 2):
                for j in range(0, 8, 2):
                    submatrix = image[i:i+2, j:j+2]
                    x[0] = np.mean(submatrix)
                    x.iternext()
                    if (x.finished): break
                if (x.finished): break

        return features


    def unpickleFile(self, fileName):
        fileName = '/Users/bhartimehta/PycharmProjects/AI-Image-Classification/Data/ProcessedData/'+fileName
        f = open(fileName, "rb")
        data = pickle.load(f)
        return data


