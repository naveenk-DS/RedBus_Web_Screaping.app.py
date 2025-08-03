import streamlit as st
import pandas as pd

st.title("🚌 Redbus India-wide Bus Viewer")

# Load data
df = pd.read_csv("redbus_data.csv")

# Sidebar filters
st.sidebar.header("Filter Options")
cities_from = df["From"].unique()
cities_to = df["To"].unique()

selected_from = st.sidebar.selectbox("Source City", cities_from)
selected_to = st.sidebar.selectbox("Destination City", cities_to)

filtered_df = df[(df["From"] == selected_from) & (df["To"] == selected_to)]

st.write(f"Showing results for {selected_from} ➜ {selected_to}")
st.dataframe(filtered_df)

# Optional chart
st.bar_chart(filtered_df.groupby("Operator")["Price"].mean())
