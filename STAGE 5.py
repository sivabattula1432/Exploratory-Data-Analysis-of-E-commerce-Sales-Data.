#-----------------------------> Exploratory Data Analysis of E-commerce Sales Data <-------------------------------------------#

#  STAGE 5 ====>  KPI (Key Performance Indicator) Analysis
#===================================================
# OBJECTIVE----->

''' ==> To calculate key business performance metrics
that provide a quick overview of the company's sales,
profitability, orders, and operational performance.
'''
#===================================================

# STEP 1: loading cleaned dataset

import pandas as pd
data=pd.read_csv("cleaned_sales.csv")
data["Order Date"] = pd.to_datetime(data["Order Date"],format="mixed")
data["Ship Date"] = pd.to_datetime(data["Ship Date"],format="mixed")

# STEP 2: finding KPI's and calculating 

total_sales=data["Sales"].sum()

total_profit=data["Profit"].sum()

total_orders=data["Order ID"].nunique()

total_transactions=len(data)

average_discount=data["Discount"].mean()

profit_margin=(total_profit/total_sales)*100

average_order_value=total_sales/total_orders

average_profit_per_order=total_profit/total_orders

average_sales_per_transaction=total_sales/total_transactions

average_profit_per_transaction=total_profit/total_transactions

highest_sale=data["Sales"].max()

highest_profit=data["Profit"].max()

print("\n" + "=" * 100)

# STEP 3: Displaying the calculated KPI values
print()
print("_________________________________________BUSINESS KPI SUMMARY_____________________________________________________")
print()
print(f"Total Sales                   : {total_sales:.2f}")
print(f"Total Profit                  : {total_profit:.2f}")
print(f"Total Orders                  : {total_orders}")
print(f"Total Transactions            : {total_transactions}")
print(f"Average Discount              : {average_discount:.2%}")
print(f"Profit Margin                 : {profit_margin:.2f} %")
print(f"Average Order Value           : {average_order_value:.2f}")
print(f"Average Profit per Order      : {average_profit_per_order:.2f}")
print(f"Average Sales per Transaction : {average_sales_per_transaction:.2f}")
print(f"Average Profit per Transaction: {average_profit_per_transaction:.2f}")
print(f"Highest Single Sale           : {highest_sale:.2f}")
print(f"Highest Single Profit         : {highest_profit:.2f}")



