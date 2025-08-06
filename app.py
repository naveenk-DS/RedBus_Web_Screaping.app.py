import streamlit as st
import pandas as pd
import mysql.connector

# Load data from MySQL
@st.cache_data
def load_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="your_username",   # change this
        password="your_password",  # change this
        database="your_database"  # change this
    )
    df = pd.read_sql("SELECT * FROM bus_details", conn)
    conn.close()
    return df

st.set_page_config(page_title="RedBus Bus Search App", layout="wide")
st.title("🚌 RedBus - All India Bus Search")

# Load data
try:
    data = load_data()
except Exception as e:
    st.error("❌ Database connection failed. Check credentials or run your SQL server.")
    st.stop()

# Sidebar Filters
with st.sidebar:
    st.header("🔍 Filter Buses")
    states = data['Route_name'].dropna().unique().tolist()
    selected_state = st.selectbox("Select Route", states)

    max_price = int(data["Price"].max())
    price_range = st.slider("💰 Price Range", 0, max_price, (0, max_price))

    selected_type = st.multiselect("🛏️ Bus Type", options=data['Bus_Type'].dropna().unique().tolist())

# Filtering Logic
filtered = data[data["Route_name"] == selected_state]
filtered = filtered[(filtered["Price"] >= price_range[0]) & (filtered["Price"] <= price_range[1])]
if selected_type:
    filtered = filtered[filtered["Bus_Type"].isin(selected_type)]

if filtered.empty:
    st.warning("🚫 No matching buses found.")
else:
    st.success(f"✅ {len(filtered)} Buses Found")
    st.dataframe(filtered.head(10), use_container_width=True)
