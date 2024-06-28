# College-student-enrollment-predictor
This machine learning model is designed to assist colleges in predicting the likelihood of a student enrolling after receiving an acceptance offer. By analyzing various factors and features, the model aims to provide insights that can help institutions better understand and anticipate student enrollment behavior.
## Table of Contents
- [Project Overview](#project-overview)
- [Files and Directories](#files-and-directories)
- [Getting Started](#getting-started)
- [Running the Model](#running-the-model)
- [Web Portal for Individual Predictions](#web-portal-for-individual-predictions)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)
## Project Overview
This project includes three main Python scripts:
1. `training.py`: Used to create and train the model, and check its accuracy.
2. `predicting.py`: Used to make predictions for a whole CSV file.
3. `app.py`: A web portal to get individual predictions through a user-friendly interface.

**Note:** Due to privacy and sensitivity concerns, the actual dataset and feature details used in the training process are not provided. Users are encouraged to use their own datasets and features.

## Files and Directories
- `training.py`: Script to train the model.
- `predicting.py`: Script to make batch predictions.
- `app.py`: Flask web application for individual predictions.
- `templates/index.html`: HTML template for the web interface.

## Getting Started
To get started with the project, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your_username/your_repository.git
    cd your_repository
    ```

2. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Prepare your dataset:**
    Ensure your dataset is in CSV format and contains the relevant features you want to use for prediction.

## Running the Model

### Training the Model
1. **Update the `training.py` file:**
   - Replace `'location of your dataset'` with the path to your CSV file.
   - Ensure that the feature columns are correctly referenced.

2. **Run the training script:**
    ```bash
    python training.py
    ```
   This script will train the model and save it for future use.

### Making Batch Predictions
1. **Update the `predicting.py` file:**
   - Replace `'location of your model'` and `'location of your dict'` with the paths to your saved model and dictionary files.
   - Replace `'location of your new dataset'` with the path to the CSV file you want to predict.

2. **Run the predicting script:**
    ```bash
    python predicting.py
    ```

## Web Portal for Individual Predictions
1. **Update the `app.py` file:**
   - Set the environment variables `MODEL_PATH` and `DICT_PATH` to the paths of your saved model and dictionary files.

2. **Run the Flask app:**
    ```bash
    export FLASK_APP=app.py
    flask run
    ```
   Open a web browser and go to `http://127.0.0.1:5000/` to access the web portal. Enter the required features to get individual predictions.

## Dependencies
The project requires the following Python libraries:
- Flask
- joblib
- numpy
- pandas
- scikit-learn
