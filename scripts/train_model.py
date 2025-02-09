from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pandas as pd
import joblib


def train_model():
    # Load the preprocessed data
    data = pd.read_csv('data/cleaned_behavioral_data.csv')
    # Split features and target
    X = data.drop(columns=['Autism_Prediction'])
    y = data['Autism_Prediction']
    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # Initialize and train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    # Evaluate the model
    print(classification_report(y_test, model.predict(X_test)))
    # Save the trained model
    joblib.dump(model, 'models/autism_behavior_model.pkl')


if __name__ == "__main__":
    train_model()
