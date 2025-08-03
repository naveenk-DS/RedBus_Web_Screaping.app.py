import os
import streamlit as st
import pandas as pd

st.title("🚌 Redbus India-wide Bus Viewer")

if os.path.exists("redbus_data.csv"):
    df = pd.read_csv("redbus_data.csv")
    # filtering and display logic here...
else:
    st.warning("redbus_data.csv not found. Please run redbus_scraper.py first to generate the data.")
