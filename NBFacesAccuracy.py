from ProcessFaceData import ProcessFaceData
from Labels import Labels
from NaiveBayesFaces import NaiveBayesFaces
import pickle
from decimal import *


def load_data():
    with open('processed_face_data.pkl', 'rb') as g:
        face_data = pickle.load(g)
    with open('Processed_face_labels.pkl', 'rb') as f:
        face_labels = pickle.load(f)
    return face_data, face_labels


def training_data_percentage(data, labels, percent):
    return data[:int((len(labels) * (percent / 100.0)))], labels[:int((len(labels) * (percent / 100.0)))]


def train_labels(labels):
    no_of_labels = [0.0, 0.0]
    for i in labels:
        if i == '0\n':
            no_of_labels[0] += 1.0
        if i == '1\n':
            no_of_labels[1] += 1.0
    return no_of_labels


def prior_probabilities(no_of_labels, labels):
    return list([Decimal(no_of_labels[0]) / labels, Decimal(no_of_labels[1]) / labels])


def divide_data(data, labels):
    divid_data = [[], []]
    for i in range(len(labels)):
        if labels[i] == '0\n':
            divid_data[0].append(data[i])
        else:
            divid_data[1].append(data[i])
    return divid_data

face_data,  face_labels = load_data()

test_labels = Labels('Data/facedata/facedatatestlabels.txt').get_labels()
test_features = ProcessFaceData('Data/facedata/facedatatest.txt', 70).main()

percent =10
while percent <= 100:
    r = 0
    w = 0
    new_face_data, new_face_labels = training_data_percentage(face_data, face_labels, percent)
    no_of_labels = train_labels(new_face_labels)
    length = Decimal(len(new_face_labels))
    prior_probabilitiess = prior_probabilities(no_of_labels, length)
    divide_dataa = divide_data(new_face_data, new_face_labels)

    for i in range(len(test_features)):
        feature = test_features[i]
        maxx = NaiveBayesFaces(feature, new_face_data, new_face_labels, no_of_labels, prior_probabilitiess, divide_dataa).naive()
        if maxx == "face" and test_labels[i] == '1\n':
            r += 1
        elif maxx == "not_face" and test_labels[i] == '0\n':
            r += 1
        else:
             w += 1
    print('percentage of training data is ' + str(percent) + "%")
    print('accuracy is ' + str((r/len(test_features)) * 100) + "%\n")
    percent += 10

