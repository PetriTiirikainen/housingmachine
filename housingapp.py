import streamlit as st
import pickle
import pandas as pd
import matplotlib as plt

st.title("Housing Prices Prediction")

# Display the image
st.image("for_sale.jpg")

st.write("""
### Project description
We have trained several models to predict the price of a house based on features such as the area of the house and the condition and quality. This is the best performing model. Please fill in the form below to get the estimated price of your house.
""")

model = pickle.load(open('model.pkl', 'rb'))

# Define a function to get user input and slider
def get_input(name, min_value=0, max_value=500000, step=1):
    value = st.number_input(name, step=step)
    value_slider = st.slider(name + " (Slider)", min_value=min_value, max_value=max_value, step=step)
    if value_slider != 0:
        value = value_slider
    return value

# Get user input
GrLivArea = get_input("Above Ground Living Area size in square feet")
FullBath = get_input("Number of Full Bathrooms", max_value=10)
YearBuilt = get_input("Year Built (YYYY)", min_value=1500, max_value=2024)
YearRemodAdd = get_input("Remodel Year (YYYY)", min_value=1500, max_value=2024)
GarageCars = get_input("Number of Car spaces in Garage", max_value=20)
GarageArea = get_input("Garage Area in square feet")
TotRmsAbvGrd = get_input("Total Rooms Above Ground (excluding bathrooms)", max_value=50)
FirstFlrSF = get_input("First Floor size in square feet")
SecondFlrSF = get_input("Second Floor size in square feet")
BsmtFinSF1 = get_input("Finished Basement size in square feet")
TotalBsmtSF = get_input("Total Basement size in square feet")
BsmtUnfSF = get_input("Unfinished Basement size in square feet")
ScreenPorch = get_input("Screen Porch size in square feet")
WoodDeckSF = get_input("Wood Deck size in square feet")
OpenPorchSF = get_input("Open Porch size in square feet")
LotArea = get_input("Lot Area in square feet")
OverallCond = get_input("Overall Condition (scale from 1 to 10)", max_value=10)
OverallQual = get_input("Overall Quality (scale from 1 to 10)", max_value=10)

# Create a DataFrame from the user input
new_house = pd.DataFrame({
    'ScreenPorch': [ScreenPorch],
    'OverallCond': [OverallCond],
    'WoodDeckSF': [WoodDeckSF],
    'BsmtUnfSF': [BsmtUnfSF],
    'FullBath': [FullBath],
    'OpenPorchSF': [OpenPorchSF],
    'TotRmsAbvGrd': [TotRmsAbvGrd],
    'YearRemodAdd': [YearRemodAdd],
    'GarageCars': [GarageCars],
    'YearBuilt': [YearBuilt],
    'GarageArea': [GarageArea],
    'LotArea': [LotArea],
    '1stFlrSF': [FirstFlrSF],
    'BsmtFinSF1': [BsmtFinSF1],
    '2ndFlrSF': [SecondFlrSF],
    'TotalBsmtSF': [TotalBsmtSF],
    'GrLivArea': [GrLivArea],
    'OverallQual': [OverallQual]
})

# Predict the house price
prediction = model.predict(new_house)

# Create a DataFrame for the chart
chart_data = pd.DataFrame({
    'Price': [prediction[0]]
})

# Predict the house price
prediction = model.predict(new_house)

# Create a DataFrame for the chart
chart_data = pd.DataFrame({
    'Price': [prediction[0]]
})

# Display the bar chart in the sidebar
st.sidebar.bar_chart(chart_data)

# Display the price in the sidebar in a larger format
st.sidebar.markdown(f"<h1 style='text-align: center; color: #6A9955;'>The price of the house is: {prediction[0]}</h1>", unsafe_allow_html=True)