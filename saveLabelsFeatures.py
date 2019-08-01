import pickle
from ProcessData import ProcessData


#read digits
#read test


digitTestFeatures = ProcessData().loadDigitImages('testimages.txt')
f = open('digitTestFeatures', "wb")
pickle.dump(digitTestFeatures, f)


digitTestLabels = ProcessData().loadDigitImages('testlabels.txt')
f = open('digitTestLabels', "wb")
pickle.dump(digitTestLabels, f)

#read validation
digitValidationFeatures = ProcessData().loadDigitImages('validationimages.txt')
f = open('digitValidationFeatures', "wb")
pickle.dump(digitValidationFeatures, f)


digitValidationLabels = ProcessData().loadDigitImages('validationlabels.txt')
f = open('digitValidationLabels', "wb")
pickle.dump(digitValidationLabels, f)

#read trainin
digitTrainingFeatures = ProcessData().loadDigitImages('trainingimages.txt')
f = open('digitTrainingFeatures', "wb")
pickle.dump(digitTrainingFeatures, f)

digitTrainingLabels = ProcessData().loadDigitImages('traininglabels.txt')
f = open('digitTrainingLabels', "wb")
pickle.dump(digitTrainingLabels, f)