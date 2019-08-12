import pickle
from decimal import *


class NBDigitsAccuracy:

    def load_data(self):
        with open('processed_digit_data.pkl', 'rb') as g:
            digit_data = pickle.load(g)
        with open('Processed_digit_labels.pkl', 'rb') as f:
            digit_labels = pickle.load(f)
        return digit_data, digit_labels

    def training_data_percentage(self, data, labels, percent):
        return data[:int((len(labels) * (percent / 100.0)))], labels[:int((len(labels) * (percent / 100.0)))]

    def train_labels(self, labels):
        no_of_labels = [0.0 for i in range(10)]
        for i in labels:
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

    def prior_probabilities(self, no_of_labels, labels):
        return [Decimal(no_of_labels[0]) / labels, Decimal(no_of_labels[1]) / labels, Decimal(no_of_labels[2]) / labels,
                Decimal(no_of_labels[3]) / labels, Decimal(no_of_labels[4]) / labels, Decimal(no_of_labels[5]) / labels,
                Decimal(no_of_labels[6]) / labels, Decimal(no_of_labels[7]) / labels, Decimal(no_of_labels[8]) / labels,
                Decimal(no_of_labels[9]) / labels]

    def divide_data(self, data, labels):
        divid_data = [[], [], [], [], [], [], [], [], [], []]
        for i in range(len(labels)):
            if labels[i] == '0\n':
                divid_data[0].append(data[i])
            elif labels[i] == '1\n':
                divid_data[1].append(data[i])
            elif labels[i] == '2\n':
                divid_data[2].append(data[i])
            elif labels[i] == '3\n':
                divid_data[3].append(data[i])
            elif labels[i] == '4\n':
                divid_data[4].append(data[i])
            elif labels[i] == '5\n':
                divid_data[5].append(data[i])
            elif labels[i] == '6\n':
                divid_data[6].append(data[i])
            elif labels[i] == '7\n':
                divid_data[7].append(data[i])
            elif labels[i] == '8\n':
                divid_data[8].append(data[i])
            elif labels[i] == '9\n':
                divid_data[9].append(data[i])
        return divid_data





