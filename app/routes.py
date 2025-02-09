from flask import request, render_template
import joblib
import pandas as pd
import numpy as np
import os
from app import app  # Ensure you're reusing the `app` from __init__.py, not creating a new one

# Ensure the model file exists
model_path = 'models/autism_behavior_model.pkl'
assert os.path.exists(model_path), "Model file not found at 'models/autism_behavior_model.pkl'"

# Load the trained model
model = joblib.load(model_path)


# Render the form
@app.route('/')
def index():
    return render_template('index.html')


# Handle prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect data from form submission
        form_data = request.form

        # Required fields for prediction
        feature_keys = [
            'Sucks_Finger', 'Coordinates_Swallowing', 'Food_Stimulus',
            'Eyes_Follow', 'Watches_Hand', 'Raises_Head', 'Fist_Clench',
            'Puts_Mouth', 'Grasps_Object', 'Mashed_Food', 'Holds_Bottle',
            'Swallows_Closed', 'Crawls', 'Bounces', 'Claps',
            'Plays_Tiny_Objects', 'Reaches_Object', 'Bangs_Object'
        ]

        # Get features
        features_dict = {}
        for key in feature_keys:
            if key not in form_data:
                raise ValueError(f"Missing feature: {key}")
            features_dict[key] = [int(form_data[key])]  # Ensure integer conversion

        features = pd.DataFrame.from_dict(features_dict)

        # Debug: Log dataframe for review
        print("[DEBUG] Prediction Input DataFrame:\n", features)

        # Predict using the loaded model
        if model:
            prediction = model.predict(features)[0]
        else:
            raise ValueError("Model not loaded.")

        # Result mapping
        if prediction == 0:
            risk_result = "Low Risk"
        elif prediction == 1:
            risk_result = "High Risk"
        else:
            raise ValueError(f"Unexpected prediction output: {prediction}")

        return render_template('result.html', result=risk_result)

    except ValueError as ve:
        print(f"[ERROR] Value Error during prediction: {ve}")
        return render_template('result.html', result="Error processing input: Invalid form submission.")
    except Exception as e:
        print(f"[ERROR] Unexpected error during prediction: {e}")
        return render_template('result.html', result="Error processing input. Please try again.")
