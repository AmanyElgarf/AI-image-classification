from NBFacesAccuracy import FacesMetrics
from ProcessFaceData import ProcessFaceData
from Labels import Labels
from NaiveBayesFaces import NaiveBayesFaces
from decimal import *
import random
from NBDigitsAccuracy import NBDigitsAccuracy
from NaiveBayesDigit import NaiveBayesDigit


class Interactive:
    def __init__(self):
        self.t_face_data, self.t_face_labels = FacesMetrics().load_data()
        self.test_face_labels = Labels('Data/facedata/facedatatestlabels.txt').get_labels()
        self.test_face_features = ProcessFaceData('Data/facedata/facedatatest.txt', 70).main()
        self.t_digits_data, self.t_digits_labels = NBDigitsAccuracy().load_data()
        self.test_digits_labels = Labels('Data/digitdata/testlabels.txt').get_labels()
        self.test_digits_features = ProcessFaceData('Data/digitdata/testimages.txt', 28).main()

    def allFacesAccuracy(self, percent):
        r = 0
        w = 0
        new_face_data, new_face_labels = FacesMetrics().training_data_percentage(self.t_face_data, self.t_face_labels, percent)
        no_of_labels = FacesMetrics().train_labels(new_face_labels)
        length = Decimal(len(new_face_labels))
        prior_probabilitiess = FacesMetrics().prior_probabilities(no_of_labels, length)
        divide_dataa = FacesMetrics().divide_data(new_face_data, new_face_labels)

        for i in range(len(self.test_face_features)):
            feature = self.test_face_features[i]
            maxx = NaiveBayesFaces(feature, new_face_data, new_face_labels, no_of_labels, prior_probabilitiess,
                                       divide_dataa).naive()
            if maxx == "face" and self.test_face_labels[i] == '1\n':
                r += 1
            elif maxx == "not_face" and self.test_face_labels[i] == '0\n':
                r += 1
            else:
                w += 1
        print('percentage of training data is ' + str(percent) + "%")
        print('accuracy is ' + str((r / len(self.test_face_features)) * 100) + "%\n")

    def oneFace(self, percent):
        new_face_data, new_face_labels = FacesMetrics().training_data_percentage(self.t_face_data, self.t_face_labels, percent)
        no_of_labels = FacesMetrics().train_labels(new_face_labels)
        length = Decimal(len(new_face_labels))
        prior_probabilitiess = FacesMetrics().prior_probabilities(no_of_labels, length)
        divide_dataa = FacesMetrics().divide_data(new_face_data, new_face_labels)

        i = random.randint(0, len(self.test_face_features))
        feature = self.test_face_features[i]
        maxx = NaiveBayesFaces(feature, new_face_data, new_face_labels, no_of_labels, prior_probabilitiess,
                                       divide_dataa).naive()
        if maxx == "face" and self.test_face_labels[i] == '1\n':
            print("label is " + self.test_face_labels[i] +
                  "prediction: image is a face\n" +
                  "The image number in the test data set is ", i+1)
            print("prediction is correct\n")
        elif maxx == "not_face" and self.test_face_labels[i] == '0\n':
            print("label is " + self.test_face_labels[i] +
                  "prediction: image is not a face\n" +
                  "The image number in the test data set is ", i+1)
            print("prediction is correct\n")
        else:
            if maxx == "face" and self.test_face_labels[i] == '0\n':
                print("label is " + self.test_face_labels[i] +
                      "prediction: image is a face\n" +
                      "The image number in the test data set is ", i+1)
                print("prediction is false\n")
            elif maxx == "not_face" and self.test_face_labels[i] == '1\n':
                print("label is " + self.test_face_labels[i] +
                      "prediction: image is a not a face\n" +
                      "The image number in the test data set is ", i+1)
                print("prediction is false\n")

    def allDigitsAccuracy(self, percent):
        r = 0
        w = 0
        new_digit_data, new_digit_labels = NBDigitsAccuracy().training_data_percentage(self.t_digits_data, self.t_digits_labels,
                                                                                       percent)
        no_of_labels = NBDigitsAccuracy().train_labels(new_digit_labels)
        length = Decimal(len(new_digit_labels))
        prior_probabilitiess = NBDigitsAccuracy().prior_probabilities(no_of_labels, length)
        divide_dataa = NBDigitsAccuracy().divide_data(new_digit_data, new_digit_labels)
        for i in range(len(self.test_digits_features)):
            feature = self.test_digits_features[i]
            maxx = NaiveBayesDigit(feature, new_digit_data, new_digit_labels, no_of_labels, prior_probabilitiess,
                                   divide_dataa).naive()
            if maxx == "zero" and self.test_digits_labels[i] == '0\n':
                r += 1
            elif maxx == "one" and self.test_digits_labels[i] == '1\n':
                r += 1
            elif maxx == "two" and self.test_digits_labels[i] == '2\n':
                r += 1
            elif maxx == "three" and self.test_digits_labels[i] == '3\n':
                r += 1
            elif maxx == "four" and self.test_digits_labels[i] == '4\n':
                r += 1
            elif maxx == "five" and self.test_digits_labels[i] == '5\n':
                r += 1
            elif maxx == "six" and self.test_digits_labels[i] == '6\n':
                r += 1
            elif maxx == "seven" and self.test_digits_labels[i] == '7\n':
                r += 1
            elif maxx == "eight" and self.test_digits_labels[i] == '8\n':
                r += 1
            elif maxx == "nine" and self.test_digits_labels[i] == '9\n':
                r += 1
            else:
                w += 1
        print('percentage of training data is ' + str(percent) + "%")
        print('accuracy is ' + str((r / len(self.test_digits_features)) * 100) + "%\n")

    def oneDigit(self, percent):
        new_digit_data, new_digit_labels = NBDigitsAccuracy().training_data_percentage(self.t_digits_data,
                                                                                       self.t_digits_labels,
                                                                                       percent)
        no_of_labels = NBDigitsAccuracy().train_labels(new_digit_labels)
        length = Decimal(len(new_digit_labels))
        prior_probabilitiess = NBDigitsAccuracy().prior_probabilities(no_of_labels, length)
        divide_dataa = NBDigitsAccuracy().divide_data(new_digit_data, new_digit_labels)
        i = random.randint(0, len(self.test_digits_features))
        feature = self.test_digits_features[i]
        maxx = NaiveBayesDigit(feature, new_digit_data, new_digit_labels, no_of_labels, prior_probabilitiess,
                               divide_dataa).naive()
        if maxx == "zero" and self.test_digits_labels[i] == '0\n':
            print("label is " + self.test_digits_labels[i] +
                  "prediction: image is zero\n" +
                  "The image number in the test data set is ", i+1)
            print("prediction is correct\n")
        elif maxx == "one" and self.test_digits_labels[i] == '1\n':
            print("label is " + self.test_digits_labels[i] +
                  "prediction: image is one\n" +
                  "The image number in the test data set is ", i+1)
            print("prediction is correct\n")
        elif maxx == "two" and self.test_digits_labels[i] == '2\n':
            print("label is " + self.test_digits_labels[i] +
                  "prediction: image is two\n" +
                  "The image number in the test data set is ", i+1)
            print("prediction is correct\n")
        elif maxx == "three" and self.test_digits_labels[i] == '3\n':
            print("label is " + self.test_digits_labels[i] +
                  "prediction: image is three\n" +
                  "The image number in the test data set is ", i+1)
            print("prediction is correct\n")
        elif maxx == "four" and self.test_digits_labels[i] == '4\n':
            print("label is " + self.test_digits_labels[i] +
                  "prediction: image is four\n" +
                  "The image number in the test data set is ", i+1)
            print("prediction is correct\n")
        elif maxx == "five" and self.test_digits_labels[i] == '5\n':
            print("label is " + self.test_digits_labels[i] +
                  "prediction: image is five\n" +
                  "The image number in the test data set is ", i+1)
            print("prediction is correct\n")
        elif maxx == "six" and self.test_digits_labels[i] == '6\n':
            print("label is " + self.test_digits_labels[i] +
                  "prediction: image is six\n" +
                  "The image number in the test data set is ", i+1)
            print("prediction is correct\n")
        elif maxx == "seven" and self.test_digits_labels[i] == '7\n':
            print("label is " + self.test_digits_labels[i] +
                  "prediction: image is seven\n" +
                  "The image number in the test data set is ", i+1)
            print("prediction is correct\n")
        elif maxx == "eight" and self.test_digits_labels[i] == '8\n':
            print("label is " + self.test_digits_labels[i] +
                  "prediction: image is eight\n" +
                  "The image number in the test data set is ", i+1)
            print("prediction is correct\n")
        elif maxx == "nine" and self.test_digits_labels[i] == '9\n':
            print("label is " + self.test_digits_labels[i] +
                  "prediction: image is nine\n" +
                  "The image number in the test data set is ", i+1)
            print("prediction is correct\n")
        else:
            if maxx == "zero":
                print("label is " + self.test_digits_labels[i] +
                      "prediction: image is a zero\n" +
                      "The image number in the test data set is ", i+1)
                print("prediction is false\n")
            elif maxx == "one":
                print("label is " + self.test_digits_labels[i] +
                      "prediction: image is a one\n" +
                      "The image number in the test data set is ", i+1)
                print("prediction is false\n")
            elif maxx == "two":
                print("label is " + self.test_digits_labels[i] +
                      "prediction: image is a two\n" +
                      "The image number in the test data set is ", i+1)
                print("prediction is false\n")
            elif maxx == "three":
                print("label is " + self.test_digits_labels[i] +
                      "prediction: image is a three\n" +
                      "The image number in the test data set is ", i+1)
                print("prediction is false\n")
            elif maxx == "four":
                print("label is " + self.test_digits_labels[i] +
                      "prediction: image is a four\n" +
                      "The image number in the test data set is ", i+1)
                print("prediction is false\n")
            elif maxx == "five":
                print("label is " + self.test_digits_labels[i] +
                      "prediction: image is a five\n" +
                      "The image number in the test data set is ", i+1)
                print("prediction is false\n")
            elif maxx == "six":
                print("label is " + self.test_digits_labels[i] +
                      "prediction: image is a six\n" +
                      "The image number in the test data set is ", i+1)
                print("prediction is false\n")
            elif maxx == "seven":
                print("label is " + self.test_digits_labels[i] +
                      "prediction: image is a seven\n" +
                      "The image number in the test data set is ", i+1)
                print("prediction is false\n")
            elif maxx == "eight":
                print("label is " + self.test_digits_labels[i] +
                      "prediction: image is an eight\n" +
                      "The image number in the test data set is ", i+1)
                print("prediction is false\n")
            elif maxx == "nine":
                print("label is " + self.test_digits_labels[i] +
                      "prediction: image is a nine\n" +
                      "The image number in the test data set is ", i+1)
                print("prediction is false\n")

    def run(self):
        user_input = None
        while user_input != "q":
            print("Enter a percentage\n"
                  "q: Quit\n")
            user_input = input()

            if user_input != "q":
                percent = user_input
                print("1: Test a random face\n"
                      "2: Test a random digit\n"
                      "3: Test all faces\n"
                      "4: Test all digits\n")
                user_input2 = input()
                if user_input2 == "3":
                    self.allFacesAccuracy(int(percent))
                elif user_input2 == "1":
                    self.oneFace(int(percent))
                elif user_input2 == "2":
                    self.oneDigit(int(percent))
                elif user_input2 == "4":
                    self.allDigitsAccuracy(int(percent))


Interactive().run()
