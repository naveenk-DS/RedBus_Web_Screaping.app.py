import streamlit as st
import pandas as pd

st.set_page_config(page_title="Redbus Data Viewer", layout="wide")

st.title("🚌 Redbus Data Scraper & Filter App")

from_city = st.text_input("From City", "Chennai")
to_city = st.text_input("To City", "Bangalore")
date = st.date_input("Travel Date").strftime("%d-%b-%Y")

if st.button("Scrape Redbus Data"):
    with st.spinner("Scraping in progress..."):
        df = scrape_redbus_data(from_city, to_city, date)
        st.success("Scraping completed! ✅")
        st.dataframe(df)

        # Save path confirmation
        st.info(f"Data saved to: `E:\\Naveen\\Scrap data\\redbus_data.csv`")

# Load data if already scraped
try:
    df = pd.read_csv(r"E:\Naveen\Scrap data\redbus_data.csv")
    st.subheader("📊 Filter Scraped Redbus Data")

    # Filters
    selected_operator = st.multiselect("Select Bus Operator(s)", options=df["Bus Operator"].unique())
    selected_price = st.slider("Select Price Range", int(df["Price"].min()), int(df["Price"].max()))

    filtered_df = df.copy()

    if selected_operator:
        filtered_df = filtered_df[filtered_df["Bus Operator"].isin(selected_operator)]

    filtered_df = filtered_df[filtered_df["Price"].astype(int) <= selected_price]

    st.dataframe(filtered_df)

except FileNotFoundError:
    st.warning("No scraped data found. Please scrape first using the above form.")
# ✅ Only define the function here, don't import from itself
def scrape_redbus_data(...):
    # scraping code
    return df
