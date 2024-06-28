import os
from flask import Flask, request, render_template
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the model and preprocessing artifacts
pipeline = joblib.load(os.getenv('MODEL_PATH'))
application_round_dict, decisions_name_dict = joblib.load(os.getenv('DICT_PATH'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    feature_1 = request.form['feature_1']
    feature_2 = request.form['feature_2']
    feature_3 = request.form['feature_3']

    # Convert inputs from the form to numerical values
    feature_1 = feature_1_dict.get(feature_1, -1)
    feature_2 = feature_2_dict.get(feature_2, -1)
    feature_3 = 1 if feature_3 == 'Yes' else 0

    # Prepare the feature array as a DataFrame with the correct column names
    features = pd.DataFrame(
        [[feature_1, feature_2, feature_3]],
        columns=['Your columns for the features']
    )

    # Make a prediction using our model
    prediction = pipeline.predict(features)

    # Display the result
    result = 'Enroll' if prediction[0] == 1 else 'Not Enroll'
    return render_template('index.html', prediction_text=f'Student will: {result}')

if __name__ == "__main__":
    app.run(debug=True)
