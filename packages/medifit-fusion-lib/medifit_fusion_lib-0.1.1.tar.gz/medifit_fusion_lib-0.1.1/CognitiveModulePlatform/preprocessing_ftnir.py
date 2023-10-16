from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
from raw_data_smoothing_methods import BaselineCorrection, StandardNormalVariate, SavitzkyGolayFilter


class Preprocessing:

    def __init__(self, file_path, sheet_name='Sheet1'):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.n_components = 10
        self.n_components_to_keep = 5
        self.pipeline = self._create_pipeline()

    def _create_pipeline(self):
        return Pipeline([
            ('baseline_correction', BaselineCorrection()),
            ('standard_normal_variate', StandardNormalVariate()),
            ('savgol_filter', SavitzkyGolayFilter()),
            ('pca', PCA(n_components=self.n_components))
        ])

    def load_data(self):
        training_data = pd.read_excel(self.file_path, sheet_name=self.sheet_name, header=None)
        self.geographical_origin = training_data.iloc[:, 0]
        self.numerical_data = training_data.iloc[:, 1:]
        self.numerical_data.columns = self.numerical_data.columns.astype(str)
        return self.geographical_origin

    def apply_preprocessing(self):
        principal_components = self.pipeline.fit_transform(self.numerical_data)
        self.principal_components_selected = principal_components[:, :self.n_components_to_keep]
        pca = self.pipeline.named_steps['pca']
        self.explained_variance_ratio_ = pca.explained_variance_ratio_
        self.cumulative_explained_variance = np.cumsum(self.explained_variance_ratio_)

    def perform_pca(self):
        pca = PCA(n_components=self.n_components)
        principal_components = pca.fit_transform(self.numerical_data_filtered)  # Using filtered numerical data
        self.explained_variance_ratio_ = pca.explained_variance_ratio_
        self.cumulative_explained_variance = np.cumsum(self.explained_variance_ratio_)

        self.n_components_to_keep = 5
        self.principal_components_selected = principal_components[:, :self.n_components_to_keep]
        return self.principal_components_selected

    def save_pcs(self, file_path='first_5_principal_components.joblib'):
        joblib.dump(self.principal_components_selected, file_path)

    def save_pipeline(self, file_path='preprocessing_pipeline.joblib'):  # CHANGED THAT INTO .JOBLIB
        joblib.dump(self.pipeline, file_path)

    def visualize_cumulative_variance(self):
        plt.figure(figsize=(8, 6))
        plt.plot(range(1, self.n_components + 1), self.cumulative_explained_variance, marker='o', linestyle='--',
                 color='b')
        plt.xticks(range(1, self.n_components + 1))
        plt.xlabel('Number of Principal Components')
        plt.ylabel('Cumulative Explained Variance')
        plt.title('Cumulative Explained Variance by Principal Components')
        plt.grid(True)
        plt.show()

    def visualize_explained_variance(self):
        plt.figure(figsize=(8, 6))
        plt.bar(range(1, self.n_components + 1), self.explained_variance_ratio_, alpha=0.8)
        plt.xticks(range(1, self.n_components + 1))
        plt.xlabel('Principal Components')
        plt.ylabel('Explained Variance Ratio')
        plt.title('Explained Variance Ratio by Principal Components')
        plt.grid(True)
        plt.show()

    def visualize_pca_2d(self, first_index, second_index):
        label_encoder = LabelEncoder()
        labels_encoded = label_encoder.fit_transform(self.geographical_origin)

        cmap = plt.get_cmap('viridis', len(np.unique(labels_encoded)))

        plt.figure(figsize=(8, 6))
        scatter = plt.scatter(self.principal_components_selected[:, first_index],
                              self.principal_components_selected[:, second_index],
                              c=labels_encoded, cmap=cmap)
        plt.xlabel('Principal Component 1')
        plt.ylabel('Principal Component 2')

        handles, labels = scatter.legend_elements()
        legend = plt.legend(handles, label_encoder.inverse_transform(np.unique(labels_encoded)),
                            title='Geographical Origin', loc='best')
        legend.get_title().set_fontsize('12')

        plt.title('PCA - First 2 Principal Components with Baseline Correction')
        plt.show()

    def visualize_pca_3d(self, first_idx, second_idx, third_idx):
        label_encoder = LabelEncoder()
        labels_encoded = label_encoder.fit_transform(self.geographical_origin)

        cmap = plt.get_cmap('viridis', len(np.unique(labels_encoded)))

        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        scatter = ax.scatter(self.principal_components_selected[:, first_idx],
                             self.principal_components_selected[:, second_idx],
                             self.principal_components_selected[:, third_idx],
                             c=labels_encoded, cmap=cmap)
        ax.set_xlabel('Principal Component 1')
        ax.set_ylabel('Principal Component 2')
        ax.set_zlabel('Principal Component 3')
        cbar = plt.colorbar(scatter, ticks=np.unique(labels_encoded))
        cbar.set_label('Geographical Origin')
        cbar.set_ticklabels(label_encoder.inverse_transform(np.unique(labels_encoded)))
        plt.title('PCA - First 3 Principal Components with Baseline Correction')
        plt.show()


class PreprocessingExternal:

    def __init__(self, file_path, sheet_name='Sheet1', include_classes=True):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.include_classes = include_classes
        self.data = pd.read_excel(file_path)

    def load_data(self):
        training_data = pd.read_excel(self.file_path, sheet_name=self.sheet_name)

        if self.include_classes:
            self.geographical_origin = training_data.iloc[:, 0]
            self.numerical_data = training_data.iloc[:, 1:]
        else:
            self.geographical_origin = None
            self.numerical_data = training_data

        self.numerical_data.columns = self.numerical_data.columns.astype(str)
        return self.geographical_origin

    def load_pipeline(self, file_path='preprocessing_pipeline.joblib'):  # CHANGED HERE TOO
        self.pipeline = joblib.load(file_path)

    def apply_preprocessing(self):
        principal_components = self.pipeline.transform(self.numerical_data)
        self.principal_components_selected = principal_components[:, :5]  # Assuming you want to keep the first 5 PCs
        return self.principal_components_selected

    def save_pcs(self, file_path='first_5_principal_components.joblib'):
        joblib.dump(self.principal_components_selected, file_path)

    def visualize_cumulative_variance(self):
        pca = self.pipeline.named_steps['pca']
        explained_variance_ratio_ = pca.explained_variance_ratio_
        cumulative_explained_variance = np.cumsum(explained_variance_ratio_)

        plt.figure(figsize=(8, 6))
        plt.plot(range(1, len(explained_variance_ratio_) + 1), cumulative_explained_variance, marker='o',
                 linestyle='--', color='b')
        plt.xticks(range(1, len(explained_variance_ratio_) + 1))
        plt.xlabel('Number of Principal Components')
        plt.ylabel('Cumulative Explained Variance')
        plt.title('Cumulative Explained Variance by Principal Components')
        plt.grid(True)
        plt.show()

    def visualize_explained_variance(self):
        pca = self.pipeline.named_steps['pca']
        explained_variance_ratio_ = pca.explained_variance_ratio_

        plt.figure(figsize=(8, 6))
        plt.bar(range(1, len(explained_variance_ratio_) + 1), explained_variance_ratio_, alpha=0.8)
        plt.xticks(range(1, len(explained_variance_ratio_) + 1))
        plt.xlabel('Principal Components')
        plt.ylabel('Explained Variance Ratio')
        plt.title('Explained Variance Ratio by Principal Components')
        plt.grid(True)
        plt.show()

    def get_data_size(self):
        return self.data.shape
