import pandas as pd
#load the dataset
diabetes_data = pd.read_csv("../data/diabetes_data.csv")
#Quick Overview
print("first 5 rows:")
primt(diabetes_data.head())
print(\nDataset info:")
print("diabetes_data.info()")
print("\nStatistical summary:")
print(diabetes_data.describe())
