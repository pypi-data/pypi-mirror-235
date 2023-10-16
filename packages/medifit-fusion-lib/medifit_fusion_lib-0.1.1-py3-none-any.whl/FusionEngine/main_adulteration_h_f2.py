import os
import pandas as pd
from preprocessing_ftir import ValidationPreprocessing
from preprocessing_raman import ValidationPreprocessingRaman
from preprocessing_ftnir import PreprocessingExternal
from fusion_2_creation import Fusion2AlgorithmExternal
from joblib import load
import numpy as np
from tabulate import tabulate

# F1 scores from the training phase
f1_score_ftir = 0.905
f1_score_ftnir = 0.856
f1_score_raman = 0.889

def load_full_excel(file_path):
    data = pd.read_excel(file_path, header=None)
    return data

def process_excel_file(excel_file_ftir, excel_file_ftnir, excel_file_raman, output_folder_path=None):
    if 'ftir' not in excel_file_ftir.lower():
        raise ValueError(
            f"Invalid file type for FTIR processing: {excel_file_ftir}. The file must contain the sensor's name (FTIR)")

    if 'ftnir' not in excel_file_ftnir.lower():
        raise ValueError(
            f"Invalid file type for FTNIR processing: {excel_file_ftnir}. The file must contain the sensor's name  (FTNIR)")

    if 'raman' not in excel_file_raman.lower():
        raise ValueError(
            f"Invalid file type for Raman processing: {excel_file_raman}. The file must contain the sensor's name  (Raman)")

    ftir_preprocessor = ValidationPreprocessing(excel_file_ftir,
                                                pipeline_path="ftmir_preprocessing_pipeline_geo.joblib")
    ftnir_preprocessor = PreprocessingExternal(excel_file_ftnir, include_classes=False)
    raman_preprocessor = ValidationPreprocessingRaman(excel_file_raman,
                                                      raman_pipeline_path='raman_preprocessing_pipeline_geo.joblib')

    # Load the entire Excel files
    full_ftir_data = load_full_excel(excel_file_ftir)
    full_ftnir_data = load_full_excel(excel_file_ftnir)
    full_raman_data = load_full_excel(excel_file_raman)

    ftir_preprocessor.numerical_data = full_ftir_data.iloc[:, :]
    ftnir_preprocessor.numerical_data = full_ftnir_data
    raman_preprocessor.numerical_data = full_raman_data.iloc[:, :]

    rows_ftir = ftir_preprocessor.numerical_data.shape[0]
    rows_ftnir = ftnir_preprocessor.numerical_data.shape[0]
    rows_raman = raman_preprocessor.numerical_data.shape[0]

    if rows_ftir != rows_ftnir:
        raise ValueError(
            f"Number of rows in both Excel files are not the same. FTIR: {rows_ftir}, FTNIR: {rows_ftnir}.")

    ftir_pcs = ftir_preprocessor.preprocess_data()

    ftnir_pipeline_path = "ftnir_preprocessing_pipeline_ad.joblib"
    ftnir_preprocessor.load_pipeline(ftnir_pipeline_path)
    ftnir_pcs = ftnir_preprocessor.apply_preprocessing()

    raman_pcs = raman_preprocessor.preprocess_data()
    return ftir_pcs, ftnir_pcs, raman_pcs


# Here we take the excel files and implement the preprocessing

excel_file_ftir = "example_ftir_geo.xlsx"  # Example file path for FTIR
excel_file_ftnir = "example_ftnir_geo.xlsx"  # Example file path for FTNIR
excel_file_raman = "example_raman_geo.xlsx"  # Example file path for Raman

full_ftir_data = load_full_excel(excel_file_ftir)
full_ftnir_data = load_full_excel(excel_file_ftnir)
full_raman_data = load_full_excel(excel_file_raman)

print("Full FTIR Data Size: ", full_ftir_data.shape)
print("Full FTNIR Data Size: ", full_ftnir_data.shape)
print("Full Raman Data Size: ", full_raman_data.shape)


def bayesian_fusion(predictions, f1_scores):
    total_f1 = sum(f1_scores)
    normalized_f1 = [score / total_f1 for score in f1_scores]
    fused_predictions = sum(pred * weight for pred, weight in zip(predictions, normalized_f1))
    return fused_predictions


try:
    ftir_pcs, ftnir_pcs, raman_pcs = process_excel_file(excel_file_ftir, excel_file_ftnir, excel_file_raman)
except ValueError as e:
    print(e)

# Load the classifiers
clf_ftir = load("RF.joblib")
clf_ftnir = load("MLP.joblib")
clf_raman = load("MLP.joblib")

# Get predictions from each sensor's model
predictions_ftir = clf_ftir.predict(ftir_pcs)
predictions_ftnir = clf_ftnir.predict(ftnir_pcs)
predictions_raman = clf_raman.predict(raman_pcs)

# Perform Bayesian fusion
fused_predictions = bayesian_fusion([predictions_ftir, predictions_ftnir, predictions_raman], 
                                    [f1_score_ftir, f1_score_ftnir, f1_score_raman])

# Display the results
table_data = []
for i, pred in enumerate(fused_predictions):
    likelihood = "High" if pred > 0.7 else "Medium" if pred > 0.5 else "Low"
    table_data.append([f"Sample {i+1}", pred, likelihood])

headers = ["Sample", "Fused Prediction", "Likelihood of Being Correct"]
print(tabulate(table_data, headers=headers, tablefmt="grid"))