import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin
from raw_data_smoothing_methods import BaselineCorrection, MeanCentering, SavitzkyGolayFilter, SingularValueDecomposition, MinMaxNormalization
import joblib
import matplotlib.pyplot as plt
import numpy as np
import copy


# class SelectPrincipalComponents(BaseEstimator, TransformerMixin):
    # def __init__(self, n_components_to_keep=5):
    #     self.n_components_to_keep = n_components_to_keep

    # def fit(self, X, y=None):
    #     return self

    # def transform(self, X):
    #     return X[:, :self.n_components_to_keep]


class Preprocessing:

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
            # ('baseline_correction', BaselineCorrection()),
            # ('SG', SavitzkyGolayFilter()),
            #('SVD', SingularValueDecomposition()),
            ('normalization', MinMaxNormalization()),
            ('pca', PCA(n_components=self.n_components)),
            # ('select_pcs', SelectPrincipalComponents())
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
        # return principal_components
        return principal_components[:, :self.n_components_to_keep] # for keeping the first 5 PCs

    def save_pipeline(self, file_path='ftir_preprocessing_pipeline_geo.joblib'):   # CHANGE THE NAME ACCORDINGLY #CHANGED THE PIPELINE INTO .JOBLIB
        
        # Fit the pipeline to obtain all 10 principal components
        self.pipeline.fit(self.numerical_data)
        
        # Create a deep copy of the pipeline
        modified_pipeline = copy.deepcopy(self.pipeline)
        
        # Save only the first 5 principal components in the modified pipeline
        principal_components_to_save = modified_pipeline.named_steps['pca'].components_[:self.n_components_to_keep]
        modified_pipeline.named_steps['pca'].components_ = principal_components_to_save
        
        # Save the modified pipeline with the first 5 principal components
        joblib.dump(modified_pipeline, file_path)
    
        # joblib.dump(self.pipeline, file_path)

    def save_pcs(self, pcs, file_path='first_5_principal_components.joblib'):
        # Save the first 5 principal components using joblib
        joblib.dump(pcs, file_path)

    def split_and_save_data(self, split_row):
        """
        Split the data into training and validation sets based on the given split_row.
        Save the training and validation data to the specified paths.
        """
        # Check if principal_components already exists
        if not hasattr(self, 'principal_components'):
            self.principal_components = self.preprocess_and_perform_pca()
    
        # Split the data based on the given split_row
        training_data = self.principal_components[:split_row]
        validation_data = self.principal_components[split_row:]
    
        # Add the class labels to the training and validation data
        training_labels = self.geographical_origin.iloc[:split_row].values.reshape(-1, 1)
        validation_labels = self.geographical_origin.iloc[split_row:].values.reshape(-1, 1)
    
        training_data_with_labels = np.hstack((training_labels, training_data))
        validation_data_with_labels = np.hstack((validation_labels, validation_data))
    
        # Save the training and validation data to the specified paths
        joblib.dump(training_data_with_labels, r"D:\Desktop\Folders\MEDIFIT_More\newer\Original Data\original_processed\UV-Vis\data_training_ad.joblib")
        joblib.dump(validation_data_with_labels, r"D:\Desktop\Folders\MEDIFIT_More\newer\Original Data\original_processed\UV-Vis\data_validation_ad.joblib")

    def visualize_cumulative_variance(self):
        pca = self.pipeline.named_steps['pca']
        cumulative_explained_variance = np.cumsum(pca.explained_variance_ratio_)
        
        # Plot the cumulative explained variance for the first n_components_to_keep
        plt.figure(figsize=(8, 6))
        plt.plot(range(1, self.n_components_to_keep + 1), cumulative_explained_variance[:self.n_components_to_keep], marker='o', linestyle='--', color='b')
        plt.xticks(range(1, self.n_components_to_keep + 1))
        plt.xlabel('Number of Principal Components')
        plt.ylabel('Cumulative Explained Variance')
        plt.title('Cumulative Explained Variance by Principal Components')
        plt.grid(True)
        plt.show()

    # def visualize_cumulative_variance(self):
    #     pca = self.pipeline.named_steps['pca']
    #     cumulative_explained_variance = np.cumsum(pca.explained_variance_ratio_)
        
    #     # Plot the cumulative explained variance
    #     plt.figure(figsize=(8, 6))
    #     plt.plot(range(1, self.n_components_to_keep + 1), cumulative_explained_variance, marker='o', linestyle='--', color='b')
    #     plt.xticks(range(1, self.n_components_to_keep + 1))
    #     plt.xlabel('Number of Principal Components')
    #     plt.ylabel('Cumulative Explained Variance')
    #     plt.title('Cumulative Explained Variance by Principal Components')
    #     plt.grid(True)
    #     plt.show()

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
        cbar = plt.colorbar(scatter, ticks=np.unique(labels_encoded))
        cbar.set_label('Geographical Origin')
        cbar.set_ticklabels(label_encoder.inverse_transform(np.unique(labels_encoded)))
        plt.title('PCA - First 3 Principal Components with Baseline Correction')
        plt.show()
        
        
class ValidationPreprocessing(Preprocessing):

    def __init__(self, file_path, sheet_name='Sheet1', pipeline_path='ftir_preprocessing_pipeline_geo.joblib'): # DON'T FORGET TO CHANGE THE NAME
        super().__init__(file_path, sheet_name)
        self.geographical_origin = None  # No classes in validation data
        self.data = pd.read_excel(file_path)
        self.pipeline = joblib.load(pipeline_path)  # Load the saved pipeline

    def preprocess_data(self):
        # Apply the pipeline to preprocess the validation data
        self.numerical_data_transformed = self.pipeline.transform(self.numerical_data)
        return self.numerical_data_transformed

    def load_data(self):
        # Load the validation data from the Excel file without headers
        self.numerical_data = pd.read_excel(self.file_path, sheet_name=self.sheet_name, header=None)
        # Since there's no geographical origin column in the validation data, no need to skip the first column
  
    # Override the visualization methods that rely on classes
    def visualize_pca_2d(self):
        print("This method is not applicable for validation data without classes.")

    def visualize_pca_3d(self):
        print("This method is not applicable for validation data without classes.")
    
    def get_data_size(self):
        return self.data.shape        


# INTERNAL        
# ftir_preprocessor = Preprocessing(r"D:\Desktop\Folders\MEDIFIT_More\newer\Original Data\original_processed\UV-Vis\UV_ad.xlsx") #FTIR_geo_2.xlsx or FTIR_ad.xlsx or FTIR_bot.xlsx
# principal_components = ftir_preprocessor.preprocess_and_perform_pca()
# ftir_preprocessor.split_and_save_data(split_row=631) # 556 for geo, 566 for bot and 631 for ad 
# ftir_preprocessor.save_pipeline(file_path=r"D:\Desktop\Folders\MEDIFIT_More\newer\Original Data\original_processed\UV-Vis\uvvis_preprocessing_pipeline_ad.joblib")
# ftir_preprocessor.visualize_cumulative_variance()
# ftir_preprocessor.visualize_explained_variance()
# ftir_preprocessor.visualize_pca_2d(principal_components, 0, 1)
# ftir_preprocessor.visualize_pca_2d(principal_components, 1, 2)
# ftir_preprocessor.visualize_pca_2d(principal_components, 2, 3)
# ftir_preprocessor.visualize_pca_2d(principal_components, 3, 4)
# ftir_preprocessor.visualize_pca_3d(principal_components, 0, 1, 2)
# ftir_preprocessor.visualize_pca_3d(principal_components, 1, 2, 3)
# ftir_preprocessor.visualize_pca_3d(principal_components, 2, 3, 4)


# EXTERNAL
# validator = ValidationPreprocessing(r"D:\Desktop\Folders\MEDIFIT_More\newer\Original Data\original_processed\FTIR_ATR\example_ftir.xlsx")
# validator.load_data()
# preprocessed_validation_data = validator.preprocess_data()
# validator.visualize_cumulative_variance()
# validator.visualize_explained_variance()
# validator.save_pcs('first_5_principal_components_validation.joblib')
