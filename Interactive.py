from ProcessData import ProcessData
from Perceptron import Perceptron

class Interactive:
    def __init__(self):
        self.faceTest = ProcessData().loadFaceImages('facedatatest.txt')
        self.faceTestLabel = ProcessData().makeFaceLabels('facedatatestlabels.txt')
        self.faceTrain = ProcessData().loadFaceImages('facedatatrain.txt')
        self.faceTrainLabel = ProcessData().makeFaceLabels('facedatatrainlabels.txt')

        self.digitTest = ProcessData().loadDigitImages('testimages.txt')
        self.digitTestLabel = ProcessData().makeDigitLabels('testlabels.txt')
        self.digitTrain = ProcessData().loadDigitImages('trainingimages.txt')
        self.digitTrainLabel = ProcessData().makeDigitLabels('traininglabels.txt')

        self.epoch = 3
        self.pcptF = Perceptron([70 * 60, 1], 1)
        self.pcptD = Perceptron([28 * 28, 10], 1)

    def run(self):
        user_input = None
        percent = user_input
        print("0: Change a percentage\n"
              "1: Test faces\n"
              "2: Test digits\n"
              "q: Quit\n")

        while user_input != "q":

            user_input = input("Choose an action from above : ")

            if user_input == str(0):
                percent = int ( input("Choose a percentage: ") )
                self.pcptF.demo(self.faceTrain, self.faceTrainLabel, percent, self.epoch)
                self.pcptD.demo(self.digitTrain, self.digitTrainLabel, percent, self.epoch)


            if user_input == str(1):
                if percent == None:
                    percent = int(input("Choose a percentage: "))
                    self.pcptF.demo(self.faceTrain, self.faceTrainLabel, percent, self.epoch)
                self.pcptF.demoTest(self.faceTest, self.faceTestLabel)


            if user_input == str(2):
                if percent == None:
                    percent = int(input("Choose a percentage: "))
                    self.pcptD.demo(self.digitTrain, self.digitTrainLabel, percent, self.epoch)
                self.pcptD.demoTest(self.digitTest, self.digitTestLabel)


Interactive().run()


