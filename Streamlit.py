import streamlit as st
import pandas as pd

# Load final cleaned dataset
df = pd.read_csv("E:/RedBus_Scraper_App/final_busdetails.csv")

st.set_page_config(page_title="RedBus Search", layout="wide")
st.title("🚌 RedBus India - Bus Finder App")

# Extract states from Route_Name (Assuming Route format: 'From → To')
df['From'] = df['Route_name'].str.split('→').str[0].str.strip()
df['To'] = df['Route_name'].str.split('→').str[1].str.strip()
states = sorted(df['From'].dropna().unique().tolist())

# Sidebar filter options
st.sidebar.title("🔍 Filter Options")

selected_from = st.sidebar.selectbox("Select Departure City", states)
filtered_to = df[df['From'] == selected_from]['To'].dropna().unique().tolist()
selected_to = st.sidebar.selectbox("Select Destination City", filtered_to)

search_keyword = st.sidebar.text_input("Search by Bus Name (optional)")

# Filter dataset
filtered_df = df[(df['From'] == selected_from) & (df['To'] == selected_to)]

if search_keyword:
    filtered_df = filtered_df[filtered_df['Bus_Name'].str.contains(search_keyword, case=False, na=False)]

# Display matching buses
st.markdown(f"### 🚌 Matching Buses from **{selected_from}** to **{selected_to}**")
st.write(f"Total buses found: {len(filtered_df)}")

if len(filtered_df) == 0:
    st.warning("No buses found for this route.")
else:
    for i, row in filtered_df.head(10).iterrows():
        with st.container():
            st.markdown("---")
            st.subheader(f"🚌 {row['Bus_Name']} ({row['Bus_Type']})")
            st.markdown(f"""
            - 🕒 **Departure:** {row['Departing_Time']}
            - 🕓 **Arrival:** {row['Reaching_Time']}
            - ⏱️ **Duration:** {row['Duration']}
            - 💺 **Seats Available:** {row['Seats_available']}
            - 🌟 **Rating:** {row['Star_Rating'] if not pd.isna(row['Star_Rating']) else 'Not Rated'}
            - 💵 **Price:** ₹{int(row['Price'])}
            """)
            st.markdown(f"🔗 [Route Link]({row['Route_link']})")
