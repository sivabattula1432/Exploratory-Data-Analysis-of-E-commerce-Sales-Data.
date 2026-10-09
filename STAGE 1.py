#-----------------------------> Exploratory Data Analysis of E-commerce Sales Data <-------------------------------------------#

#  STAGE 1 ====>  Initial Undestanding and Dataset loading
#===================================================
# OBJECTIVE----->

''' ==> To load the retail sales dataset into Python using Pandas 
and perform an initial exploration to understand 
its structure, dimensions, data types, column names,
and overall data quality before beginning the
data cleaning and exploratory data analysis (EDA) process.
'''
#===================================================
# STEP 1: importing required library
import numpy as np
import pandas as pd

# STEP 2: loading the dataset

data=pd.read_csv("Sales.csv")

# STEP 3: Displaying the first five and last five rows in the above dataset

print(data.head())
print(data.tail())
print("\n" + "=" * 100)

# STEP 4:  finding the shape of the dataset 

print("Dataset shape")
print(data.shape)
print(f"rows : {data.shape[0]}")
print(f"columns : {data.shape[1]}")
print("\n" + "=" * 100)

# STEP 5: finding the column names

print("\n Column Names:")
print(data.columns)
print("\n" + "=" * 100)

# STEP 6: information within the data

print("\n Dataset information")
print(data.info())
print("\n" + "=" * 100)

# STEP 7: Checking missing values within the data

print("\n Missing values:")
print(data.isnull().sum())
print("\n" + "=" * 100)

# STEP 8: Statistical summary of the above data

print("\n Statistical summary:")
print(data.describe())
print("\n" + "=" * 100)


