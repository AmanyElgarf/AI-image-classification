import numpy as np

class Perceptron:

    def __init__(self, layerSizes, learnRate):
        self.layerSizes = layerSizes
        self.learnRate = learnRate
        self.weight = np.array( np.random.randn(layerSizes[1], layerSizes[0]), dtype=np.float128 )
        self.bias = np.array(np.random.randn(layerSizes[1],1), dtype=np.float128)
        self.errorW = np.zeros(self.weight.shape)
        self.errorB = np.zeros(self.bias.shape)

    def main(self, trainingFeatures, trainingLabels, percentTraining, cycles, validationFeatures, validationLabels):
        trainingData = list(zip(trainingFeatures, trainingLabels))
        np.random.shuffle(trainingData)
        del trainingData[ len(trainingData)*percentTraining // 100 - 1 ]
        np.asarray(trainingData)

        avgAccuracy = 0
        for j in range(0, cycles):
            print(j)
            np.random.shuffle(trainingData)
            self.errorW = np.zeros(self.weight.shape)
            self.errorB = np.zeros(self.bias.shape)
            for feature,label in trainingData:
                self.logisticLearn(feature, label)
            # self.weight = self.weight+self.learnRate*self.errorW
            # self.bias = self.bias+self.learnRate*self.errorB

            avgAccuracy += self.calculateAccuracy(validationFeatures, validationLabels)
        print(avgAccuracy/j)

    def linearLearn(self, feature, label):
        prediction = np.dot(self.weight, feature) + self.bias
        prediction = np.where(prediction<0, 0, 1)
        err = label - prediction
        self.errorB += err
        self.errorW += np.dot( err, feature.transpose() )

    def logisticLearn(self, feature, label):
        prediction = np.dot(self.weight, feature) + self.bias
        prediction = prediction/100
        prediction = 1.0/(1.0+np.exp(-prediction))

        err = (prediction-label)*((prediction)*(1-prediction))
        # self.errorB += err
        # self.errorW += np.dot( err, feature.transpose() )

        self.weight = self.weight - self.learnRate * np.dot(err,feature.transpose())
        self.bias = self.bias - self.learnRate * err


    # def calculateAccuracy(self, imageData, labelData):
    #     correct = 0
    #     for image, label in zip(imageData, labelData):
    #         l = self.getPrediction(image)
    #         if l[0][0] == label[0][0]:
    #             correct += 1
    #     percent = correct / len(labelData) * 100
    #     print(percent)
    #     return percent
    #
    # def getPrediction(self, feature):
    #     feature = np.matmul(self.weight, feature) + self.bias
    #     # feature = np.where(feature<0, 0, 1)
    #     feature = feature / 100
    #     feature = 1.0/(1.0+np.exp(-feature))
    #     feature = np.where(feature<.5, 0, 1)
    #     return feature

    def calculateAccuracy(self, imageData, labelData):
        correct = 0
        for image, label in zip(imageData,labelData):
            if self.getPrediction(image) == np.argmax(label):
                correct+=1
        percent = correct/len(labelData)*100
        print(percent)
        return percent

    def getPrediction(self, feature):
        feature = np.dot(self.weight,feature)+self.bias
        feature = feature/100
        feature = 1.0/(1.0+np.exp(-feature))
        return np.argmax(feature)

















