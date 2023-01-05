# BENGALURU-HOUSE-PRICE-PREDICTOR

`Machine Leaning` `Linear Regression`

## Problem Statement

Prices of real estate properties are sophisticatedly linked with our economy. Buying a home, especially in a city like Bengaluru, is a tricky choice. While the major factors are usually the same for all metros, there are others to be considered for the Silicon Valley of India. With its help millennial crowd, vibrant culture, great climate and a slew of job opportunities, it is difficult to ascertain the price of a house in Bengaluru. Therefore, the goal of this project is to use machine learning to predict the selling prices of houses in Bengaluru based on many economic factors.

The model would predict the house price by taking 4 input parameters:
1. Location
2. Area
3. BHK
4. Bathrooms

## Data Collection

The dataset is obtained from Kaggle.

Link -> https://www.kaggle.com/amitabhajoy/bengaluru-house-price-data

## Modeling

### Steps involved in building the predictive model.
1. Importing required libraries and the dataset.
2. Data Cleaning.
3. Feature Engineering.
4. Dimensionality Reduction.
5. Removing Outliers.
6. Dummy Encoding.
7. Creating test and training partitions
8. Implementing the Models `a. Linear Regression` `b. Random Forest Regression` `c. XGBoost Regression`
9. Generating predictions over the train and test dataset for the above models
10. Evaluating the models.
11. Predicting Sales Price

`Bengaluru House Price Predictor.ipynb` contains the code for the above mentioned steps.

## Result
Linear Regression -> 86% acuuracy

Random Forest Regressor -> 77% accuracy

Xgboost Regressor -> 70% accuracy

## Deployment

The App for this model is built using `streamlit`. `app.py` contains the code of this application!

Below are the links of deployed app:

Streamlit deployment -> https://suhas-2002-bengaluru-house-price-predictor-app-vn7ino.streamlit.app/

## UI Interface

![image](https://user-images.githubusercontent.com/85097320/183143155-6f9c2b16-17b2-40db-a3b9-573fcaa69dad.png)

## Installing and Running the app locally

1. Download the code from this repository as zip.

![image](https://user-images.githubusercontent.com/85097320/183140634-c8fd7561-24bb-4f7a-8eca-e0c06ddf7e1d.png)

2. Unzip the folder.
3. Open your command prompt and change the directory to the above folder.
4. If you don't have python installed, install it using the command :
```console
pip install python
```
5. Install requirements.txt using the command :
```console
pip install -r requirements.txt
```
6. Now run the app.py using the command :
```console
streamlit run app.py
```
7. This will open the app locally!

![image](https://user-images.githubusercontent.com/85097320/183142072-1033268a-066b-4ceb-b8d8-4d8a2e1d06b5.png)

## Predictions

![image](https://user-images.githubusercontent.com/85097320/183142956-cdeda555-144a-4101-b21d-bd42da650694.png)


