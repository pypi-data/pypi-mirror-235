from one_class_classification import ClassifierManager
import joblib
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix

train_path = "data_training_ad.joblib"
validation_path = "data_validation_ad.joblib"
save_path_if = "IF.joblib"
save_path_ocsvm = 'OCSVM.joblib'
save_path_lof = 'LOF.joblib'

data_train_ftir = joblib.load(train_path)
pca_train_ftir = data_train_ftir[:,1:]
y_train_ftir = data_train_ftir[:,0].reshape(-1,1)
data_validation_ftir = joblib.load(validation_path)
y_valid_ftir = data_validation_ftir[:,0]

manager = ClassifierManager(train_path, validation_path)

########################
# OC - SVM GRID SEARCH #
########################

param_grid_ocsvm = [
    {
        'kernel': ['rbf', 'sigmoid'], 
        'gamma': ['scale', 'auto', 1e-2, 2e-2, 5e-2, 1e-1, 2e-1, 3e-1, 5e-1, 7e-1, 9e-1, 1, 1.5, 2.0],
        'Nu': [0.05, 0.075, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9], 
        'decision_function_shape': ['ovr'], 
        'break_ties': [True, False], 
        'random_state': [42]
    },
    {
        'kernel': ['poly'], 
        'gamma': ['scale', 'auto', 1e-2, 2e-2, 5e-2, 1e-1, 2e-1, 3e-1, 5e-1, 7e-1, 9e-1, 1, 1.5, 2.0],
        'Nu': [0.05, 0.075, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9], 
        'degree': [1, 2, 3, 4], 
        'decision_function_shape': ['ovr'], 
        'break_ties': [True, False], 
        'random_state': [42]
    }
]

# Find best hyperparameters using grid search
best_ocsvm = manager.grid_search("SVM", param_grid_ocsvm)

# Train and evaluate the best RandomForest model
best_ocsvm.fit(manager.X_train, manager.y_train)
y_pred = best_ocsvm.predict(manager.X_validation)
f1 = f1_score(manager.y_validation, y_pred, average='weighted')
print(f"F1 Score for best SVM: {f1:.4f}")

#####################################
# LOCAL OUTLIER FACTOR GRID SEARCH  #
#####################################

param_grid_lof = {
    'n_neighbors': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20], 
    'algorithm': ['auto', 'ball tree', 'kd-tree', 'brute'], 
    'metric': ['jaccard', 'cityblock', 'euclidean', 'mahalanobis', 'minkowski', 'manhattan', 'canberra', 'hamming', 'L1', 'L2', 'yule'], 
    'novelty': [True],
}

# Find best hyperparameters using grid search
best_lof = manager.grid_search("MLP", param_grid_lof)

# Train and evaluate the best RandomForest model
best_lof.fit(manager.X_train, manager.y_train)
y_pred = best_lof.predict(manager.X_validation)
f1 = f1_score(manager.y_validation, y_pred, average='weighted')
print(f"F1 Score for best MLP: {f1:.4f}")

################################
# ISOLATION FOREST GRID SEARCH #
################################
ratio = manager.outlier_target_ratio()
param_grid_isolation_forest = {
    'n_estimators': [2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180],
    'max_samples': ['auto', 1, 2, 3, 4, 5, 6, 7, 8],
    'contamination': [ratio], 
    'min_samples_leaf': [1, 2, 3, 4],
    'random_state': [42]
}

# Find best hyperparameters using grid search
best_if = manager.grid_search("RandomForest", param_grid_isolation_forest)

# Train and evaluate the best RandomForest model
best_if.fit(manager.X_train, manager.y_train)
y_pred = best_if.predict(manager.X_validation)
f1 = f1_score(manager.y_validation, y_pred, average='weighted')
print(f"F1 Score for best RandomForest: {f1:.4f}")


manager.train_and_evaluate_anomaly("OneClassSVM", y_valid_ftir, save_path_ocsvm)
manager.train_and_evaluate_anomaly("IsolationForest", y_valid_ftir, save_path_if)
manager.train_and_evaluate_anomaly("LocalOutlierFactor", y_valid_ftir, save_path_lof)

