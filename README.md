# Predictive NL Machine Learning - Santander

- [link: ***Deployment of webpage and app***](<https://santander-predictor.herokuapp.com/>)

![Santader.png](static/images/Santader.png)

## Background
Our mission is to help Banco Santander identify the customers that will make a transaction and understand their financial health in order to solve the most common challenge on binary classification problems such as: is a customer satisfied? Will a customer buy this product? Can a customer pay this loan? We will try to surpass the current results comparig different models precision and accuracy. With this knowledge Santander will know which products and services might help them achieve their monetary goals.

## Dataset
We found a Dataset from Santander that invites Kaggler´s to participate on a competition to identify which customers will make a transaction. The dataset contains a train.csv and a test.csv which are anonymized for privacy affairs. You can find the dataset on the next link:
https://www.kaggle.com/c/santander-customer-transaction-prediction

## The Challenge
We will solve a binary classification problem:
INPUT: Will the customer will make a transaction?
OUTPUT: Yes/No
This binary problem solves questions like: is the customer satisfied? Will a customer buy this product? Can a customer pay this loan?
With our Machine Learnig Algorythm - Neuronal Network we will Identify which customers will make a specific transaction in the future, irrespective of the amount of money transacted or not.

## Model
We chose to run a neuronal network with the following structure:

Model: "sequential"

## Data preprocessing
1. Variables does show very low correlation among them, meaning that variables are independent. Variables while plotting them in box plots show outliers that mainly are coming from target "1" data.
2. Variables were passed through a Standard Scaler before fitting them into the model.
3. Tune and balance the dataset.

## Conclusions
Dataset
- 2 outputs
    0 = No transaction
    1 = Transaction

- 200 variables

## Dataset testing results
- 89.95% corresponds to target "0" and 10.04% corresponds to target "1".
- We decided to down sampling target "0" data to better train our model, leaving the dataset as follow: 33.33% for target "0" and 66.66% for target "1".



