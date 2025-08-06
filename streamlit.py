# app.py - Streamlit UI for RedBus Scraper Pro Version

import streamlit as st
import pandas as pd
import os

# Load cleaned final bus data
DATA_PATH = "E:/RedBus_Scraper_App/datas/final_busdetails.csv"

@st.cache_data
def load_data():
    if os.path.exists(DATA_PATH):
        df = pd.read_csv(DATA_PATH)
        return df
    else:
        st.error("Data file not found. Please run the scraper first.")
        return pd.DataFrame()

df = load_data()

if not df.empty:
    st.title("🚌 RedBus Pro - Indian Bus Route Search")
    st.markdown("""
        Easily explore and filter bus information scraped from RedBus.in.
        - Search by **State**, **Route**, **Bus Type**, and more
        - View **Prices**, **Seat Availability**, and **Ratings**
    """)

    # Filters
    col1, col2, col3 = st.columns(3)

    with col1:
        selected_state = st.selectbox("Select State/RTC", options=sorted(df['Route_name'].dropna().unique()))

    with col2:
        bus_type = st.selectbox("Select Bus Type", options=['All'] + sorted(df['Bus_Type'].dropna().unique()))

    with col3:
        min_seats = st.slider("Minimum Seats Available", 0, 50, 1)

    # Apply filters
    filtered_df = df[df['Route_name'] == selected_state]

    if bus_type != 'All':
        filtered_df = filtered_df[filtered_df['Bus_Type'] == bus_type]

    filtered_df = filtered_df[filtered_df['Seats_available'] >= min_seats]

    st.subheader(f"Showing {len(filtered_df)} Buses")

    st.dataframe(filtered_df[['Route_name', 'Bus_Name', 'Bus_Type', 'Departing_Time',
                              'Reaching_Time', 'Duration', 'Price', 'Seats_available', 'Star_Rating']], use_container_width=True)

    # Download button
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Filtered Data as CSV",
        data=csv,
        file_name='filtered_bus_data.csv',
        mime='text/csv'
    )

else:
    st.warning("No data to show.")
