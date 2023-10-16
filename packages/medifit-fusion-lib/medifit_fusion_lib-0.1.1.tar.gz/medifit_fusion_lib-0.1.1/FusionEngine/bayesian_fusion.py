from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import joblib

class BayesianFusion:
    def __init__(self, model_paths, sensor_data_paths):
        self.models = [joblib.load(path) for path in model_paths]
        self.sensor_data = [joblib.load(path) for path in sensor_data_paths]

    def predict_proba(self):
        proba_list = []
        for model, data in zip(self.models, self.sensor_data):
            X = data[:, 1:]
            proba = model.predict_proba(X)
            proba_list.append(proba)
        return proba_list

    def bayesian_fusion(self, proba_list):
        # Initialize with the first sensor's probabilities
        fused_proba = proba_list[0]
        
        # Update probabilities based on additional sensors
        for proba in proba_list[1:]:
            fused_proba *= proba  # Bayes' theorem update step
            
        # Normalize the probabilities so they sum to 1
        fused_proba /= np.sum(fused_proba, axis=1, keepdims=True)
        
        # Get the class with the maximum probability
        fused_predictions = np.argmax(fused_proba, axis=1)
        
        return fused_predictions

    def evaluate(self, true_labels, fused_predictions):
        f1 = f1_score(true_labels, fused_predictions, average='weighted')
        precision = precision_score(true_labels, fused_predictions, average='weighted')
        recall = recall_score(true_labels, fused_predictions, average='weighted')
        accuracy = accuracy_score(true_labels, fused_predictions)
        
        print(f"F1 Score: {f1:.4f}")
        print(f"Precision: {precision:.4f}")
        print(f"Recall: {recall:.4f}")
        print(f"Accuracy: {accuracy:.4f}")

        cm = confusion_matrix(true_labels, fused_predictions)
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
        plt.xlabel("Predicted Label")
        plt.ylabel("True Label")
        plt.title("Confusion Matrix Heatmap - Bayesian Fusion")
        plt.show()

# Paths to the trained models and sensor data
model_paths = ["model_sensor1.joblib", "model_sensor2.joblib", "model_sensor3.joblib"]
sensor_data_paths = ["data_sensor1.joblib", "data_sensor2.joblib", "data_sensor3.joblib"]

# Initialize the BayesianFusion class
fusion = BayesianFusion(model_paths, sensor_data_paths)

# Get predicted probabilities from each model
proba_list = fusion.predict_proba()

# Perform Bayesian fusion on the probabilities
fused_predictions = fusion.bayesian_fusion(proba_list)

# Assume the true labels are the same for all sensors (you can change this)
true_labels = fusion.sensor_data[0][:, 0]

# Evaluate the fused predictions
fusion.evaluate(true_labels, fused_predictions)
