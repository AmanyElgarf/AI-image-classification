from ProcessData import ProcessData
from Perceptron import Perceptron
import pandas as pd

faceTest = ProcessData().loadFaceImages('facedatatest.txt')
faceTestLabel = ProcessData().makeFaceLabels('facedatatestlabels.txt')
faceTrain = ProcessData().loadFaceImages('facedatatrain.txt')
faceTrainLabel = ProcessData().makeFaceLabels('facedatatrainlabels.txt')

digitTest = ProcessData().loadDigitImages('testimages.txt')
digitTestLabel = ProcessData().makeDigitLabels('testlabels.txt')
digitTrain = ProcessData().loadDigitImages('trainingimages.txt')
digitTrainLabel = ProcessData().makeDigitLabels('traininglabels.txt')


for e in range(1,11):
    for j in range(0, 5):
        data = []
        row = ["Percent Data", "Training Time Face", "Accuracy Face", "Train Time Digit", "Accuracy Digit"]
        data.append(row)
        for p in range(10,110, 10):
            print(p)
            row = []
            row.append(p)

            pcptF = Perceptron([70 * 60, 1], 1)
            time, l = pcptF.main(faceTrain, faceTrainLabel, p, e, faceTest, faceTestLabel)
            print(time)
            row.append(time)
            row.append(l)
            pcptD = Perceptron([28 * 28, 10], 1)
            time, l = pcptD.main(digitTrain, digitTrainLabel, p, e, digitTest, digitTestLabel)
            print(time)
            row.append(time)
            row.append(l)
            print()
            data.append(row)

        df = pd.DataFrame(data)
        name = 'PerceptronData'+str(e)+str(j)+'.csv'
        print(name)
        df.to_csv(name, index=False)


