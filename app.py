import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.analysis import root_cause_analysis
# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(page_title="Customer Analytics Dashboard", layout="wide")

st.title("📊 Customer Analytics Dashboard with Root Cause Analysis")

# ---------------------- LOAD DATA ----------------------
df = pd.read_csv("data/ecommerce.csv")

# Fix date format
df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True)

# ---------------------- SIDEBAR FILTER ----------------------
st.sidebar.header("Filters")
region = st.sidebar.selectbox("Select Region", df['region'].unique())

filtered_df = df[df['region'] == region]

# ---------------------- KPI CALCULATIONS ----------------------
revenue = filtered_df['sales'].sum()
orders = filtered_df.shape[0]
aov = revenue / orders if orders > 0 else 0

# ---------------------- KPI DISPLAY ----------------------
st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"${revenue:,.2f}")
col2.metric("Total Orders", orders)
col3.metric("Avg Order Value", f"${aov:,.2f}")

# ---------------------- SALES TREND ----------------------
st.subheader("📈 Sales Trend")

trend = filtered_df.groupby('order_date')['sales'].sum()

fig, ax = plt.subplots()
trend.plot(ax=ax)
ax.set_xlabel("Date")
ax.set_ylabel("Sales")

st.pyplot(fig)

# ---------------------- ROOT CAUSE ANALYSIS ----------------------
st.subheader("🔍 Root Cause Analysis")

