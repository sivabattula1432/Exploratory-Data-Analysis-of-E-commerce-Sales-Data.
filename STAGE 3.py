#-----------------------------> Exploratory Data Analysis of E-commerce Sales Data <-------------------------------------------#

#  STAGE 3 ====>  Exploratory Data Analysis
#===================================================
# OBJECTIVE----->

''' ==> It is key stage of this project 
the main obejctive of this stage 3 is
To perform Exploratory Data Analysis (EDA) on the cleaned 
sales dataset to uncover business trends, identify sales
and profit patterns, evaluate customer and product performance, and 
generate actionable insights that support data-driven business decisions.
'''
#===================================================

# STEP 1: Loading the cleaned dataset

import pandas as pd
data=pd.read_csv("cleaned_sales.csv")

# again converting the date columns into proper format
data["Order Date"] = pd.to_datetime(data["Order Date"],format="mixed")
data["Ship Date"] = pd.to_datetime(data["Ship Date"],format="mixed")

# displaying the fisrt five rows of data and all column names after cleaning process
print(data.head())
print()
print(data.columns)


print("\n" + "=" * 100)


# STEP 2: Calculating the overall business performance

total_transactions=len(data)
total_orders=data["Order ID"].nunique()
total_sales=data["Sales"].sum()
total_profit=data["Profit"].sum()

print("* "*50)
print()
print("                             OVERALL BUSINESS PERFORMANCE           ")
print()
print("TOTAL TRANSACTIONS : ",total_transactions)
print("TOTAL ORDERS : ",total_orders)
print("TOTAL SALES : ",round(total_sales,2))
print("TOTAL PROFIT : ",round(total_profit,2))
print("\n" + "=" * 100)


# STEP 3: Sales Analysis by region

sales_by_region=data.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print("\n \n")
print("____________________SALES BY REGION_____________________")
print(round(sales_by_region,5))
print()
print("\n" + "=" * 100)



# STEP 4: Profit  Analysis by Region

profit_by_region=data.groupby("Region")["Profit"].sum().sort_values(ascending=False)
print("\n \n")
print("______________________PROFIT BY REGION___________________")
print(profit_by_region)
print()
print("\n" + "=" * 100)

# STEP 5: Sales Analysis by Product category

sales_by_category=data.groupby("Product Category")["Sales"].sum().sort_values(ascending=False)
print("\n \n")
print("_____________________SALES BY PRODUCT CATEGORY___________________")
print(sales_by_category)
print()
print("\n" + "=" * 100)


# STEP 5: Profit Analysis by Product category

profit_by_category=data.groupby("Product Category")["Profit"].sum().sort_values(ascending=False)
print("\n \n")
print("_____________________PROFIT BY PRODUCT CATEGORY___________________")
print(profit_by_category)
print("\n" + "=" * 100) 

# STEP 6: Sales by customer segment

sales_by_segment=data.groupby("Customer Segment")["Sales"].sum().sort_values(ascending=False)
print("\n \n")
print("_______________________Sales by Customer Segment_____________________")
print(sales_by_segment)
print("\n" + "=" * 100) 

# STEP 7: Profit by customer segment

profit_by_segment=data.groupby("Customer Segment")["Profit"].sum().sort_values(ascending=False)
print("\n \n")
print("_______________________profit by Customer Segment_____________________")
print(profit_by_segment)
print("\n" + "=" * 100) 



# print(data["Order Date"].dtype)
# print(data["Order Date"].head(25))
# print(data["Order Date"].isna().sum())

# STEP 8: Monthly sales trend analysis

#extracting months from the Order date column
data["YR_month"]=data["Order Date"].dt.to_period("M")
monthly_sales=data.groupby("YR_month")["Sales"].sum()
print("\n \n")
print("________________________MONTHLY SALES ANALYSIS_______________________")
print(monthly_sales)
print("\n" + "=" * 100) 



# STEP 9: Monthly profit analysis

monthly_profit=data.groupby("YR_month")["Profit"].sum()
print("\n \n")
print("________________________MONTHLY Profit ANALYSIS_______________________")
print(monthly_profit)
print("\n" + "=" * 100)


# STEP 10: Top 10 products by sales

top10_sales=(data.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10))
print("\n \n")
print("_____________________________ TOP 10 PRODUCTS BY SALES_________________________________")
print(top10_sales)
print("\n" + "=" * 100)


# STEP 11: Top 10 products by profit

top10_profit=(data.groupby("Product Name")["Profit"].sum().sort_values(ascending=False).head(10))
print("\n \n")
print("_____________________________ TOP 10 PRODUCTS BY PROFIT_________________________________")
print(top10_profit)
print("\n" + "=" * 100)


# STEP 12: Discount vs profit analysis

correlation=data["Discount"].corr(data["Profit"])
print("\n \n")
print("________________________DISCOUNT VS PROFIT ANALYSIS____________________________")
print()
print("correlation between discount and profit : ",round(correlation,2))
print("\n" + "=" * 100)


# STEP 13: Shipping mode analysis

ship_mode=(data.groupby("Ship Mode")["Order ID"].count().sort_values(ascending=False))
print("\n \n")
print("_______________________SHIPPING MODE ANALYSIS___________________________________")
print(ship_mode)
print("\n" + "=" * 100)


# STEP 14: Order Priority Analysis

ord_prior=(data.groupby("Order Priority")["Order ID"].count().sort_values(ascending=False))
print("\n \n")
print("___________________________ORDER PRIORITY_________________________________________")
print(ord_prior)
print("\n" + "=" * 100)


