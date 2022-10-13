from fastapi import FastAPI
from typing import Optional
import pandas as pd
import json
from data_request_model import *
from catboost import CatBoostRegressor
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

app = FastAPI()


model = CatBoostRegressor()
model.load_model('diamond_catboost', format='cbm')

def predict(carat, cut, color, clarity, depth, table, x, y, z):
    prediction = model.predict(pd.DataFrame([[carat, cut, color, clarity, depth, table, x, y, z]], columns=['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'x', 'y', 'z']))
    return prediction


@app.post("/model-predict")
async def ml_predict(parameters: MlRequest):
      return  predict(parameters.carat, parameters.cut, parameters.color, parameters.clarity, parameters.depth, parameters.table, parameters.x, parameters.y, parameters.z)[0]