import numpy as np
import timeit
import random

class Perceptron:

    def __init__(self, layerSizes, learnRate):
        self.layerSizes = layerSizes
        self.learnRate = learnRate
        self.weight = np.array( np.random.randn(layerSizes[1], layerSizes[0]), dtype=np.float128 )
        self.bias = np.array(np.random.randn(layerSizes[1],1), dtype=np.float128)

    def demo(self, trainingFeatures, trainingLabels, percentTraining, cycles):
        trainingData = list(zip(trainingFeatures, trainingLabels))
        np.random.shuffle(trainingData)
        del trainingData[ len(trainingData)*percentTraining // 100 - 1 : len(trainingData) ]
        np.asarray(trainingData)

        self.weight = np.array(np.random.randn(self.layerSizes[1], self.layerSizes[0]), dtype=np.float128)
        self.bias = np.array(np.random.randn(self.layerSizes[1], 1), dtype=np.float128)

        for j in range(0, cycles):
            np.random.shuffle(trainingData)
            for feature,label in trainingData:
                self.logisticLearn(feature, label)

    def demoTest(self,  validationFeatures, validationLabels):
        i = random.randint(0, len(validationFeatures)-1)
        print("Index of Test Image: " + str(i))
        image = validationFeatures[i]
        label = validationLabels[i]
        prediction = self.getPrediction(image)
        if label.size == 1:
            prediction = np.where(prediction < .5, 0, 1)
            print("Label: " + str(label[0][0]))
            print("Prediction: "+  str(prediction[0][0]))
        else:
            prediction = np.argmax(prediction)
            print("Label: " + str(np.argmax(label)))
            print("Prediction: " + str(prediction))
        print()

    def main(self, trainingFeatures, trainingLabels, percentTraining, cycles, validationFeatures, validationLabels):
        trainingData = list(zip(trainingFeatures, trainingLabels))
        np.random.shuffle(trainingData)
        del trainingData[ len(trainingData)*percentTraining // 100 - 1 : len(trainingData) ]
        np.asarray(trainingData)

        start_time = timeit.default_timer()
        for j in range(0, cycles):
            np.random.shuffle(trainingData)
            for feature,label in trainingData:
                self.logisticLearn(feature, label)
        time = timeit.default_timer() - start_time
        l = self.calculateAccuracy(validationFeatures, validationLabels)
        print(l)
        return time, l

    def linearLearn(self, trainingData):
        errorW = np.zeros(self.weight.shape)
        errorB = np.zeros(self.bias.shape)
        for feature, label in trainingData:
            prediction = np.dot(self.weight, feature) + self.bias
            prediction = np.where(prediction<0, 0, 1)
            err = label - prediction
            errorB += err
            errorW += np.dot( err, feature.transpose() )
        self.weight = self.weight+self.learnRate*errorW
        self.bias = self.bias+self.learnRate*errorB

    def logisticLearn(self, feature, label):
        prediction = self.getPrediction(feature)
        err = (prediction-label)*((prediction)*(1-prediction))
        self.weight = self.weight - self.learnRate * np.dot(err,feature.transpose())
        self.bias = self.bias - self.learnRate * err

    def calculateAccuracy(self, imageData, labelData):
        correct = 0
        for image, label in zip(imageData,labelData):
            prediction = self.getPrediction(image)
            if label.size == 1:
                if np.where(prediction < .5, 0, 1) == label:
                    correct += 1
            elif np.argmax(prediction) == np.argmax(label):
                correct+=1
        percent = correct/len(labelData)*100
        return percent

    def getPrediction(self, feature):
        f = np.dot(self.weight,feature)+self.bias
        return 1.0/(1.0+np.exp(-f/100))













