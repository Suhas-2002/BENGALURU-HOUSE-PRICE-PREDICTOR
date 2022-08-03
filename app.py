import streamlit as st
import pandas as pd
import numpy as np

data = pd.read_csv("Processed Bengaluru Housing Data.csv")
X = data.drop(['price (in lakhs)'],axis='columns')
Y = data['price (in lakhs)']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=0.2,random_state=10)

from sklearn.linear_model import LinearRegression
lr = LinearRegression(normalize = True)
lr.fit(x_train,y_train)

st.write("""# Bengaluru House Price Predictor
This app predicts the **Bengaluru House Price**!""")

st.write('<div style="text-align: right;"> ~Suhas Prabhu </div>', unsafe_allow_html=True)
st.write('---')


Location = st.selectbox('Select the Location :', data.columns[4:])
st.write('You selected:', Location)

Area = st.number_input('Enter Area (in sqft) :', min_value=450, step=1) 
bhk = st.number_input('Enter BHK : ', min_value=1, step=1) 
bath = st.number_input('Enter number of bathrooms : ', min_value=1, step=1) 

def check_input():
    if (not Area): 
        st.warning("Please enter the Area")
        return False
    elif(not bhk): 
        st.warning("Please enter the value of bhk")
        return False
    elif(not bath): 
        st.warning("Please enter number of bathrooms")
        return False
    
    if (Area < 450):
        st.warning("Minimum value of Area is 450 sqft!")
        return False
    elif (bhk < 1):
        st.warning("Minimum value of bhk is 1")
        return False
    elif (bath < 1):
        st.warning("Minimum value of bathrooms is 1")
        return False

    return True

df = pd.DataFrame([[Location,Area,bhk,bath]],
              columns=['Location','Area in sqft', 'BHK', 'Bathrooms'])

st.header('Specified Input parameters')
st.write(df)
st.write('---')

submit = st.button('Predict')

pred = int()

def predict(location,sqft,bhk,bath):    
    loc_index = np.where(X.columns==location)[0][0]

    x = np.zeros(len(X.columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return lr.predict([x])[0]

if submit:
    if check_input():
        pred = predict(Location, Area, bhk, bath)
    if pred > 0:
        st.write("""## Predicted House Price : 
### Rs """, round(pred*100000,2))  
    else :
        st.write("""## Couldn't find any house as per your requirement!""")
