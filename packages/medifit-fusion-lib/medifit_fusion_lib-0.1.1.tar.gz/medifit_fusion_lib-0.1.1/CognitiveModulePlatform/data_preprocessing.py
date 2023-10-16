import os
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score
from raw_data_smoothing_methods import BaselineCorrection, MeanCentering, SavitzkyGolayFilter, SingularValueDecomposition, MinMaxNormalization
import joblib
import matplotlib.pyplot as plt
import numpy as np
import copy
from matplotlib.lines import Line2D  # Import Line2D for custom legend


class TrainingPreprocessing:

    def __init__(self, file_path, sheet_name='Sheet1'):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.n_components = 10  # Number of principal components for PCA
        self.n_components_to_keep = 5
        self.pipeline = self._create_pipeline()
        self.x_train = None
        self.y_train = None
        self.y_train_array = None
        self.pca_train = None
    
    def _create_pipeline(self):
        pipeline = Pipeline([
            ('baseline_correction', BaselineCorrection()),
            ('SG', SavitzkyGolayFilter()),
            ('SVD', SingularValueDecomposition()),
            ('normalization', MinMaxNormalization()),
            ('pca', PCA(n_components=self.n_components)),
        ])
        return pipeline    
    
    def load_data(self):
        # Load the data from the Excel file into a pandas DataFrame without headers
        training_data = pd.read_excel(self.file_path, sheet_name=self.sheet_name, header=None)
        self.geographical_origin = training_data.iloc[:, 0]
        self.numerical_data = training_data.iloc[:, 1:]
        return self.numerical_data
     
    def preprocess_and_perform_pca(self):
        data = self.load_data()
        principal_components = self.pipeline.fit_transform(data)
        self.pca_train = principal_components[:, :self.n_components_to_keep]  # Update this line
        print(f"Debug: self.pca_train shape: {self.pca_train.shape}")
        return self.pca_train 

    def save_pipeline(self, file_path='ftir_preprocessing_pipeline_geo.joblib'):   # CHANGE THE NAME ACCORDINGLY #CHANGED THE PIPELINE INTO .JOBLIB

        self.pipeline.fit(self.numerical_data)

        modified_pipeline = copy.deepcopy(self.pipeline)

        principal_components_to_save = modified_pipeline.named_steps['pca'].components_[:self.n_components_to_keep]
        modified_pipeline.named_steps['pca'].components_ = principal_components_to_save
        
        joblib.dump(modified_pipeline, file_path)
    
       
    def calculate_clustering_metrics(self):
        """
        Calculate clustering metrics like silhouette score, Davies-Bouldin index,
        and Calinski-Harabasz index.
        """
        # Make sure the transformed data is available
        if self.pca_train is None:
            print("Please run preprocess_and_perform_pca() first.")
            return

        # Make sure the labels are available
        if self.geographical_origin is None:
            print("Geographical origin labels are not available.")
            return

        # Calculate the metrics
        silhouette = silhouette_score(self.pca_train, self.geographical_origin)
        davies_bouldin = davies_bouldin_score(self.pca_train, self.geographical_origin)
        calinski_harabasz = calinski_harabasz_score(self.pca_train, self.geographical_origin)

        print(f"Silhouette Score: {silhouette}")
        print(f"Davies-Bouldin Index: {davies_bouldin}")
        print(f"Calinski-Harabasz Index: {calinski_harabasz}")

        return silhouette, davies_bouldin, calinski_harabasz

    def save_pcs(self, pcs, file_path='first_5_principal_components.joblib'):
        
        joblib.dump(pcs, file_path)

    def split_and_save_data(self, split_row, training_path=None, validation_path=None ):
        """
        Split the data into training and validation sets based on the given split_row.
        Save the training and validation data to the specified paths.
        """
        if training_path is None:
            training_path = os.path.dirname(self.file_path) + "/data_training.joblib"
            
        if validation_path is None:
            validation_path = os.path.dirname(self.file_path) + "/data_validation.joblib"
        
        if not hasattr(self, 'principal_components'):
            self.principal_components = self.preprocess_and_perform_pca()
    
        training_data = self.principal_components[:split_row]
        validation_data = self.principal_components[split_row:]
    
        training_labels = self.geographical_origin.iloc[:split_row].values.reshape(-1, 1)
        validation_labels = self.geographical_origin.iloc[split_row:].values.reshape(-1, 1)
    
        training_data_with_labels = np.hstack((training_labels, training_data))
        validation_data_with_labels = np.hstack((validation_labels, validation_data))
    
        joblib.dump(training_data_with_labels, training_path)
        joblib.dump(validation_data_with_labels, validation_path)

    def visualize_cumulative_variance(self):
        pca = self.pipeline.named_steps['pca']
        cumulative_explained_variance = np.cumsum(pca.explained_variance_ratio_)
        
        # Plot the cumulative explained variance for the first n_components_to_keep
        plt.figure(figsize=(8, 6))
        plt.plot(range(1, self.n_components + 1), cumulative_explained_variance[:self.n_components], marker='o', linestyle='--', color='b')
        plt.xticks(range(1, self.n_components + 1))
        plt.xlabel('Number of Principal Components')
        plt.ylabel('Cumulative Explained Variance')
        plt.title('Cumulative Explained Variance by Principal Components')
        plt.grid(True)
        plt.show()

    def visualize_explained_variance(self):
        pca = self.pipeline.named_steps['pca']
        
        # Plot the explained variance per principal component
        plt.figure(figsize=(8, 6))
        plt.bar(range(1, self.n_components + 1), pca.explained_variance_ratio_, alpha=0.8)
        plt.xticks(range(1, self.n_components + 1))
        plt.xlabel('Principal Components')
        plt.ylabel('Explained Variance Ratio')
        plt.title('Explained Variance Ratio by Principal Components')
        plt.grid(True)
        plt.show()
    
    def visualize_pca_2d(self, principal_components, first_index, second_index):
        # Encode the geographical origin labels to numerical values for color mapping
        label_encoder = LabelEncoder()
        labels_encoded = label_encoder.fit_transform(self.geographical_origin)
    
        # Create a color map for the classes
        cmap = plt.get_cmap('viridis', len(np.unique(labels_encoded)))
    
        # Visualize the data points in 2D (first 2 PCs)
        plt.figure(figsize=(8, 6))
        scatter = plt.scatter(principal_components[:, first_index], principal_components[:, second_index], c=labels_encoded, cmap=cmap)
        plt.xlabel('Principal Component 1')
        plt.ylabel('Principal Component 2')
    
        # Create a legend
        handles, labels = scatter.legend_elements()
        legend = plt.legend(handles, label_encoder.inverse_transform(np.unique(labels_encoded)), title='Adulteration', loc='best')
        legend.get_title().set_fontsize('12')
    
        plt.title('PCA - First 2 Principal Components with Baseline Correction')
        plt.show()

    def visualize_pca_3d(self, principal_components, first_index, second_index, third_index):
        # Encode the geographical origin labels to numerical values for color mapping
        label_encoder = LabelEncoder()
        labels_encoded = label_encoder.fit_transform(self.geographical_origin)
    
        # Create a color map for the classes
        cmap = plt.get_cmap('viridis', len(np.unique(labels_encoded)))
    
        # Visualize the data points in 3D (first 3 PCs)
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        scatter = ax.scatter(principal_components[:, first_index], principal_components[:, second_index], principal_components[:, third_index], c=labels_encoded, cmap=cmap)
        ax.set_xlabel('Principal Component 1')
        ax.set_ylabel('Principal Component 2')
        ax.set_zlabel('Principal Component 3')
    
        # Create a color bar
        cbar = plt.colorbar(scatter, ticks=np.unique(labels_encoded))
        cbar.set_label('Geographical Origin')
        cbar.set_ticklabels(label_encoder.inverse_transform(np.unique(labels_encoded)))
    
        # Create a custom legend
        unique_labels = np.unique(self.geographical_origin)
        legend_elements = [Line2D([0], [0], marker='o', color='w', label=label_encoder.inverse_transform([i])[0],
                                  markersize=10, markerfacecolor=cmap(i)) for i in np.unique(labels_encoded)]
        
        ax.legend(handles=legend_elements, title='Geographical Origin')
    
        plt.title('PCA - First 3 Principal Components with Baseline Correction')
        plt.show()
        
        
class ValidationPreprocessing(TrainingPreprocessing):

    def __init__(self, file_path, sheet_name='Sheet1', pipeline_path=None):
        super().__init__(file_path, sheet_name)
        if pipeline_path is None:
            pipeline_path = os.path.dirname(pipeline_path) + 'preprocessing_pipeline.joblib'
        self.geographical_origin = None  # No classes in validation data
        self.data = pd.read_excel(file_path)
        self.pipeline = joblib.load(pipeline_path)  # Load the saved pipeline

    def preprocess_data(self):
        self.numerical_data_transformed = self.pipeline.transform(self.numerical_data)
        return self.numerical_data_transformed

    def load_data(self):
        self.numerical_data = pd.read_excel(self.file_path, sheet_name=self.sheet_name, header=None)
  
    # Override the visualization methods that rely on classes
    def visualize_pca_2d(self):
        print("This method is not applicable for validation data without classes.")

    def visualize_pca_3d(self):
        print("This method is not applicable for validation data without classes.")
    
    def get_data_size(self):
        return self.data.shape        

