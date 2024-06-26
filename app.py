from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')


@app.route('/predict', methods=['POST'])
def predict():
    # Get input features from request
    data = request.json
    # Directly use data if it's already in the correct format
    features_array = data

    # Make prediction
    prediction = model.predict([features_array])[0]

    # Map prediction to class label
    species_mapping = {
        0: 'setosa',
        1: 'versicolor',
        2: 'virginica'
    }
    predicted_species = species_mapping[prediction]

    # Return prediction as JSON response
    return jsonify({'predicted_species': predicted_species})


if __name__ == '__main__':
    app.run(debug=True)
