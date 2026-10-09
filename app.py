#-----------------------------> Exploratory Data Analysis of E-commerce Sales Data <-------------------------------------------#

# STAGE 7 =====> STREAMLIT DASHBOARD
#==================================================================================================

# OBJECTIVE ----->

'''
==> To build an interactive dashboard using Streamlit that displays sales data,
KPIs, charts, and business insights in a clear and user-friendly manner,
helping users analyze business performance and make informed decisions.
'''

# STEP 1: Importing Required Libraries

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# STEP 2: Configuring the Dashboard Page

st.set_page_config(
    page_title="Retail Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

# STEP 3: Displaying the Dashboard Title

st.title("📊 Retail Sales Analytics Dashboard")
st.markdown(" 📌 Sales Performance Analysis using Python")

# STEP 4: Loading the Cleaned Dataset

data=pd.read_csv("cleaned_sales.csv")

# STEP 5: Displaying the Dataset Preview

st.subheader("Dataset Preview")
st.dataframe(data.head())

# STEP 6: Creating KPI cards

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

# STEP 7: Displaying kpi cards

st.subheader("📊 Business KPI Dashboard")

col1,col2,col3,col4=st.columns(4)
with col1:
    st.metric("💰 Total Sales",f"{total_sales:,.2f}")
with col2:
    st.metric("📈 Total Profit",f"{total_profit:,.2f}")
with col3:
    st.metric("🛒 Total Orders",f"{total_orders}")
with col4:
    st.metric("📦 Total Transactions",f"{total_transactions}")
col5,col6,col7,col8=st.columns(4)
with col5:
    st.metric("🏷️ Avg Discount",f"{average_discount:.2%}")
with col6:
    st.metric("📊 Profit Margin",f"{profit_margin:.2f}%")
with col7:
    st.metric("💳 Avg Order Value",f"{average_order_value:,.2f}")
with col8:
    st.metric("💵 Avg Profit / Order",f"{average_profit_per_order:,.2f}")
col9,col10,col11,col12=st.columns(4)
with col9:
    st.metric("📈 Avg Sales / Transaction",f"{average_sales_per_transaction:,.2f}")
with col10:
    st.metric("💹 Avg Profit / Transaction",f"{average_profit_per_transaction:,.2f}")
with col11:
    st.metric("🏆 Highest Sale",f"{highest_sale:,.2f}")
with col12:
    st.metric("⭐ Highest Profit",f"{highest_profit:,.2f}")

# STEP 7: Creating Interactive Sidebar Filters

st.sidebar.header("🔍 Dashboard Filters")

selected_region=st.sidebar.selectbox(
    "Select Region",
    ["All"]+sorted(data["Region"].unique().tolist())
)

selected_category=st.sidebar.selectbox(
    "Select Product Category",
    ["All"]+sorted(data["Product Category"].unique().tolist())
)

selected_segment=st.sidebar.selectbox(
    "Select Customer Segment",
    ["All"]+sorted(data["Customer Segment"].unique().tolist())
)  

# STEP 8: Applying the Sidebar Filters and Displaying the filtered data

filtered_data=data.copy()

if selected_region!="All":
    filtered_data=filtered_data[filtered_data["Region"]==selected_region]
if selected_category!="All":
    filtered_data=filtered_data[filtered_data["Product Category"]==selected_category]
if selected_segment!="All":
    filtered_data=filtered_data[filtered_data["Customer Segment"]==selected_segment]

st.subheader("📋 Filtered Dataset")

st.dataframe(filtered_data)  

# STEP 9: Dynamic KPI Dashboard after data is filtered

total_sales=filtered_data["Sales"].sum()
total_profit=filtered_data["Profit"].sum()
total_orders=filtered_data["Order ID"].nunique()
total_transactions=len(filtered_data)
average_discount=filtered_data["Discount"].mean()
profit_margin=(total_profit/total_sales)*100 if total_sales!=0 else 0
average_order_value=total_sales/total_orders if total_orders!=0 else 0
average_profit_per_order=total_profit/total_orders if total_orders!=0 else 0
average_sales_per_transaction=total_sales/total_transactions if total_transactions!=0 else 0
average_profit_per_transaction=total_profit/total_transactions if total_transactions!=0 else 0
highest_sale=filtered_data["Sales"].max()
highest_profit=filtered_data["Profit"].max()


# STEP 11: Sales by Region Chart

sales_by_region=filtered_data.groupby("Region")["Sales"].sum().sort_values(ascending=False)
fig,ax=plt.subplots(figsize=(9,5))
ax.bar(sales_by_region.index,sales_by_region.values,color="royalblue",edgecolor="black",linewidth=1)
ax.set_title("Sales by Region",fontsize=17,fontweight="bold",color="darkblue",pad=12)
ax.set_xlabel("Region",fontsize=13,fontweight="bold",color="darkred")
ax.set_ylabel("Total Sales",fontsize=13,fontweight="bold",color="darkgreen")
ax.tick_params(axis="x",labelsize=10)
ax.tick_params(axis="y",labelsize=10)
plt.xticks(rotation=15,ha="right")
ax.grid(axis="y",linestyle="--",alpha=0.3)
plt.tight_layout()
st.pyplot(fig)

# STEP 12: Profit by Region Chart

profit_by_region=filtered_data.groupby("Region")["Profit"].sum().sort_values(ascending=False)
fig,ax=plt.subplots(figsize=(9,5))
ax.bar(profit_by_region.index,profit_by_region.values,color="limegreen",edgecolor="black",linewidth=1)
ax.set_title("Profit by Region",fontsize=17,fontweight="bold",color="darkblue",pad=12)
ax.set_xlabel("Region",fontsize=13,fontweight="bold",color="darkred")
ax.set_ylabel("Total Profit",fontsize=13,fontweight="bold",color="darkgreen")
ax.tick_params(axis="x",labelsize=10)
ax.tick_params(axis="y",labelsize=10)
plt.xticks(rotation=15,ha="right")
ax.grid(axis="y",linestyle="--",alpha=0.3)
plt.tight_layout()
st.pyplot(fig)

# Converting Date Columns to Datetime Format

filtered_data["Order Date"]=pd.to_datetime(filtered_data["Order Date"],format="mixed")
filtered_data["Ship Date"]=pd.to_datetime(filtered_data["Ship Date"],format="mixed")

# STEP 13: Monthly Sales Trend
# Displaying only every 3rd month label on X-axis to avoid clumsiveness

filtered_data["YR_month"]=filtered_data["Order Date"].dt.strftime("%y-%m")
monthly_sales=filtered_data.groupby("YR_month")["Sales"].sum()
fig,ax=plt.subplots(figsize=(9,5))
ax.plot(monthly_sales.index,monthly_sales.values,marker="o",markersize=5,color="royalblue",linewidth=2.5)
ax.set_title("Monthly Sales Trend",fontsize=17,fontweight="bold",color="darkblue",pad=12)
ax.set_xlabel("Month",fontsize=13,fontweight="bold",color="darkred")
ax.set_ylabel("Total Sales",fontsize=13,fontweight="bold",color="darkgreen")
ax.tick_params(axis="y",labelsize=10)
ax.set_xticks(range(0,len(monthly_sales.index),3))
ax.set_xticklabels(monthly_sales.index[::3],rotation=45,ha="right",fontsize=10,fontweight="bold")
ax.grid(linestyle="--",alpha=0.3)
plt.tight_layout()
st.pyplot(fig)

# STEP 14: Monthly Profit Trend
# Displaying only every 3rd month label on X-axis to avoid clumsiveness

monthly_profit=filtered_data.groupby("YR_month")["Profit"].sum()
fig,ax=plt.subplots(figsize=(9,5))
ax.plot(monthly_profit.index,monthly_profit.values,marker="o",markersize=5,color="green",linewidth=2.5)
ax.set_title("Monthly Profit Trend",fontsize=17,fontweight="bold",color="darkblue",pad=12)
ax.set_xlabel("Month",fontsize=13,fontweight="bold",color="darkred")
ax.set_ylabel("Total Profit",fontsize=13,fontweight="bold",color="darkgreen")
ax.tick_params(axis="y",labelsize=10)
ax.set_xticks(range(0,len(monthly_profit.index),3))
ax.set_xticklabels(monthly_profit.index[::3],rotation=45,ha="right",fontsize=10,fontweight="bold")
ax.grid(linestyle="--",alpha=0.3)
plt.tight_layout()
st.pyplot(fig)

# STEP 15: Sales by Product Category

sales_by_category=filtered_data.groupby("Product Category")["Sales"].sum().sort_values(ascending=False)
fig,ax=plt.subplots(figsize=(9,5))
ax.bar(sales_by_category.index,sales_by_category.values,color="orange",edgecolor="black",linewidth=1)
ax.set_title("Sales by Product Category",fontsize=17,fontweight="bold",color="darkblue",pad=12)
ax.set_xlabel("Product Category",fontsize=13,fontweight="bold",color="darkred")
ax.set_ylabel("Total Sales",fontsize=13,fontweight="bold",color="darkgreen")
ax.tick_params(axis="x",labelsize=10)
ax.tick_params(axis="y",labelsize=10)
plt.xticks(fontsize=10,fontweight="bold")
ax.grid(axis="y",linestyle="--",alpha=0.3)
plt.tight_layout()
st.pyplot(fig)

# STEP 16: Profit by Product Category

profit_by_category=filtered_data.groupby("Product Category")["Profit"].sum().sort_values(ascending=False)
fig,ax=plt.subplots(figsize=(9,5))
ax.bar(profit_by_category.index,profit_by_category.values,color="crimson",edgecolor="black",linewidth=1)
ax.set_title("Profit by Product Category",fontsize=17,fontweight="bold",color="darkblue",pad=12)
ax.set_xlabel("Product Category",fontsize=13,fontweight="bold",color="darkred")
ax.set_ylabel("Total Profit",fontsize=13,fontweight="bold",color="darkgreen")
ax.tick_params(axis="x",labelsize=10)
ax.tick_params(axis="y",labelsize=10)
plt.xticks(fontsize=10,fontweight="bold")
ax.grid(axis="y",linestyle="--",alpha=0.3)
plt.tight_layout()
st.pyplot(fig)

# STEP 17: Top 10 Products by Sales

top_sales=filtered_data.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)
top_sales.index=[name[:25]+"..." if len(name)>25 else name for name in top_sales.index]
fig,ax=plt.subplots(figsize=(10,6))
ax.barh(top_sales.index,top_sales.values,color="dodgerblue",edgecolor="black",linewidth=1)
ax.set_title("Top 10 Products by Sales",fontsize=17,fontweight="bold",color="darkblue",pad=12)
ax.set_xlabel("Total Sales",fontsize=13,fontweight="bold",color="darkred")
ax.set_ylabel("Product Name",fontsize=13,fontweight="bold",color="darkgreen")
ax.tick_params(axis="x",labelsize=10)
ax.tick_params(axis="y",labelsize=9)
ax.grid(axis="x",linestyle="--",alpha=0.3)
plt.tight_layout()
st.pyplot(fig)

# STEP 18: Top 10 Products by Profit

top_profit=filtered_data.groupby("Product Name")["Profit"].sum().sort_values(ascending=False).head(10)
top_profit.index=[name[:25]+"..." if len(name)>25 else name for name in top_profit.index]
fig,ax=plt.subplots(figsize=(10,6))
ax.barh(top_profit.index,top_profit.values,color="seagreen",edgecolor="black",linewidth=1)
ax.set_title("Top 10 Products by Profit",fontsize=17,fontweight="bold",color="darkblue",pad=12)
ax.set_xlabel("Total Profit",fontsize=13,fontweight="bold",color="darkred")
ax.set_ylabel("Product Name",fontsize=13,fontweight="bold",color="darkgreen")
ax.tick_params(axis="x",labelsize=10)
ax.tick_params(axis="y",labelsize=9)
ax.grid(axis="x",linestyle="--",alpha=0.3)
plt.tight_layout()
st.pyplot(fig)

# STEP 19: Correlation Heatmap

import seaborn as sns

corr=filtered_data[["Sales","Profit","Discount","Order Quantity","Shipping Cost","Unit Price"]].corr()

fig,ax=plt.subplots(figsize=(8,6))
sns.heatmap(corr,annot=True,cmap="coolwarm",linewidths=0.5,fmt=".2f",ax=ax)
ax.set_title("Correlation Heatmap",fontsize=17,fontweight="bold",color="darkblue",pad=12)
plt.xticks(fontsize=10,fontweight="bold",rotation=30,ha="right")
plt.yticks(fontsize=10,fontweight="bold",rotation=0)
plt.tight_layout()
st.pyplot(fig)

# STEP 20: Business Insights

st.subheader("📌 Business Insights")

top_region=filtered_data.groupby("Region")["Sales"].sum().idxmax()
top_category=filtered_data.groupby("Product Category")["Sales"].sum().idxmax()
top_segment=filtered_data.groupby("Customer Segment")["Sales"].sum().idxmax()
top_product=filtered_data.groupby("Product Name")["Sales"].sum().idxmax()

st.info(f"🏆 Highest Sales Region : {top_region}")
st.info(f"📦 Best Product Category : {top_category}")
st.info(f"👥 Best Customer Segment : {top_segment}")
st.info(f"⭐ Best Selling Product : {top_product}")

# STEP 21: Dashboard Footer

st.markdown("---")
st.markdown("### 📊 Retail Sales Analytics Dashboard")
st.write("**Developed by:** Bhanuprasad K")
st.write("**Tools Used:** Python | Pandas | Matplotlib | Streamlit")
st.write("**Project:** Exploratory Data Analysis of E-commerce Sales Data")
st.success("✅ Dashboard Developed Successfully")