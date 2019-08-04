from ProcessFaceData import ProcessFaceData
from Labels import Labels
import pickle


class NaiveBayes:
    def __init__(self, feature):
        self.digit_data = []
        self.labels = []
        self.feature = feature

    def __labels(self):
        no_of_labels = [0.0 for i in range(10)]
        for i in self.labels:
            if i == '0\n':
                no_of_labels[0] += 1.0
            elif i == '1\n':
                no_of_labels[1] += 1.0
            elif i == '2\n':
                no_of_labels[2] += 1.0
            elif i == '3\n':
                no_of_labels[3] += 1.0
            elif i == '4\n':
                no_of_labels[4] += 1.0
            elif i == '5\n':
                no_of_labels[5] += 1.0
            elif i == '6\n':
                no_of_labels[6] += 1.0
            elif i == '7\n':
                no_of_labels[7] += 1.0
            elif i == '8\n':
                no_of_labels[8] += 1.0
            elif i == '9\n':
                no_of_labels[9] += 1.0
        return no_of_labels

    def __probability_of_zero(self):
        return self.__labels()[0] / float(len(self.labels))

    def __probability_of_one(self):
        return self.__labels()[1] / float(len(self.labels))

    def __probability_of_two(self):
        return self.__labels()[2] / float(len(self.labels))

    def __probability_of_three(self):
        return self.__labels()[3] / float(len(self.labels))

    def __probability_of_four(self):
        return self.__labels()[4] / float(len(self.labels))

    def __probability_of_five(self):
        return self.__labels()[5] / float(len(self.labels))

    def __probability_of_six(self):
        return self.__labels()[6] / float(len(self.labels))

    def __probability_of_seven(self):
        return self.__labels()[7] / float(len(self.labels))

    def __probability_of_eight(self):
        return self.__labels()[8] / float(len(self.labels))

    def __probability_of_nine(self):
        return self.__labels()[9] / float(len(self.labels))

    def __feature_given_zero(self, feature_frequency):
        return float(feature_frequency)/float(self.__labels()[0])

    def __feature_given_one(self, feature_frequency):
        return float(feature_frequency)/float(self.__labels()[1])

    def __feature_given_two(self, feature_frequency):
        return float(feature_frequency)/float(self.__labels()[2])

    def __feature_given_three(self, feature_frequency):
        return float(feature_frequency)/float(self.__labels()[3])

    def __feature_given_four(self, feature_frequency):
        return float(feature_frequency)/float(self.__labels()[4])

    def __feature_given_five(self, feature_frequency):
        return float(feature_frequency)/float(self.__labels()[5])

    def __feature_given_six(self, feature_frequency):
        return float(feature_frequency)/float(self.__labels()[6])

    def __feature_given_seven(self, feature_frequency):
        return float(feature_frequency) / float(self.__labels()[7])

    def __feature_given_eight(self, feature_frequency):
        return float(feature_frequency) / float(self.__labels()[8])

    def __feature_given_nine(self, feature_frequency):
        return float(feature_frequency) / float(self.__labels()[9])

    def probability_being_a_zero(self):
        p = self.__probability_of_zero()
        for i in range(len(self.feature)):
            feature_frequency = 0
            for k in range(len(self.digit_data)):
                if self.labels[k] == '0\n':
                    if self.digit_data[k][i] == self.feature[i]:
                        feature_frequency += 1
            if feature_frequency == 0:
                feature_frequency += 0.1
            p = p * self.__feature_given_zero(feature_frequency)
        return p

    def probability_being_a_one(self):
        p = self.__probability_of_one()
        for i in range(len(self.feature)):
            feature_frequency = 0
            for k in range(len(self.digit_data)):
                if self.labels[k] == '1\n':
                    if self.digit_data[k][i] == self.feature[i]:
                        feature_frequency += 1
            if feature_frequency == 0:
                feature_frequency += 0.1
            p = p * self.__feature_given_one(feature_frequency)
        return p

    def probability_being_a_two(self):
        p = self.__probability_of_two()
        for i in range(len(self.feature)):
            feature_frequency = 0
            for k in range(len(self.digit_data)):
                if self.labels[k] == '2\n':
                    if self.digit_data[k][i] == self.feature[i]:
                        feature_frequency += 1
            if feature_frequency == 0:
                feature_frequency += 0.1
            p = p * self.__feature_given_two(feature_frequency)
        return p

    def probability_being_a_three(self):
        p = self.__probability_of_zero()
        for i in range(len(self.feature)):
            feature_frequency = 0
            for k in range(len(self.digit_data)):
                if self.labels[k] == '3\n':
                    if self.digit_data[k][i] == self.feature[i]:
                        feature_frequency += 1
            if feature_frequency == 0:
                feature_frequency += 0.1
            p = p * self.__feature_given_three(feature_frequency)
        return p

    def probability_being_a_four(self):
        p = self.__probability_of_four()
        for i in range(len(self.feature)):
            feature_frequency = 0
            for k in range(len(self.digit_data)):
                if self.labels[k] == '4\n':
                    if self.digit_data[k][i] == self.feature[i]:
                        feature_frequency += 1
            if feature_frequency == 0:
                feature_frequency += 0.1
            p = p * self.__feature_given_four(feature_frequency)
        return p

    def probability_being_a_five(self):
        p = self.__probability_of_five()
        for i in range(len(self.feature)):
            feature_frequency = 0
            for k in range(len(self.digit_data)):
                if self.labels[k] == '0\n':
                    if self.digit_data[k][i] == self.feature[i]:
                        feature_frequency += 1
            if feature_frequency == 0:
                feature_frequency += 0.1
            p = p * self.__feature_given_five(feature_frequency)
        return p

    def probability_being_a_six(self):
        p = self.__probability_of_six()
        for i in range(len(self.feature)):
            feature_frequency = 0
            for k in range(len(self.digit_data)):
                if self.labels[k] == '6\n':
                    if self.digit_data[k][i] == self.feature[i]:
                        feature_frequency += 1
            if feature_frequency == 0:
                feature_frequency += 0.1
            p = p * self.__feature_given_six(feature_frequency)
        return p

    def probability_being_a_seven(self):
        p = self.__probability_of_seven()
        for i in range(len(self.feature)):
            feature_frequency = 0
            for k in range(len(self.digit_data)):
                if self.labels[k] == '7\n':
                    if self.digit_data[k][i] == self.feature[i]:
                        feature_frequency += 1
            if feature_frequency == 0:
                feature_frequency += 0.1
            p = p * self.__feature_given_seven(feature_frequency)
        return p

    def probability_being_a_eight(self):
        p = self.__probability_of_eight()
        for i in range(len(self.feature)):
            feature_frequency = 0
            for k in range(len(self.digit_data)):
                if self.labels[k] == '8\n':
                    if self.digit_data[k][i] == self.feature[i]:
                        feature_frequency += 1
            if feature_frequency == 0:
                feature_frequency += 0.1
            p = p * self.__feature_given_eight(feature_frequency)
        return p

    def probability_being_a_nine(self):
        p = self.__probability_of_nine()
        for i in range(len(self.feature)):
            feature_frequency = 0
            for k in range(len(self.digit_data)):
                if self.labels[k] == '0\n':
                    if self.digit_data[k][i] == self.feature[i]:
                        feature_frequency += 1
            if feature_frequency == 0:
                feature_frequency += 0.1
            p = p * self.__feature_given_nine(feature_frequency)
        return p

    def naive(self):
        with open('processed_digit_data.pkl', 'rb') as g:
            digit_data = pickle.load(g)
        with open('Processed_digit_labels.pkl', 'rb') as f:
            labels = pickle.load(f)
        self.digit_data = digit_data
        self.labels = labels


labels = Labels('Data/digitdata/testlabels.txt').get_labels()
r = 0
w = 0


for i in range(1000):
    feature = ProcessFaceData('Data/digitdata/testimages.txt', 28).main()[i]
    amany = NaiveBayes(feature)
    amany.naive()
    maxx = max(amany.probability_being_a_zero(),
               amany.probability_being_a_one(),
               amany.probability_being_a_two(),
               amany.probability_being_a_three(),
               amany.probability_being_a_four(),
               amany.probability_being_a_five(),
               amany.probability_being_a_six(),
               amany.probability_being_a_seven(),
               amany.probability_being_a_eight(),
               amany.probability_being_a_nine())

    if maxx == amany.probability_being_a_zero() and labels[i] == '0\n':
        r += 1
        print('correct')
    elif maxx == amany.probability_being_a_one() and labels[i] == '1\n':
        r += 1
        print('correct')
    elif maxx == amany.probability_being_a_two() and labels[i] == '2\n':
        r += 1
        print('correct')
    elif maxx == amany.probability_being_a_three() and labels[i] == '3\n':
        r += 1
        print('correct')
    elif maxx == amany.probability_being_a_four() and labels[i] == '4\n':
        r += 1
        print('correct')
    elif maxx == amany.probability_being_a_five() and labels[i] == '5\n':
        r += 1
        print('correct')
    elif maxx == amany.probability_being_a_six() and labels[i] == '6\n':
        r += 1
        print('correct')
    elif maxx == amany.probability_being_a_seven() and labels[i] == '7\n':
        r += 1
        print('correct')
    elif maxx == amany.probability_being_a_eight() and labels[i] == '8\n':
        r += 1
        print('correct')
    elif maxx == amany.probability_being_a_nine() and labels[i] == '9\n':
        r += 1
        print('correct')
    else:
        w +=1
        print('wrong')
print(r, ' ', w)


