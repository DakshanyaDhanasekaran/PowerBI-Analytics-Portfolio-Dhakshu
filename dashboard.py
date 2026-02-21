import streamlit as st
import requests
import pandas as pd
import time
import plotly.express as px

st.set_page_config(layout="wide")

# -------- HEADER --------
st.markdown("## Real-Time Sales Performance Dashboard")
st.markdown("---")

# -------- SIDEBAR FILTERS --------
st.sidebar.header("Report Filters")

regions = ["North", "South", "East", "West"]
categories = ["Electronics", "Clothing", "Home", "Sports"]

selected_regions = st.sidebar.multiselect("Region", regions, default=regions)
selected_categories = st.sidebar.multiselect("Category", categories, default=categories)
sales_range = st.sidebar.slider("Sales Range", 500, 5000, (500, 5000))

run_stream = st.sidebar.checkbox("Enable Real-Time Data", value=True)

records = []

while run_stream:
    response = requests.get("http://127.0.0.1:8000/stream")
    new_data = response.json()
    records.append(new_data)

    df = pd.DataFrame(records)

    if len(df) > 0:

        # -------- APPLY FILTERS --------
        df = df[df["region"].isin(selected_regions)]
        df = df[df["category"].isin(selected_categories)]
        df = df[(df["sales"] >= sales_range[0]) & (df["sales"] <= sales_range[1])]

        if len(df) == 0:
            st.warning("No records match selected filters.")
            time.sleep(2)
            continue

        # -------- KPI CALCULATIONS --------
        total_sales = df["sales"].sum()
        total_profit = df["profit"].sum()
        avg_rating = df["rating"].mean()
        total_orders = len(df)
        profit_margin = (total_profit / total_sales) * 100

        # -------- KPI ROW --------
        k1, k2, k3, k4, k5 = st.columns(5)

        k1.metric("Total Sales", f"{total_sales:,.0f}")
        k2.metric("Total Profit", f"{total_profit:,.0f}")
        k3.metric("Total Orders", total_orders)
        k4.metric("Avg Rating", f"{avg_rating:.2f}")
        k5.metric("Profit Margin %", f"{profit_margin:.2f}%")

        st.markdown("---")

        # -------- VISUAL ROW 1 --------
        col1, col2 = st.columns(2)

        # Sales Trend
        sales_trend = px.line(
            df,
            x=df.index,
            y="sales",
            title="Sales Trend",
            color_discrete_sequence=["#2F80ED"]
        )
        col1.plotly_chart(sales_trend, use_container_width=True)

        # Region Sales
        region_sales = df.groupby("region")["sales"].sum().reset_index()
        region_chart = px.bar(
            region_sales,
            x="region",
            y="sales",
            color="region",
            title="Sales by Region"
        )
        col2.plotly_chart(region_chart, use_container_width=True)

        # -------- VISUAL ROW 2 --------
        col3, col4 = st.columns(2)

        category_profit = df.groupby("category")["profit"].sum().reset_index()
        category_chart = px.pie(
            category_profit,
            names="category",
            values="profit",
            title="Profit by Category"
        )
        col3.plotly_chart(category_chart, use_container_width=True)

        heatmap_data = df.pivot_table(
            values="profit",
            index="region",
            columns="category",
            aggfunc="sum"
        )

        heatmap = px.imshow(
            heatmap_data,
            text_auto=True,
            color_continuous_scale="Blues",
            title="Profit Heatmap"
        )
        col4.plotly_chart(heatmap, use_container_width=True)

    time.sleep(2)