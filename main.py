from ProcessData import ProcessData
from Perceptron import Perceptron
from NaiveBayesDigit import NaiveBayes


##test face feature [70*60][1]
validationImages = ProcessData().loadFaceImages('facedatatest.txt')
##test face label [1][1]
validationLabels = ProcessData().makeFaceLabels('facedatatestlabels.txt')
trainingImages = ProcessData().loadFaceImages('facedatatrain.txt')
trainingLabels = ProcessData().makeFaceLabels('facedatatrainlabels.txt')

pcpt = Perceptron( [70*60, 1], .1)
pcpt.main(trainingImages, trainingLabels, 10, 200, validationImages, validationLabels)

validationImages = ProcessData().loadDigitImages('testimages.txt')
validationLabels = ProcessData().makeDigitLabels('testlabels.txt')
trainingImages = ProcessData().loadDigitImages('trainingimages.txt')
trainingLabels = ProcessData().makeDigitLabels('traininglabels.txt')

pcpt = Perceptron( [28*28, 10], .1)
pcpt.main(trainingImages, trainingLabels, 10, 200, validationImages, validationLabels)




##test digit feature [28*28][1]
validationImages = ProcessData().loadDigitImages('testimages.txt')
##test digit label [10][1]
validationLabels = ProcessData().makeDigitLabels('testlabels.txt')

##train digit features
trainingImages = ProcessData().loadDigitImages('trainingimages.txt')
##train digit labels
trainingLabels = ProcessData().makeDigitLabels('traininglabels.txt')


nBD = NaiveBayes(trainingImages)
