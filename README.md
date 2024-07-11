# College-student-enrollment-predictor
## by Muhammad Umer Tahir
This machine learning model is designed to assist colleges in predicting the likelihood of a student enrolling after receiving an acceptance offer. By analyzing various factors and features, the model aims to provide insights that can help institutions better understand and anticipate student enrollment behavior. I tested various machine learning algorithms including KNN, decision tree, and gradient boosting but Random forest came out to be the best model for this project.
## Table of Contents
- [Project Overview](#project-overview)
- [Files and Directories](#files-and-directories)
- [Getting Started](#getting-started)
- [Running the Model](#running-the-model)
- [Web Portal for Individual Predictions](#web-portal-for-individual-predictions)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
## Project Overview
This project includes three main Python scripts:
1. `training.py`: Used to create and train the model, and check its accuracy.
2. `predicting.py`: Used to make predictions for a whole CSV file.
3. `app.py`: A web portal to get individual predictions through a user-friendly interface.

**Note:** Due to privacy and sensitivity concerns by the admissions office at Rhodes College, the actual dataset and feature details used in the training process are not provided. Users are encouraged to use their own datasets and features.

## Files and Directories
- `training.py`: Script to train the model.
- `predicting.py`: Script to make batch predictions.
- `app.py`: Flask web application for individual predictions.
- `templates/index.html`: HTML template for the web interface.

## Getting Started
To get started with the project, follow these steps:

1. **Clone the repository:**
    ```
    git clone https://github.com/your_username/your_repository.git
    cd your_repository
    ```

2. **Install the required dependencies:**
    ```
    pip3 install "library name"
    ```

3. **Prepare your dataset:**
    Ensure your dataset is in CSV format and contains the relevant features you want to use for prediction. I have also provided the to pick     and choose specific columns from the CSV file.

## Running the Model

### Training the Model
1. **Update the `training.py` file:**
   - Replace `'location of your dataset'` with the path to your CSV file.
   - Ensure that the feature columns are correctly referenced.

2. **Run the training script:**
    ```
    python3 training.py
    ```
   This script will train the model and save it for future use. Using this code you can also test the accuracy of your model while predicting using the split function between training and testing datasets. If you have limited data, I will also recommend training the model on the whole dataset, once you're satisfied with your model.

### Making Batch Predictions using CSV file
1. **Update the `predicting.py` file:**
   - Replace `'location of your model'` and `'location of your dict'` with the paths to your saved model and dictionary files during training.
   - Replace the `'location of your new dataset'` with the path to the CSV file you want to predict.

2. **Run the predicting script:**
    ```
    python3 predicting.py
    ```

## Web Portal for Individual Predictions
1. **Update the `app.py` file:**
   - Set the environment variables `MODEL_PATH` and `DICT_PATH` to the paths of your saved model and dictionary files.

2. **Run the Flask app:**
    ```
    python3 app.py
    ```
   Open a web browser and go to `http://127.0.0.1:5000/` to access the web portal. Enter the required features to get individual predictions.

## Dependencies
The project requires the following Python libraries:
- Flask
- joblib
- numpy
- pandas
- scikit-learn

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## Further improvements
I am planning on improving the web app and make it visually appealing by using html and CSS.
Coming Soon!
