from joblib import load, dump
import numpy as np


class Fusion1Algorithm:
    def __init__(self, training_file1, training_file2, validation_file1, validation_file2):
        self.data_training1 = load(training_file1)
        self.data_training2 = load(training_file2)
        self.data_validation1 = load(validation_file1)
        self.data_validation2 = load(validation_file2)

    def extract_labels_features(self, data):
        labels = data[:, 0]
        features = data[:, 1:6]
        return labels, features

    def combine_features(self, features1, features2):
        return np.hstack((features1, features2))

    def create_combined_data(self, labels, combined_features):
        return np.hstack((labels.reshape(-1, 1), combined_features))

    def process(self):
        labels_training1, features_training1 = self.extract_labels_features(self.data_training1)
        labels_training2, features_training2 = self.extract_labels_features(self.data_training2)
        labels_validation1, features_validation1 = self.extract_labels_features(self.data_validation1)
        labels_validation2, features_validation2 = self.extract_labels_features(self.data_validation2)

        combined_features_training = self.combine_features(features_training1, features_training2)
        combined_features_validation = self.combine_features(features_validation1, features_validation2)

        self.combined_data_training = self.create_combined_data(labels_training1, combined_features_training)
        self.combined_data_validation = self.create_combined_data(labels_validation1, combined_features_validation)

        return self.combined_data_training, self.combined_data_validation

    def save_combined_data(self, training_file, validation_file):
        dump(self.combined_data_training, training_file)
        dump(self.combined_data_validation, validation_file)


class Fusion1AlgorithmExternal:

    def __init__(self, training_data1, training_data2, from_files=True):
        if from_files:
            self.data_training1 = load(training_data1)
            self.data_training2 = load(training_data2)
        else:
            self.data_training1 = training_data1
            self.data_training2 = training_data2

    def combine_features(self, features1, features2):
        return np.hstack((features1, features2))


    def process(self):
        self.combined_features_training = self.combine_features(self.data_training1, self.data_training2)
        return self.combined_features_training

    def save_combined_data(self, training_file):
        dump(self.combined_features_training, training_file)