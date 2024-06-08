from fastapi import FastAPI
import pickle
import pandas as pd
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

with open("model.pkl", "rb") as file:
    model = pickle.load(file)


class PredictRequest(BaseModel):
    SEX: str
    DESIGNATION: str
    AGE: int
    UNIT: str
    LEAVES_REMAINING: int
    PAST_EXP: int
    YEAR_OF_EXPERIENCE: int
    RATINGS: int


class PredictResponse(BaseModel):
    SALARY: int


def preprocess_user_input(user_input):
    user_df = pd.DataFrame([user_input.dict()])
    user_df.rename(columns={
    'LEAVES_REMAINING': 'LEAVES REMAINING',
    'PAST_EXP': 'PAST EXP',
    'YEAR_OF_EXPERIENCE': 'YEAR OF EXPERIENCE',
    }, inplace=True)
    return user_df


def predict_salary(user_input):
    user_processed = preprocess_user_input(user_input)
    predicted_salary = model.predict(user_processed)

    return predicted_salary


app = FastAPI(title="Salary Prediction")



origins = [
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/predict", response_model=PredictResponse)
async def predict(request: PredictRequest):
    salary = int(predict_salary(request)[0])
    return PredictResponse(SALARY=salary)
