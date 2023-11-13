import streamlit as st
import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
# Load the pre-trained model
model = joblib.load('linear_regression_model.pkl')

def run_prediction_page():
    st.title("Prediction Page")
    st.write("You can make predictions on this page.")

     # Upload a CSV file
    uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

    # Initialize data as None
    data = None

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)

    # User input sidebar
    st.sidebar.header('User Input')
    year = st.sidebar.number_input('Year', min_value=2023, max_value=2030, step=1)
    season = st.sidebar.selectbox('Season', ('PostMonsoon', 'Rainy', 'Summer', 'Winter'))
    products = st.sidebar.selectbox('Products', ('T-shirt', 'Jeans', 'Dress', 'Jacket', 'Shorts', 'Shirt', 'Tops', 'Leggings'))

   

    # Position the "Predict" button below the sidebar
    predict_button = st.sidebar.button("Predict")

    # Make predictions
    if predict_button:
        season_encoded = [0, 0, 0, 0]
        if season == 'PostMonsoon':
            season_encoded[0] = 1
        elif season == 'Rainy':
            season_encoded[1] = 1
        elif season == 'Summer':
            season_encoded[2] = 1
        elif season == 'Winter':
            season_encoded[3] = 1

        products_encoded = [0, 0, 0, 0, 0, 0, 0, 0]
        if products == 'T-shirt':
            products_encoded[0] = 1
        elif products == 'Jeans':
            products_encoded[1] = 1
        elif products == 'Dress':
            products_encoded[2] = 1
        elif products == 'Jacket':
            products_encoded[3] = 1
        elif products == 'Shorts':
            products_encoded[4] = 1
        elif products == 'Shirt':
            products_encoded[5] = 1
        elif products == 'Tops':
            products_encoded[6] = 1
        elif products == 'Leggings':
            products_encoded[7] = 1

        prediction = model.predict([[year] + season_encoded + products_encoded])

        st.subheader('Prediction')
        st.write(f'Predicted Sales Percentage: {prediction[0]:.2f}')