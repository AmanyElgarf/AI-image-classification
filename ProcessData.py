
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
        #make a list of each line from txt file
        fileName = 'Data/digitdata/'+fileName
        f = open(fileName)
        lines = f.readlines()
        f.close()

        #initialize 28x28 matrices for each image in the txt file (number of lines // 28 = number of images)
        images = [np.zeros((28, 28)) for i in range( len(lines)//28 ) ]


        for image in images:
            #iterate thru each element of one image matrix
            x = np.nditer(image, op_flags=['writeonly'])
            for line in lines:
                for c in line:
                    #if character is a newline character dont iterate to next element in image, only iterate with ' ', '#', '+'
                    #otherwise it will be larger than 28x28
                    if c == '\n':
                        continue
                    elif c == '#':
                        x[0] = 1
                    elif c == '+':
                        x[0] = .5
                    x.iternext()
                    #if all elements in matrix iterated thru, break to next image matrix
                    if (x.finished): break
                if (x.finished): break


        features = self.extractFeatures(images)

        return features


    def makeDigitLabels(self, fileName):
        fileName = 'Data/digitdata/'+fileName
        f = open(fileName)
        lines = f.readlines()
        f.close()

        #convert list of each line into integer list
        integers = list(map(int, lines))

        #initialize 10x1 numpy vector to represent labels
        labels = [np.zeros((10, 1)) for i in range(len(lines))]

        #make element at index of label to 1
        for i, vector in zip(integers, labels):
            vector[i][0] = 1

        return labels

    def extractFeatures(self, images):

        #initialize numpy vector to represent the features for each image, divide the number of elements by 4
        #since we are taking average over 4 elemnts
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


