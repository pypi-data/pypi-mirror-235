import joblib 
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class ClassifierManager:
    def __init__(self, train_path, validation_path):
        # Load the training and validation data
        self.train_data = joblib.load(train_path)
        self.validation_data = joblib.load(validation_path)

        # Separate the labels and features
        self.X_train, self.y_train = self.train_data[:, 1:], self.train_data[:, 0]
        self.X_validation, self.y_validation = self.validation_data[:, 1:], self.validation_data[:, 0]

        # Define the classifiers
        self.classifiers = {
            "MLP": MLPClassifier(
                hidden_layer_sizes=(60,40), 
                max_iter=6000,
                activation='relu', 
                solver='adam', 
                alpha=0.05, 
                learning_rate='adaptive',
                random_state=42),
            "SVM": SVC(
                kernel='rbf',
                gamma='auto', 
                C = 4.5,
                probability=True, 
                decision_function_shape='ovr', 
                break_ties=True, 
                random_state=42),
            "RandomForest": RandomForestClassifier(
                n_estimators=40, 
                criterion='gini', 
                min_samples_split=2, 
                min_samples_leaf=1, 
                random_state=42)
        }

    def train_and_evaluate(self, classifier_name, save_path=None):
        classifier = self.classifiers[classifier_name]

        # Train the classifier
        classifier.fit(self.X_train, self.y_train)

        # Evaluate the classifier
        y_pred = classifier.predict(self.X_validation)
        accuracy = accuracy_score(self.y_validation, y_pred)
        precision = precision_score(self.y_validation, y_pred, average='weighted')
        recall = recall_score(self.y_validation, y_pred, average='weighted')
        # f1 = f1_score(self.y_validation, y_pred, average='weighted')
        f1 = 2 * precision * recall / (precision + recall)
        # roc_auc = roc_auc_score(self.y_validation, classifier.predict_proba(self.X_validation), multi_class='ovr')

        print(f"Classifier: {classifier_name}")
        # print(f"Accuracy: {accuracy:.4f}")
        print(f"Precision: {precision:.4f}")
        print(f"Recall: {recall:.4f}")
        print(f"F1 Score: {f1:.4f}")
        # print(f"ROC-AUC: {roc_auc:.4f}")
        print("")
        
        # Confusion Matrix Heatmap
        cm = confusion_matrix(self.y_validation, y_pred)
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=np.unique(self.y_train), yticklabels=np.unique(self.y_train))
        plt.xlabel("Predicted Label")
        plt.ylabel("True Label")
        plt.title(f"Confusion Matrix Heatmap - {classifier_name}")
        plt.show()

        # Save the trained model if a path is provided
        if save_path:
            joblib.dump(classifier, save_path)

        return classifier

    def deployment(self, model_path, unseen_data_path, y_true=None):
        model = joblib.load(model_path)

        unseen_data = joblib.load(unseen_data_path) if isinstance(unseen_data_path, str) else unseen_data_path

        predictions = model.predict(unseen_data)

        if y_true is not None:
            cm = confusion_matrix(y_true, predictions)
            plt.figure(figsize=(8, 6))
            sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=np.unique(y_true), yticklabels=np.unique(y_true))
            plt.xlabel("Predicted Label")
            plt.ylabel("True Label")
            plt.title("Confusion Matrix Heatmap")
            plt.show()

        return predictions
    
    def grid_search(self, classifier_name, param_grid):
        classifier = self.classifiers[classifier_name]
        grid = GridSearchCV(classifier, param_grid, cv=5, scoring='f1_weighted', n_jobs=-1)
        grid.fit(self.X_train, self.y_train)
        
        print(f"Best parameters for {classifier_name}: {grid.best_params_}")
        print(f"Best cross-validation F1 score: {grid.best_score_:.4f}")
        
        return grid.best_estimator_
    