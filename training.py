import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import joblib

# Load the dataset for training and testing 
file_path = 'Your dataset'
data = pd.read_csv(file_path)

# Select relevant columns from the dataset
# Choose the relevant coloumns you want to use for features and label
# I will recommend using the features as they really increase the accuracy of the model
data = data[['feature_1', 'feature_2', 'feature_3', ' feature_4', 'enrolled']] # the coloumn enrolled is the target for testing your model

# Features with binary categories like "yes' and "no"
data['feature_1'] = data['feature_1'].apply(lambda x: 1 if x == 'Yes' else 0)
data['enrolled'] = data['enrolled'].apply(lambda x: 1 if x == 'Yes' else 0)

# Manually allocate numerical values to multi-categorical features
# These are dummy dictionaries and values so modify them according to the categories you have in your dataset
# you can create more dicts according to your features
feature_2_dict = {'Regular Decision': 0, 'Early Decision 2': 1, 'Early Action': 2, 'Early Decision 1': 3}
feature_3_dict = { 'Financial Aid Award': 1, 'Top Scholar': 2, 'Pending Deposit': 3,  'Admit': 4, 'Defer': 5, 'Gap Year': 6}

# Apply the dictionaries to convert categories to numerical values
data['feature_2'] = data['feature_2'].map(feature_2_dict)
data['feature_3'] = data['feature_3'].map(feature_3_dict)

# Define features and target, please modify these according to your dataset 
X = data[['feature_1', 'feature_2', 'feature_3', ' feature_4']]
y = data['enrolled']

# Create a ColumnTransformer to handle preprocessing
# put all your features for processing and imputing the data so the model doesn't encounter any null values 
preprocessor = ColumnTransformer(
    transformers=[
        ('num', SimpleImputer(strategy='mean'), ['feature_1', 'feature_2', 'feature_3', ' feature_4'])
    ]
)

# Creating a pipeline that includes the preprocessor and the model (combines the preprocessed data with the model)
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', RandomForestClassifier(n_estimators=900, random_state=42))
])

# Split the data into training and testing sets
# i will recommend spliting the data between 0.2-0.3
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
pipeline.fit(X_train, y_train)

# Evaluating the model so you can see the accuracy 
y_pred = pipeline.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Random Forest Accuracy: {accuracy:.2%}')
print(f'Random Forest Classification Report:')
print(classification_report(y_test, y_pred))

# Save the model and preprocessing artifacts
joblib.dump(pipeline, 'location where you want to save your model')
joblib.dump((feature_2_dict, feature_3_dict), 'location where you want to save your dict for future use and predictions')
# saving dicts are important to keep the feature values consistant
print("the model has been saved")
