#use this code if you want the prediction for a whole csv file
import joblib
import pandas as pd
import numpy as np

# Load the model and preprocessing artifacts
pipeline = joblib.load('location of your model')
application_round_dict, decisions_name_dict = joblib.load('loacation of your dict')

# Load the dataset
file_path = 'location of your new dataset for which you want to predict'
data = pd.read_csv(file_path)

# Select relevant columns from the dataset
data = data[['Get your features coloumns from your csv file']]

# Convert binary categorical data to binary values
data['feature'] = data['feature'].apply(lambda x: 1 if x == 'Yes' else 0)

# Apply the dictionaries to convert categories to numerical values (multi-categorical data)
# we are using the dict we created and stored while the training of the model 
data['feature_1'] = data['feature_1'].map(fetaure_1_dict)
data['feature_2'] = data['feature_2'].map(feature_2_dict)

# Check for missing values before imputing
print("Missing values in the dataset before imputing:")
print(data.isnull().sum())

# Use the model for the prediction of your file
predictions = pipeline.predict(data)

# Count the number of 0s and 1s in the predictions
# 0s means the student didn't enroll and 1 means the student enrolled 
count_0 = np.sum(predictions == 0)
count_1 = np.sum(predictions == 1)

# Print the count of predictions for each category
print(f"Number of students predicted not to enroll: {count_0}")
print(f"Number of students predicted to enroll: {count_1}")
