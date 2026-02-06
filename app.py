import streamlit as st
import pandas as pd

st.set_page_config(page_title="Interactive Data Dashboard", layout="centered")

st.title("📊 Interactive Data Dashboard")
st.write("Virtual Internship Project")

# Load data
data = pd.read_csv("data.csv")

st.subheader("📁 Dataset Preview")
st.dataframe(data)

st.subheader("📈 Marks Visualization")
st.bar_chart(data.set_index("Name"))

st.subheader("📌 Insights")
st.write("• Student E has the highest marks.")
st.write("• Overall performance is good.")
