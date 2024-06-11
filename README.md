# Salary Prediction Model

This project predicts employee salaries using machine learning models based on various features like designation, age, unit, and ratings. It includes a FastAPI application to serve the model predictions and a web interface for user input.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Models Used](#models-used)
- [Evaluation Metrics](#evaluation-metrics)
- [API Endpoints](#api-endpoints)
- [Web Interface](#web-interface)
- [Contributing](#contributing)

## Installation

1. Clone the repository:
   ```sh 
   git clone https://github.com/VatsAmanJha/Salary-Prediction-Model.git
   ```
2. Navigate to the project directory and set up a virtual environment:
   ```sh
   cd salary-prediction-model
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Running the Jupyter Notebook

Open the Jupyter notebook and execute the cells in sequence:
   ```sh
   jupyter notebook salary.ipynb
   ```

### Running the FastAPI Application

1. Save the FastAPI code to a file named `main.py`.
2. Run the FastAPI application:
   ```sh
   uvicorn main:app --reload
   ```
3. The API will be available at `http://127.0.0.1:8000`.

### Running the Web Interface

1. Save the provided HTML code to a file named `client.html`.
2. Open `client.html` in your web browser.
3. Fill in the form and click "Predict Salary" to get the predicted salary.

## Project Structure

- `salary.ipynb`: Main notebook with data loading, EDA, model training, and prediction.
- `main.py`: FastAPI application for serving the salary prediction model.
- `client.html`: HTML file for the web interface.
- `requirements.txt`: List of required Python packages.
- `model.pkl`: Pickle file containing the trained model.

## Dataset

The dataset includes features such as:
- `FIRST NAME`: First name  
- `LAST NAME`: Last name  
- `SEX`: Gender  
- `DOJ`: Date of joining the company 
- `CURRENT DATE`: Current date of data 
- `DESIGNATION`: Job role/designation  
- `AGE`: Age  
- `SALARY`: Target variable, the salary of the data professional 
- `UNIT`: Business unit or department  
- `LEAVES USED`: Number of leaves used  
- `LEAVES REMAINING`: Number of leaves remaining  
- `RATINGS`: Ratings or performance ratings  
- `PAST EXP`: Past work experience

## Models Used

- Linear Regression
- Ridge, Lasso, ElasticNet Regression
- Decision Tree, Random Forest, Gradient Boosting, Extra Trees Regressors

## Evaluation Metrics

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R-squared (R²)

## API Endpoints

### `POST /predict`

Predicts the salary based on the input features.

**Request:**

```json
{
    "SEX": "F",
    "DESIGNATION": "Senior Analyst",
    "AGE": 27,
    "UNIT": "Marketing",
    "LEAVES_REMAINING": 14,
    "PAST_EXP": 3,
    "YEAR_OF_EXPERIENCE": 2,
    "RATINGS": 4
}
```

**Response:**

```json
{
    "SALARY": 69643
}
```

## Web Interface

The web interface allows users to input their details and get the predicted salary. 

### HTML Interface

1. Save the provided HTML code to a file named `client.html`.
2. Open `client.html` in your web browser.
3. Fill in the form and click "Predict Salary" to get the predicted salary.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.


