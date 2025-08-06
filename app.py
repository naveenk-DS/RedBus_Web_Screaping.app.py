# app.py
import streamlit as st
import pandas as pd
import os

DATA_PATH = "E:/RedBus_Scraper_App/final_busdetails.csv"

st.set_page_config(page_title="RedBus Scraper", layout="wide")
st.title("🚌 RedBus Route Explorer (All India)")

if not os.path.exists(DATA_PATH):
    st.warning("⚠️ Data file not found. Please run the scraper first.")
else:
    df = pd.read_csv(DATA_PATH)

    if df.empty:
        st.error("❌ No data to show.")
    else:
        states = sorted(df['Route_name'].str.split(" to ").str[0].dropna().unique())
        selected_state = st.selectbox("Select State (From City):", states)

        filtered = df[df['Route_name'].str.startswith(selected_state)]
        cities = sorted(filtered['Route_name'].str.split(" to ").str[1].dropna().unique())
        selected_city = st.selectbox("To City:", cities)

        result = df[df['Route_name'] == f"{selected_state} to {selected_city}"]

        st.markdown(f"### 🎯 Matching Buses from **{selected_state}** to **{selected_city}**")
        st.dataframe(result.head(10), use_container_width=True)

        csv = result.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download CSV", csv, "filtered_buses.csv", "text/csv", key='download-csv')
