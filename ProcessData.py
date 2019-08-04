
import pickle
import numpy as np

class ProcessData:
    def __init__(self):
        pass

        #to use: look at main function, how i used it.

    def loadFaceImages(self, fileName):
        fileName = 'Data/facedata/' + fileName
        f = open(fileName)
        lines = f.readlines()
        f.close()

        # list of images
        images = []

        # each image is 70x60, currently each element is 0
        image = np.zeros((70, 60))
        k = 0
        i = 0
        #for each line
        while k < len(lines):
            if (i == 70):
                i = 0
                images.append(image)
                image = np.zeros((70, 60))
            line = lines[k]
            for c, j in zip(line, range(0, 60)):
                if c == '\n':
                    continue
                elif c == '#':
                    image[i][j] = 1
                elif c == '+':
                    image[i][j] = .5
            k += 1
            i += 1

        features = self.extractFeatures(images)

        #returns a list of vectors (70*60)x1, each vector represents 1 image
        return features

    def makeFaceLabels(self, fileName):
        fileName = 'Data/facedata/'+fileName
        f = open(fileName)
        lines = f.readlines()
        f.close()

        #convert list of each line into integer list
        integers = list(map(int, lines))

        #initialize 1x1 numpy vector to represent labels
        labels = [np.zeros((1, 1)) for i in range(len(lines))]

        #make element at index of label to 1 if face, or 0 if not
        #0 = [[0]] (not face)
        #1 = [[1]] (face)
        for i, vector in zip(integers, labels):
            vector[0][0] = i

        return labels

    def loadDigitImages(self, fileName):
        #make a list of each line from txt file
        fileName = 'Data/digitdata/'+fileName
        f = open(fileName)
        lines = f.readlines()
        f.close()

        #initialize 28x28 matrices for each image in the txt file (number of lines // 28 = number of images)
        images = []

        image = np.zeros((28, 28))
        k=0
        i=0
        while k < len(lines):
            if (i == 28):
                i = 0
                images.append(image)
                image = np.zeros((28, 28))
            line = lines[k]
            for c, j in zip(line, range(0, 28)):
                if c == '\n':
                    continue
                elif c == '#':
                    image[i][j] = 1
                elif c == '+':
                    image[i][j] = .5
            k += 1
            i += 1

        features = self.extractFeatures(images)

        #returns a list of vectors (28*28)x1, each vector represents 1 image
        return features

    def makeDigitLabels(self, fileName):
        fileName = 'Data/digitdata/'+fileName
        f = open(fileName)
        lines = f.readlines()
        f.close()

        #take the character at each line, make it an int, convert it to list
        integers = list(map(int, lines))

        #initialize listof  10x1 numpy vectors for each label
        #each label is a 10x1 vector of zeros, with one value as 1, the index where 1
        # is the number represented by label
        # 5 =   [ [0]
        #         [0]
        #         [0]
        #         [0]
        #         [0]
        #         [1]
        #         [0]
        #         [0]
        #         [0]
        #         [0] ]
        labels = [np.zeros((10, 1)) for i in range(len(lines))]

        #if number is 5, i=5, and [5][0] will be set to 1
        for i, vector in zip(integers, labels):
            vector[i][0] = 1

        return labels

    def extractFeatures(self, images):
        # no averaging take the values for each change, make it into a vector, instead of matrix
        # for each image in images, take the size and make it a vector, add to a list called features.
        features = [img.reshape(img.size,1) for img in images]
        return features

    def originalExtractFeatures(self, images):
        # initialize numpy vector to represent the features for each image, divide the number of elements by 4
        # since we are taking average over 4 elemnts
        features = [np.zeros( (img.size//4, 1) ) for img in images]

        # iterate thru each image in the data to extract its feature
        for image,ft in zip(images,features):
            #iterate thru each element of feature for first image
            x = np.nditer(ft, op_flags=['writeonly'])
            for i in range(0, 28, 2):
                for j in range(0, 28, 2):
                    #create a 4x4 submatrix of the image
                    submatrix = image[i:i+2, j:j+2]
                    #get average for all 4 of these elements and set to feature
                    x[0] = np.mean(submatrix)
                    x.iternext()
                    if (x.finished): break
                if (x.finished): break
        return features

    def unpickleFile(self, fileName):
        fileName = 'Data/ProcessedData/'+fileName
        f = open(fileName, "rb")
        data = pickle.load(f)
        return data


