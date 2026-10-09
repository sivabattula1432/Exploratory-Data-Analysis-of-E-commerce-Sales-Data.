#-----------------------------> Exploratory Data Analysis of E-commerce Sales Data <-------------------------------------------#

#  STAGE 2 ====>  Data Cleaning & Preprocessing
#===================================================
# OBJECTIVE----->

''' ==> To improve the quality of the dataset by identifying 
and handling missing values, duplicate records, incorrect data types,
and inconsistent data 
so that the dataset is ready for analysis.
'''
#===================================================

#loading the dataset
import pandas as pd
data=pd.read_csv("Sales.csv")

# STEP 1: Checking for missing values

print("Missing Values:")
print(data.isnull().sum())
print()

print("\n Total missing values:")
print(data.isnull().sum().sum())
print("\n" + "=" * 100)

# STEP 2: filling missing values with median 

data["Product Base Margin"]=data["Product Base Margin"].fillna(data["Product Base Margin"].median())

# final checking of missing values after filling with median
print("\n after performing filling missing values count is :")
print(data["Product Base Margin"].isnull().sum())
print("\n" + "=" * 100)

# STEP 3: identifying the datatypes of the each column in the dataset

print(data.dtypes)
print()

# STEP 4: convertig the date columns 

data["Order Date"] = pd.to_datetime(data["Order Date"],format="mixed")
data["Ship Date"] = pd.to_datetime(data["Ship Date"],format="mixed")


print(data.dtypes)
print("\n" + "=" * 100)

# STEP 5: checking the duplicate rows

print("Duplicated Rows:")
print(data.duplicated().sum())
print("\n" + "=" * 100)


# STEP 6: updating the dataset in cleaned format

# an error has occurred while saving the file to solve that i am droping unwanted columns within the dataset
data=data.drop(columns=["Unnamed: 0"],errors="ignore")
data.to_csv("cleaned_sales.csv",index=False)

