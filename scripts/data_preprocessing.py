import os
import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        data = pd.read_csv(file_path)
        if 'Autism_Prediction' not in data.columns:
            raise KeyError("'Autism_Prediction' column not found in dataset.")
        # Fill missing values
        data = data.fillna(0)
        # Separate features and target
        features = data.drop(columns=['Autism_Prediction'])
        target = data['Autism_Prediction']
        # Scale features
        scaler = StandardScaler()
        features_scaled = scaler.fit_transform(features)
        # Create a new DataFrame for processed data
        processed_data = pd.DataFrame(features_scaled, columns=features.columns)
        processed_data['Autism_Prediction'] = target
        # Save the cleaned data
        output_path = 'data/cleaned_behavioral_data.csv'
        processed_data.to_csv(output_path, index=False)
        print(f"Processed data saved to: {os.path.abspath(output_path)}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    preprocess_data('./data/behavioral_assessment.csv')
