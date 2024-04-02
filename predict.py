# This assumes your Flask app's `/predict` route correctly unpacks the features from the request and uses them for prediction.

import requests

# Define the URL of the Flask API endpoint
url = 'http://127.0.0.1:5000/predict'

# Define input features for prediction
input_features = [5.1, 3.5, 1.4, 0.2]  # Assuming your API expects a list of feature values

# Send a POST request to the Flask API endpoint with input features
response = requests.post(url, json=input_features)

# Parse the JSON response
if response.status_code == 200:
    data = response.json()
    predicted_species = data['predicted_species']
    print(f"Predicted Species: {predicted_species}")
else:
    print(f"Failed to make prediction. Status code: {response.status_code}")
