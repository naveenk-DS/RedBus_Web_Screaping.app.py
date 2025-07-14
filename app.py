import streamlit as st
import pandas as pd
df = pd.read_csv(r"E:/Naveen/Scrap data/datas/final_busdetails_df.csv")

# App title
st.set_page_config(page_title="Redbus Data Viewer", layout="wide")
st.title("🚌 Redbus Data Scraping Dashboard")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("redbus_data.csv")  # Replace with your CSV name
    return df

df = load_data()

# Show full dataframe
st.subheader("📊 Scraped Bus Data")
st.dataframe(df)

# Filters
st.sidebar.header("🔍 Filter Options")

# Filter by source city
if 'Source' in df.columns:
    source_cities = df['Source'].dropna().unique().tolist()
    selected_source = st.sidebar.multiselect("Select Source City", source_cities)
    if selected_source:
        df = df[df['Source'].isin(selected_source)]

# Filter by destination city
if 'Destination' in df.columns:
    dest_cities = df['Destination'].dropna().unique().tolist()
    selected_dest = st.sidebar.multiselect("Select Destination City", dest_cities)
    if selected_dest:
        df = df[df['Destination'].isin(selected_dest)]

# Filter by Bus Type
if 'Bus Type' in df.columns:
    bus_types = df['Bus Type'].dropna().unique().tolist()
    selected_bus_type = st.sidebar.multiselect("Select Bus Type", bus_types)
    if selected_bus_type:
        df = df[df['Bus Type'].isin(selected_bus_type)]

# Display filtered data
st.subheader("🔎 Filtered Results")
st.write(f"Total Results: {len(df)}")
st.dataframe(df)

# Optional: Save filtered data
if not df.empty:
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Filtered Data as CSV",
        data=csv,
        file_name="filtered_redbus_data.csv",
        mime="text/csv"
    )
