import joblib
import numpy as np

# Load the trained model
model = joblib.load('app/models/trained_model.pkl')

def predict_yield(features):
    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)
    return prediction[0]
