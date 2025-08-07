import streamlit as st
import pandas as pd
from db_config import get_connection

st.set_page_config(page_title="RedBus Scraper", layout="wide")
st.title("🚌 RedBus Data Filtering App")

def load_data():
    conn = get_connection()
    query = "SELECT * FROM rb_bus_routes"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

df = load_data()

# ✅ Sidebar filters
with st.sidebar:
    st.header("🔍 Filter Options")
    
    # Route selection
    route = st.selectbox("Select Route", options=df['route_name'].dropna().unique())
    
    # Bus type multiselect
    bustype = st.multiselect("Bus Type", df['bustype'].dropna().unique())

    # Combine bus name + seats
    df['bus_detail'] = df['busname'] + " - " + df['seats_available'].astype(str) + " seats"
    busname = st.multiselect("Bus Detail", df['bus_detail'].dropna().unique())

    # ✅ Handle max price safely
    max_price = int(float(df['price'].max())) if not df['price'].empty else 9999
    price_range = st.slider("Select Price Range", 0, max_price, (300, 1500))

    # Min rating
    min_rating = st.slider("Min Star Rating", 0.0, 5.0, 3.5)

# ✅ Apply filters
filtered_df = df.copy()

if bustype:
    filtered_df = filtered_df[filtered_df['bustype'].isin(bustype)]

# First convert to numeric
filtered_df['price'] = pd.to_numeric(filtered_df['price'], errors='coerce')
filtered_df = filtered_df.dropna(subset=['price'])


filtered_df = filtered_df[
    (filtered_df['price'] >= price_range[0]) & 
    (filtered_df['price'] <= price_range[1])
]

filtered_df['star_rating'] = pd.to_numeric(filtered_df['star_rating'], errors='coerce')
filtered_df = filtered_df.dropna(subset=['star_rating'])

filtered_df = filtered_df[filtered_df['star_rating'] >= min_rating]

# ✅ Show the result
st.subheader(f"🚌 Buses from {route}")
st.write(f"Showing {len(filtered_df)} buses matching filters")

st.dataframe(filtered_df)
