# app.py
import streamlit as st
import pandas as pd
from redbus_scraper import scrape_redbus_data

st.set_page_config(page_title="Redbus Scraper", layout="wide")
st.title("🚌 Redbus Data Viewer (Mock Version for Cloud)")

from_city = st.text_input("From City", "Chennai")
to_city = st.text_input("To City", "Bangalore")
date = st.date_input("Travel Date").strftime("%d-%b-%Y")

if st.button("Scrape Mock Redbus Data"):
    with st.spinner("Scraping..."):
        df = scrape_redbus_data(from_city, to_city, date)
        st.success("Scraping done!")
        st.dataframe(df)

# Try loading saved data
try:
    df = pd.read_csv(r"E:\Naveen\Scrap data\redbus_data.csv")

    st.subheader("📊 Filter Scraped Data")
    selected_operator = st.multiselect("Select Bus Operators", options=df["Bus Operator"].unique())
    selected_price = st.slider("Max Price", int(df["Price"].min()), int(df["Price"].max()))

    filtered_df = df.copy()
    if selected_operator:
        filtered_df = filtered_df[filtered_df["Bus Operator"].isin(selected_operator)]
    filtered_df = filtered_df[filtered_df["Price"] <= selected_price]

    st.dataframe(filtered_df)

except FileNotFoundError:
    st.warning("Please click 'Scrape' to generate mock data.")
