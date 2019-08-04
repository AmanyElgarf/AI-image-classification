from ProcessFaceData import ProcessFaceData
from Labels import Labels
import pickle


class NaiveBayes:
    def __init__(self, feature):
        self.face_data = []
        self.labels = []
        self.feature = feature

    def __labels(self):
        no_of_labels = [0.0, 0.0]
        for i in self.labels:
            if i == '0\n':
                no_of_labels[0] += 1.0
            if i == '1\n':
                no_of_labels[1] += 1.0
        return no_of_labels

    def __probability_of_face(self):
        return self.__labels()[1] / float(len(self.labels))

    def __probability_of_not_face(self):
        return self.__labels()[0] / float(len(self.labels))

    def __feature_given_face(self, feature_frequency):
        return float(feature_frequency)/float(self.__labels()[1])

    def __feature_given_not_face(self, feature_frequency):
        return float(feature_frequency)/float(self.__labels()[0])

    def probability_being_a_face(self):
        p = self.__probability_of_face()
        for i in range(len(self.feature)):
            feature_frequency = 0
            for k in range(len(self.face_data)):
                if self.labels[k] == '1\n':
                    if self.face_data[k][i] == self.feature[i]:
                        feature_frequency += 1
            if feature_frequency == 0:
                feature_frequency += 0.1
            p = p * self.__feature_given_face(feature_frequency)
        return p

    def probability_not_being_a_face(self):
        p = self.__probability_of_not_face()
        for i in range(len(self.feature)):
            feature_frequency = 0
            for k in range(len(self.face_data)):
                if self.labels[k] == '0\n':
                    if self.face_data[k][i] == self.feature[i]:
                        feature_frequency += 1
            if feature_frequency == 0:
                feature_frequency += 0.01
            p = p * self.__feature_given_not_face(feature_frequency)
        return p

    def naive(self):
        with open('processed_face_data.pkl', 'rb') as g:
            face_data = pickle.load(g)
        with open('Processed_labels.pkl', 'rb') as f:
            labels = pickle.load(f)
        self.face_data = face_data
        self.labels = labels


labels = Labels('Data/facedata/facedatatestlabels.txt').get_labels()
r = 0

for i in range(150):
    feature = ProcessFaceData('Data/facedata/facedatatest.txt').main()[i]
    amany = NaiveBayes(feature)
    amany.naive()
    maxx = max(amany.probability_being_a_face(), amany.probability_not_being_a_face())
    if amany.probability_being_a_face() > amany.probability_not_being_a_face() and labels[i] == '1\n':
        r += 1
        print('correct')
    elif amany.probability_being_a_face() < amany.probability_not_being_a_face() and labels[i] == '0\n':
        r += 1
        print('correct')

    else:
        print('wrong')
print(r)

