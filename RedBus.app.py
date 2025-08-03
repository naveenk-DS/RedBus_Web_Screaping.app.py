import streamlit as st
import pandas as pd
import io

st.title("🚌 Redbus India-wide Bus Viewer")

uploaded_file = st.file_uploader("Upload Redbus CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("CSV loaded successfully!")

    # Your filter and display logic below...
    st.dataframe(df)
else:
    st.warning("Please upload a redbus_data.csv file to view results.")

