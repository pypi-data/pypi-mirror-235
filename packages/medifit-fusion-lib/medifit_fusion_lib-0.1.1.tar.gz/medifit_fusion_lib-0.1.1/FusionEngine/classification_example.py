import joblib
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
from multiclass_classification import ClassifierManager 
    
# Paths
train_path = "combined_data_training_geo.joblib"
validation_path = "combined_data_validation_geo.joblib"
save_path_MLP = "MLP.joblib"
save_path_RF = "RF.joblib"
save_path_SVM = "SVM.joblib"

# Load and sort data
data_train_ftir = joblib.load(train_path)
pca_train_ftir = data_train_ftir[:,1:]
y_train_ftir = data_train_ftir[:,0].reshape(-1,1)

# Initialize manager
manager = ClassifierManager(train_path, validation_path)

#############################
# RANDOM FOREST GRID SEARCH #
#############################

param_grid_rf = {
    'n_estimators': [2, 3, 4, 5, 10, 20, 30, 40, 50, 80, 100, 120, 150, 200],
    'criterion': ['gini', 'entropy', 'log_loss'],
    'min_samples_split': [2, 3, 4, 5, 6, 7], 
    'min_samples_leaf': [1, 2, 3, 4],
    'random_state': [42]
}

# Find best hyperparameters using grid search
best_rf = manager.grid_search("RandomForest", param_grid_rf)

# Train and evaluate the best RandomForest model
best_rf.fit(manager.X_train, manager.y_train)
y_pred = best_rf.predict(manager.X_validation)
f1 = f1_score(manager.y_validation, y_pred, average='weighted')
print(f"F1 Score for best RandomForest: {f1:.4f}")

######################################
# SUPPORT VECTOR MACHINE GRID SEARCH #
######################################

param_grid_svm = [
    {
        'kernel': ['rbf', 'sigmoid'], 
        'gamma': ['scale', 'auto', 0.01, 0.05, 0.1, 0.5, 1], 
        'C': [.5, 1, 2, 4, 5, 10, 15, 20],
        'probability': [True], 
        'decision_function_shape': ['ovr'], 
        'break_ties': [True, False], 
        'random_state': [42]
    },
    {
        'kernel': ['poly'], 
        'gamma': ['scale', 'auto', 0.01, 0.05, 0.1, 0.5, 1], 
        'C': [.5, 1, 2, 4, 5, 10, 15, 20],
        'degree': [1, 2, 3, 4], 
        'probability': [True], 
        'decision_function_shape': ['ovr'], 
        'break_ties': [True, False], 
        'random_state': [42]
    }
]

# Find best hyperparameters using grid search
best_svm = manager.grid_search("SVM", param_grid_svm)

# Train and evaluate the best RandomForest model
best_svm.fit(manager.X_train, manager.y_train)
y_pred = best_svm.predict(manager.X_validation)
f1 = f1_score(manager.y_validation, y_pred, average='weighted')
print(f"F1 Score for best SVM: {f1:.4f}")

#####################################
# MULTILAYER PERCEPTRON GRID SEARCH #
#####################################

param_grid_mlp = {
    'hidden_layer_sizes': [(30, 30), (70, 70), (40, 60), (50, 50), (60, 60), (70, 70), (60, 40), (100, 100), (90, 120), (120,90), (70, 100), (100,70)], 
    'max_iter': [1000, 1500, 2000, 4000, 5000, 6000, 8000], 
    'activation': ['relu', 'tanh', 'logistic'], 
    'solver': ['adam', 'sgd'], 
    'alpha': [1e-4, 3e-4, 6e-4, 9e-4, 1e-3, 2e-3, 3e-3, 6e-3, 9e-3, 1e-2, 3e-2, 5e-2, 1e-1], 
    'learning_rate': ['constant', 'adaptive'],
    'random_state': [42]
}

# Find best hyperparameters using grid search
best_mlp = manager.grid_search("MLP", param_grid_mlp)

# Train and evaluate the best RandomForest model
best_mlp.fit(manager.X_train, manager.y_train)
y_pred = best_mlp.predict(manager.X_validation)
f1 = f1_score(manager.y_validation, y_pred, average='weighted')
print(f"F1 Score for best MLP: {f1:.4f}")

# Training and evaluating the MLP
manager.train_and_evaluate("MLP", save_path_MLP)
manager.train_and_evaluate("SVM", save_path_SVM)
manager.train_and_evaluate("RandomForest", save_path_RF)
