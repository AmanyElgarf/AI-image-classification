from decimal import *


class NaiveBayesFaces:
    def __init__(self, feature, face_data, face_labels, no_of_labels, prior_probabilities, divide_data):
        self.face_data = face_data
        self.labels = face_labels
        self.feature = feature
        self.no_of_labels = no_of_labels
        self.prior_probabilities = prior_probabilities
        self.divide_data = divide_data

    def __feature_given_face(self, feature_frequency):
        return Decimal(feature_frequency)/Decimal(self.no_of_labels[1])

    def __feature_given_not_face(self, feature_frequency):
        return Decimal(feature_frequency)/Decimal(self.no_of_labels[0])

    def probability_being_a_face(self):
        p = Decimal(self.prior_probabilities[1])
        for i in range(len(self.feature)):
            feature_frequency = 0
            for k in range(len(self.divide_data[1])):
                if self.divide_data[1][k][i] == self.feature[i]:
                    feature_frequency += 1
            if feature_frequency == 0:
                feature_frequency += Decimal(60)
            p = Decimal(p * self.__feature_given_face(feature_frequency))
        return p

    def probability_not_being_a_face(self):
        p = Decimal(self.prior_probabilities[0])
        for i in range(len(self.feature)):
            feature_frequency = 0
            for k in range(len(self.divide_data[0])):
                if self.divide_data[0][k][i] == self.feature[i]:
                    feature_frequency += 1
            if feature_frequency == 0:
                feature_frequency+= Decimal(60)
            p = Decimal(p * self.__feature_given_not_face(feature_frequency))
        return p

    def naive(self):
        face = self.probability_being_a_face()
        not_face = self.probability_not_being_a_face()
        maxx = max(face, not_face)
        if maxx == face:
            return "face"
        else:
            return "not_face"







