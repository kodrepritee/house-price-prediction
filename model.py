import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib


# For simplicity, we create a dummy model.
# In practice, load a dataset and train a model.
def load_model():
    # Load the trained model and location encoder
    model = joblib.load('models/trained_model.pkl')
    location_encoder = joblib.load('models/location_encoder.pkl')
    return model, location_encoder


model, location_encoder = load_model()


def predict_price(bedrooms, bathrooms, sqft, location):
    # Transform location string to encoded value
    location_encoded = location_encoder.transform([location])[0]
    # Create feature array with encoded location
    features = np.array([[bedrooms, bathrooms, sqft, location_encoded]])
    prediction = model.predict(features)
    return round(prediction[0], 2)
