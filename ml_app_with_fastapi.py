import streamlit as st
import pandas as pd
from catboost import CatBoostRegressor
import requests
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# Set Page Layout
st.set_page_config(layout='wide')





st.title('Diamond Price Predictor')
st.image("""https://www.thestreet.com/.image/ar_4:3%2Cc_fill%2Ccs_srgb%2Cq_auto:good%2Cw_1200/MTY4NjUwNDYyNTYzNDExNTkx/why-dominion-diamonds-second-trip-to-the-block-may-be-different.png""")
st.header('Enter the characteristics of the diamond:')


carat = st.number_input('Carat Weight:', min_value=0.1, max_value=10.0, value=1.0)

cut = st.selectbox('Cut Rating:', ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])

color = st.selectbox('Color Rating:', ['J', 'I', 'H', 'G', 'F', 'E', 'D'])

clarity = st.selectbox('Clarity Rating:', ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'])

depth = st.number_input('Diamond Depth Percentage:', min_value=0.1, max_value=100.0, value=1.0)

table = st.number_input('Diamond Table Percentage:', min_value=0.1, max_value=100.0, value=1.0)

x = st.number_input('Diamond Length (X) in mm:', min_value=0.1, max_value=100.0, value=1.0)

y = st.number_input('Diamond Width (Y) in mm:', min_value=0.1, max_value=100.0, value=1.0)

z = st.number_input('Diamond Height (Z) in mm:', min_value=0.1, max_value=100.0, value=1.0)

inputs = {'carat':carat, 'cut':cut, 'color':color, 'clarity':clarity, 'depth':depth, 'table':table, 'x':x, 'y':y, 'z':z}

if st.button('Predict Price'):
    response = requests.post(url = "http://127.0.0.1:8000/model-predict", data = json.dumps(inputs))

    st.success(f'The predicted price of the diamond is ${response.text} USD')