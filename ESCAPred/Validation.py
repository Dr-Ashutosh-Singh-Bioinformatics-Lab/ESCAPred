# ESCA/Validation.py

import os
import pandas as pd
import joblib

def predict(df, model_type='svc'):
    # List of selected genes
    selected_genes = ['DBF4', 'UTP18', 'TYMP', 'IBSP', 'HOXC8', 'TRIP13', 'TRMT6', 'BIRC5', 'HNRNPC', 'IL11', 'MMP11', 'PFDN4', 'PSMA7', 'MRGBP', 'CDC25B', 'SEC14L5', 'PDAP1', 'NUDT1', 'LIMK1', 'UBE2S', 'PPP1R9B', 'ULBP1', 'BRIX1', 'POLR1G', 'DDX39A', 'HOXC11', 'NSUN5', 'NXT1', 'RFC3', 'DHX34', 'TMEM60', 'NRM', 'PFDN2', 'SNRPG', 'MMP3', 'TDO2', 'LRP8', 'C19orf47', 'MAGOH', 'ESM1', 'MCM7', 'CXCL8', 'RSRC1', 'ERFE', 'FOXS1', 'HOXC9', 'KPNA2', 'HMCES', 'H2AC20', 'ISG15', 'SUMO2',  'CENPW', 'MZT1', 'PSMB3']

    # Select features from dataframe
    df_selected = df[selected_genes]
    
    # Construct model path
    model_path = os.path.join(os.path.dirname(__file__), 'models', f'{model_type.lower()}.pkl')
    
    # Check if model file exists
    if not os.path.exists(model_path):
        raise ValueError(f"Model '{model_type}' not found. Ensure the model file exists at {model_path}.")
    
    # Load the model
    model = joblib.load(model_path)
    
    # Make predictions
    y_pred = model.predict(df_selected)
    
    # Add predictions to dataframe
    df['Prediction'] = ['Cancer' if pred == 1 else 'Normal' for pred in y_pred]
    
    # Save predictions to CSV file
    df.to_csv('predictions.csv', index=False)
    
    # Print diagnosis
    count_cancer = y_pred.sum()
    count_normal = len(y_pred) - count_cancer
    percentage_cancer = count_cancer / len(y_pred)
    percentage_normal = count_normal / len(y_pred)
    
    if percentage_cancer > 0.6:
        print(f"ESCA patient detected, {percentage_cancer*100:.2f}%")
    else:
        print(f"Normal patient detected, {percentage_normal*100:.2f}%")

