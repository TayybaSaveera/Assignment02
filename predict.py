import requests


# Define the URL of the Flask API endpoint
url = 'http://127.0.0.1:5000/predict'

# Define input features for prediction
input_features = {
    'sepal_length': 5.1,
    'sepal_width': 3.5,
    'petal_length': 1.4,
    'petal_width': 0.2
}

# Send a POST request to the Flask API endpoint with input features
response = requests.post(url, json={'features': input_features})

# Parse the JSON response
if response.status_code == 200:
    data = response.json()
    predicted_species = data['predicted_species']
    print(f"Predicted Species: {predicted_species}")
else:
    print("Failed to make prediction. Status code:", response.status_code)
