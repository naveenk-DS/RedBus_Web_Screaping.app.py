import streamlit as st
from scraper.redbus_scraper import scrape_redbus
import pandas as pd

st.set_page_config(page_title="RedBus Live Scraper", layout="wide")

st.title("🚌 RedBus Live Scraper - India")
st.markdown("Search for available buses in real-time from RedBus.in")

with st.form("search_form"):
    col1, col2, col3 = st.columns(3)
    with col1:
        source = st.text_input("Source", "Chennai")
    with col2:
        destination = st.text_input("Destination", "Bangalore")
    with col3:
        travel_date = st.text_input("Travel Date (dd-MMM-yyyy)", "03-Aug-2025")

    submitted = st.form_submit_button("🔍 Search Buses")

if submitted:
    st.info("Scraping RedBus... please wait ⏳")
    df = scrape_redbus(source, destination, travel_date)
    
    if not df.empty:
        st.success(f"Found {len(df)} buses")
        st.dataframe(df)
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download CSV", data=csv, file_name="redbus_data.csv", mime='text/csv')
    else:
        st.warning("No buses found or data couldn't be loaded.")
