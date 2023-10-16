import joblib 
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC, OneClassSVM
from sklearn.ensemble import RandomForestClassifier, IsolationForest
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
from sklearn.neighbors import LocalOutlierFactor
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
        
        self.train_outliers = self.train_data[self.train_data[:, 0] == -1]
        self.train_targets = self.train_data[self.train_data[:, 0] == 1]
    
        self.validation_outliers = self.validation_data[self.validation_data[:, 0] == -1]
        self.validation_targets = self.validation_data[self.validation_data[:, 0] == 1]

        # Define the classifiers
        self.classifiers = {
            "OneClassSVM": OneClassSVM(
                kernel='poly',
                degree=3,
                gamma=0.01, #'auto' 
                nu=.44, 
                shrinking=True, 
                verbose=False
                ),
            "IsolationForest": IsolationForest(
                n_estimators=160, 
                max_samples=5, 
                contamination=.35, 
                random_state=42
                ),
            "LocalOutlierFactor": LocalOutlierFactor(
                n_neighbors=3, 
                contamination=0.38, 
                algorithm='auto', 
                metric='cityblock', 
                novelty=True
                )
        }


    def train_and_evaluate_anomaly(self, classifier_name, y_true=None, save_path=None):
        classifier = self.classifiers[classifier_name]
        
        # Train the classifier
        if classifier_name in ["OneClassSVM", "IsolationForest", "LocalOutlierFactor"]:
            classifier.fit(self.X_train)
        elif classifier_name == "SelfOrganizingMap":
            # Placeholder SOM training here
            pass
        else:
            raise ValueError(f"Unknown classifier: {classifier_name}")
        
        # Evaluate the classifier
        if y_true is not None and classifier_name not in ["SelfOrganizingMap"]:
            y_true_binary = np.where(y_true == 'ad', -1, 1) # Convert the labels to -1 and 1
        
            if classifier_name in ["OneClassSVM", "IsolationForest", "LocalOutlierFactor"]:
                # Predict on the validation data
                predictions = classifier.predict(self.X_validation)
            else:
                # Handle evaluation for other classifiers
                pass
        
            # Compute metrics
            accuracy = accuracy_score(y_true_binary, predictions)
            precision = precision_score(y_true_binary, predictions, pos_label=-1)  # For anomaly label
            recall = recall_score(y_true_binary, predictions, pos_label=-1)  # For anomaly label
            f1 = 2 * precision * recall / (precision + recall)
            
            # Print metrics
            print(f"Anomaly Detector: {classifier_name}")
            print(f"Precision: {precision:.4f}")
            print(f"Recall: {recall:.4f}")
            print(f"F1 Score: {f1:.4f}")
            print("")
        
            # Confusion Matrix Heatmap
            cm = confusion_matrix(y_true_binary, predictions)
            plt.figure(figsize=(8, 6))
            sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=np.unique(y_true_binary), yticklabels=np.unique(y_true_binary))
            plt.xlabel("Predicted Label")
            plt.ylabel("True Label")
            plt.title(f"Confusion Matrix Heatmap - {classifier_name}")
            plt.show()
            
            # Save the trained model if a path is provided
            if save_path:
                joblib.dump(classifier, save_path)
        
        return classifier
  
    def deploy_som(self, som_path, unseen_data, y_true=None):
        som = joblib.load(som_path)
    
        som_predictions = [som.winner(x) for x in unseen_data]
    
        if y_true is not None:
            y_true_binary = np.where(y_true == 'ad', -1, 1)
            
            som_predictions_labels = np.array([1 if som.winner(x) == (0, 0) else -1 for x in unseen_data])
            
            accuracy = accuracy_score(y_true_binary, som_predictions_labels)
            print(f"SOM Accuracy: {accuracy:.4f}")
    
        return som_predictions

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
    
    def outlier_target_ratio(self):
        '''Computes the outlier/target ratio, that is used as an input to
        the contamination in Local Outlier Factor and Isolation Forest.'''
        
        num_outliers = len(self.train_outliers)
        num_targets = len(self.train_targets)
        
        if num_targets == 0:  # To avoid division by zero
            return float('inf')
        
        return num_outliers / num_targets
    
