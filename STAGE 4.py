#-----------------------------> Exploratory Data Analysis of E-commerce Sales Data <-------------------------------------------#

#  STAGE 4 ====>   Data Visualization
#===================================================
# OBJECTIVE----->

''' ==> To transform the analyzed data into meaningful 
visualizations that help stakeholders quickly understand sales 
performance, profitability, customer behaviour, and business trend.
'''
#===================================================

# STEP 1: importingf libraries and loading cleaned dataset

import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("cleaned_sales.csv")
data["Order Date"] = pd.to_datetime(data["Order Date"],format="mixed")
data["Ship Date"] = pd.to_datetime(data["Ship Date"],format="mixed")

# STEP 2: Represnting Sales by region (Bar chart)

sales_by_region=data.groupby("Region")["Sales"].sum().sort_values(ascending=False)
plt.figure(figsize=(10,5))
plt.bar(sales_by_region.index,sales_by_region.values)
plt.title(" Sales by region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/sales_by_region.png",dpi=300,bbox_inches="tight")
plt.show()


# STEP 3: Representing profit by region (Bar chart)


profit_by_region=data.groupby("Region")["Profit"].sum().sort_values(ascending=False)
plt.figure(figsize=(10,5))
plt.bar(profit_by_region.index,profit_by_region.values,color="green")
plt.title(" Profit by region")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/profit_by_region.png",dpi=300,bbox_inches="tight")
plt.show()


# STEP 4: Representing Sales by product category

sales_by_category=data.groupby("Product Category")["Sales"].sum().sort_values(ascending=False)
plt.figure(figsize=(8,5))
plt.bar(sales_by_category.index,sales_by_category.values,color="blue")
plt.title(" Sales by Product category")
plt.xlabel("Product category")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/sales_by_category.png",dpi=300,bbox_inches="tight")
plt.show()

# STEP 5: Representing Profit by product category

profit_by_category = (data.groupby("Product Category")["Profit"].sum().sort_values(ascending=False))
plt.figure(figsize=(7,7))
plt.pie(
    profit_by_category,
    labels=profit_by_category.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Profit Distribution by Product Category")
plt.savefig("charts/profit_by_category.png",dpi=300,bbox_inches="tight")
plt.show()


# STEP 6: Sales by customer segment (horizontal bar chat)

sales_by_segment = (data.groupby("Customer Segment")["Sales"].sum().sort_values())
plt.figure(figsize=(8,5))
plt.barh(sales_by_segment.index,sales_by_segment.values)
plt.title("Sales by Customer Segment")
plt.xlabel("Sales")
plt.ylabel("Customer Segment")
plt.tight_layout()
plt.savefig("charts/sales_by_segment.png",dpi=300,bbox_inches="tight")
plt.show()

# STEP 7: Visualizing Monthly Sales Trend (Line Chart)

data["YR_month"] = data["Order Date"].dt.to_period("M")
monthly_sales = data.groupby("YR_month")["Sales"].sum()
plt.figure(figsize=(12,5))
plt.plot(monthly_sales.index.astype(str),monthly_sales.values,marker="o",linewidth=2)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.savefig("charts/monthly_sales.png",dpi=300,bbox_inches="tight")
plt.show()


# STEP 8: Representing Monthly Profit Trend (Area Chart)

monthly_profit=data.groupby("YR_month")["Profit"].sum()
plt.figure(figsize=(12,5))
plt.fill_between(monthly_profit.index.astype(str),monthly_profit.values,alpha=0.5)
plt.plot(monthly_profit.index.astype(str),monthly_profit.values,marker="o")
plt.title("Monthly Profit Trend")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.savefig("charts/monthly_profit.png",dpi=300,bbox_inches="tight")
plt.show()

# STEP 9: Top 10 Products by Sales

top10_sales=data.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)
short_names=[name[:35]+"..." if len(name)>35 else name for name in top10_sales.index]
plt.figure(figsize=(12,6))
plt.barh(short_names,top10_sales.values)
plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Product Name")
plt.gca().invert_yaxis()
plt.grid(axis="x")
plt.tight_layout()
plt.savefig("charts/top10_sales.png",dpi=300,bbox_inches="tight")
plt.show()


# STEP 10: Top 10 Products by Profit

top10_profit=data.groupby("Product Name")["Profit"].sum().sort_values(ascending=False).head(10)
short_names=[name[:35]+"..." if len(name)>35 else name for name in top10_profit.index]
plt.figure(figsize=(12,6))
plt.barh(short_names,top10_profit.values)
plt.title("Top 10 Products by Profit")
plt.xlabel("Total Profit")
plt.ylabel("Product Name")
plt.gca().invert_yaxis()
plt.grid(axis="x")
plt.tight_layout()
plt.savefig("charts/top10_profit.png",dpi=300,bbox_inches="tight")
plt.show()


# STEP 11: Shipping Mode Distribution

shipping_mode=data["Ship Mode"].value_counts()
plt.figure(figsize=(7,7))
plt.pie(shipping_mode.values,
        labels=shipping_mode.index,
        autopct="%1.1f%%",
        startangle=90)
plt.title("Shipping Mode Distribution")
plt.savefig("charts/shipping_mode.png",dpi=300,bbox_inches="tight")
plt.show()


# STEP 12: Order Priority Distribution

order_priority=data["Order Priority"].value_counts()
plt.figure(figsize=(8,5))
plt.bar(order_priority.index,order_priority.values)
plt.title("Order Priority Distribution")
plt.xlabel("Order Priority")
plt.ylabel("Number of Orders")
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("charts/order_priority.png",dpi=300,bbox_inches="tight")
plt.show()