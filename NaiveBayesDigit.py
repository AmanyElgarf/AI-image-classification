from decimal import *


class NaiveBayesDigit:
    def __init__(self, feature, digit_data, digit_labels, no_of_labels, prior_probabilities, divide_data):
        self.digit_data = digit_data
        self.labels = digit_labels
        self.feature = feature
        self.no_of_labels = no_of_labels
        self.__probability_of_zero = prior_probabilities[0]
        self.__probability_of_one = prior_probabilities[1]
        self.__probability_of_two = prior_probabilities[2]
        self.__probability_of_three = prior_probabilities[3]
        self.__probability_of_four = prior_probabilities[4]
        self.__probability_of_five = prior_probabilities[5]
        self.__probability_of_six = prior_probabilities[6]
        self.__probability_of_seven = prior_probabilities[7]
        self.__probability_of_eight = prior_probabilities[8]
        self.__probability_of_nine = prior_probabilities[9]
        self.divide_data = divide_data

    def __feature_given_zero(self, feature_frequency):
        return Decimal(feature_frequency)/Decimal(self.no_of_labels[0])

    def __feature_given_one(self, feature_frequency):
        return Decimal(feature_frequency)/Decimal(self.no_of_labels[1])

    def __feature_given_two(self, feature_frequency):
        return Decimal(feature_frequency)/Decimal(self.no_of_labels[2])

    def __feature_given_three(self, feature_frequency):
        return Decimal(feature_frequency)/Decimal(self.no_of_labels[3])

    def __feature_given_four(self, feature_frequency):
        return Decimal(feature_frequency)/Decimal(self.no_of_labels[4])

    def __feature_given_five(self, feature_frequency):
        return Decimal(feature_frequency)/Decimal(self.no_of_labels[5])

    def __feature_given_six(self, feature_frequency):
        return Decimal(feature_frequency)/Decimal(self.no_of_labels[6])

    def __feature_given_seven(self, feature_frequency):
        return Decimal(feature_frequency) / Decimal(self.no_of_labels[7])

    def __feature_given_eight(self, feature_frequency):
        return Decimal(feature_frequency) / Decimal(self.no_of_labels[8])

    def __feature_given_nine(self, feature_frequency):
        return Decimal(feature_frequency) / Decimal(self.no_of_labels[9])

    def probability_being_a_zero(self):
        p = self.__probability_of_zero
        for i in range(len(self.feature)):
            feature_frequency = 0
            for k in range(len(self.divide_data[0])):
                if self.divide_data[0][k][i] == self.feature[i]:
                    feature_frequency += 1
            if feature_frequency == 0:
                feature_frequency += 60
            p = Decimal(p * self.__feature_given_zero(feature_frequency))
        return p

    def probability_being_a_one(self):
        p = self.__probability_of_one
        for i in range(len(self.feature)):
            feature_frequency = 0
            for k in range(len(self.divide_data[1])):
                if self.divide_data[1][k][i] == self.feature[i]:
                    feature_frequency += 1
            if feature_frequency == 0:
                feature_frequency += 60
            p = Decimal(p * self.__feature_given_one(feature_frequency))
        return p

    def probability_being_a_two(self):
        p = self.__probability_of_two
        for i in range(len(self.feature)):
            feature_frequency = 0
            for k in range(len(self.divide_data[2])):
                if self.divide_data[2][k][i] == self.feature[i]:
                    feature_frequency += 1
            if feature_frequency == 0:
                feature_frequency += 60
            p = Decimal(p * self.__feature_given_two(feature_frequency))
        return p

    def probability_being_a_three(self):
        p = self.__probability_of_three
        for i in range(len(self.feature)):
            feature_frequency = 0
            for k in range(len(self.divide_data[3])):
                if self.divide_data[3][k][i] == self.feature[i]:
                    feature_frequency += 1
            if feature_frequency == 0:
                feature_frequency += 60
            p = Decimal(p * self.__feature_given_three(feature_frequency))
        return p

    def probability_being_a_four(self):
        p = self.__probability_of_four
        for i in range(len(self.feature)):
            feature_frequency = 0
            for k in range(len(self.divide_data[4])):
                if self.divide_data[4][k][i] == self.feature[i]:
                    feature_frequency += 1
            if feature_frequency == 0:
                feature_frequency += 60
            p = Decimal(p * self.__feature_given_four(feature_frequency))
        return p

    def probability_being_a_five(self):
        p = self.__probability_of_five
        for i in range(len(self.feature)):
            feature_frequency = 0
            for k in range(len(self.divide_data[5])):
                if self.divide_data[5][k][i] == self.feature[i]:
                    feature_frequency += 1
            if feature_frequency == 0:
                feature_frequency += 60
            p = Decimal(p * self.__feature_given_five(feature_frequency))
        return p

    def probability_being_a_six(self):
        p = self.__probability_of_six
        for i in range(len(self.feature)):
            feature_frequency = 0
            for k in range(len(self.divide_data[6])):
                if self.divide_data[6][k][i] == self.feature[i]:
                    feature_frequency += 1
            if feature_frequency == 0:
                feature_frequency += 60
            p = Decimal(p * self.__feature_given_six(feature_frequency))
        return p

    def probability_being_a_seven(self):
        p = self.__probability_of_seven
        for i in range(len(self.feature)):
            feature_frequency = 0
            for k in range(len(self.divide_data[7])):
                if self.divide_data[7][k][i] == self.feature[i]:
                    feature_frequency += 1
            if feature_frequency == 0:
                feature_frequency += 60
            p = Decimal(p * self.__feature_given_seven(feature_frequency))
        return p

    def probability_being_a_eight(self):
        p = self.__probability_of_eight
        for i in range(len(self.feature)):
            feature_frequency = 0
            for k in range(len(self.divide_data[8])):
                if self.divide_data[8][k][i] == self.feature[i]:
                    feature_frequency += 1
            if feature_frequency == 0:
                feature_frequency += 60
            p = Decimal(p * self.__feature_given_eight(feature_frequency))
        return p

    def probability_being_a_nine(self):
        p = self.__probability_of_nine
        for i in range(len(self.feature)):
            feature_frequency = 0
            for k in range(len(self.divide_data[9])):
                if self.divide_data[9][k][i] == self.feature[i]:
                    feature_frequency += 1
            if feature_frequency == 0:
                feature_frequency += 60
            p = Decimal(p * self.__feature_given_nine(feature_frequency))
        return p

    def naive(self):
        zero = self.probability_being_a_zero()
        one = self.probability_being_a_one()
        two = self.probability_being_a_two()
        three = self.probability_being_a_three()
        four = self.probability_being_a_four()
        five = self.probability_being_a_five()
        six = self.probability_being_a_six()
        seven = self.probability_being_a_seven()
        eight = self.probability_being_a_eight()
        nine = self.probability_being_a_nine()
        maxx = max(zero, one, two, three, four, five, six, seven, eight, nine)
        if maxx == zero:
            return "zero"
        elif maxx == one:
            return "one"
        elif maxx == two:
            return "two"
        elif maxx == three:
            return "three"
        elif maxx == four:
            return "four"
        elif maxx == five:
            return "five"
        elif maxx == six:
            return "six"
        elif maxx == seven:
            return "seven"
        elif maxx == eight:
            return "eight"
        else:
            return "nine"







