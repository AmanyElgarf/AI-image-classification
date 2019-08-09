import pickle
from ProcessData import ProcessData


#read digits
#read test

digitTestFeatures = ProcessData().loadDigitImages('testimages.txt')
f = open('digitTestFeatures', "wb")
pickle.dump(digitTestFeatures, f)
f.close()

digitTestLabels = ProcessData().makeDigitLabels('testlabels.txt')
f = open('digitTestLabels', "wb")
pickle.dump(digitTestLabels, f)
f.close()

#read validation
digitValidationFeatures = ProcessData().loadDigitImages('validationimages.txt')
f = open('digitValidationFeatures', "wb")
pickle.dump(digitValidationFeatures, f)
f.close()


digitValidationLabels = ProcessData().makeDigitLabels('validationlabels.txt')
f = open('digitValidationLabels', "wb")
pickle.dump(digitValidationLabels, f)
f.close()

#read trainin
digitTrainingFeatures = ProcessData().loadDigitImages('trainingimages.txt')
f = open('digitTrainingFeatures', "wb")
pickle.dump(digitTrainingFeatures, f)
f.close()

digitTrainingLabels = ProcessData().makeDigitLabels('traininglabels.txt')
f = open('digitTrainingLabels', "wb")
pickle.dump(digitTrainingLabels, f)
f.close()
