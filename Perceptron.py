import numpy as np



class Perceptron:

    def __init__(self, layerSizes):
        self.layerSizes = layerSizes
        self.weight = [np.random.randn(s1, s) for s,s1 in zip(layerSizes,layerSizes[1:])]
        self.bias = [np.random.randn(s, 1) for s in layerSizes[1:] ]
        self.trainingData = None
        self.validationData = None
        self.testData = None

    def learn(self, feature, label):
        activationFuncs = [feature]
        phiPerLayer = []
        phi = feature
        for w,b in self.weights, self.bias:
            phi = np.matmul(w,phi)+b
            phiPerLayer.append(phi)

            ft = 1/ ( 1-np.exp(-phi) )
            activationFuncs.append(ft)

        error = [np.zeros(b.shape) for b in self.bias]
        errorW = [np.zeros(w.shape) for w in self.weight]
        differenceErr = activationFuncs[-1] - label
        err = np.multiply( differenceErr, self.derivActivation( activationFuncs[-1] ) )
        error[-1] = err


        for i in range(len(self.layerSizes)-2,0,-1):
            w = self.weight[i+1]
            w = np.transpose(w)
            deriv = self.derivActivation[ phi[i] ]
            err = np.multiply( np.matmul(w,error[0]), deriv )
            error[i] = err

            aF = activationFuncs[i-1]
            aF = np.transpose(aF)
            errorW[i] = np.matmul(aF,err)

        return errorW, error


    def derivActivation(self, phi):
        expo = np.exp(-phi)
        derivative = -expo / ((1 - expo) ^ 2)
        return derivative


    def updateWeights(self, sampleData, learningRate):
        totalChangeW = [np.zeros(w.shape) for w in self.weight]
        totalChangeB = [np.zeros(b.shape) for b in self.bias]
        size = len(sampleData)
        for feature,label in sampleData:
            changeW, changeB = self.learn(feature, label)
            totalChangeW = [ (cW + sumW) for cW, sumW in zip(changeW, totalChangeW)]
            totalChangeB = [ (cB + sumB) for cB, sumB in zip(changeB, totalChangeB)]

        scalar = learningRate/size
        self.weight = [ (w - scalar*tW) for w,tW in zip(self.weight, totalChangeW) ]
        self.bias = [ (b - scalar*tB) for b,tB in zip(self.bias, totalChangeB) ]






    def calculatePercentCorrect(self, imageData, labelData):

        total = 0
        wrong = 0
        for image, label in zip(imageData,labelData):
            prediction = self.getPrediction(image)
            value = np.where(label == np.amax(label))
            total+=1
            if (prediction != value):
                wrong+=1

        percent = (total-wrong)/total*100
        print(percent)
        return percent

    def getPrediction(self, feature):
        for w,b in self.weights,self.bias:
            ft = np.matmul(w,feature)+b
            feature = 1/ ( 1-np.exp(-ft) )

        result = np.where(feature == np.amax(feature))
        return result