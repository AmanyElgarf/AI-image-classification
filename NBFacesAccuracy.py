import pickle
from decimal import *


class FacesMetrics:

    def load_data(self):
        with open('processed_face_data.pkl', 'rb') as g:
            face_data = pickle.load(g)
        with open('Processed_face_labels.pkl', 'rb') as f:
            face_labels = pickle.load(f)
        return face_data, face_labels

    def training_data_percentage(self, data, labels, percent):
        return data[:int((len(labels) * (percent / 100.0)))], labels[:int((len(labels) * (percent / 100.0)))]

    def train_labels(self, labels):
        no_of_labels = [0.0, 0.0]
        for i in labels:
            if i == '0\n':
                no_of_labels[0] += 1.0
            if i == '1\n':
                no_of_labels[1] += 1.0
        return no_of_labels

    def prior_probabilities(self, no_of_labels, labels):
        return list([Decimal(no_of_labels[0]) / labels, Decimal(no_of_labels[1]) / labels])

    def divide_data(self, data, labels):
        divid_data = [[], []]
        for i in range(len(labels)):
            if labels[i] == '0\n':
                divid_data[0].append(data[i])
            else:
                divid_data[1].append(data[i])
        return divid_data
