# app.py
import streamlit as st
import pandas as pd
import os

# ------------------------
# 🔁 Function definition (was in redbus_scraper.py)
# ------------------------
def scrape_redbus_data(from_city='Chennai', to_city='Bangalore', date='16-Jul-2025'):
    data = {
        'Bus Operator': ['KPN Travels', 'SRS Travels', 'Parveen Travels'],
        'Price': [750, 850, 950],
        'Departure Time': ['6:00 PM', '9:00 PM', '11:30 PM'],
        'From': [from_city] * 3,
        'To': [to_city] * 3,
        'Date': [date] * 3
    }

    df = pd.DataFrame(data)

    output_dir = r"E:\Naveen\Scrap data"
    os.makedirs(output_dir, exist_ok=True)
    df.to_csv(os.path.join(output_dir, 'redbus_data.csv'), index=False)

    return df

# ------------------------
# 🚀 Streamlit UI
# ------------------------
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

# ------------------------
# 📂 Load saved CSV (local use only)
# ------------------------
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
