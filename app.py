
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---- CUSTOM CSS ----
st.markdown("""
<style>
/* Main background */
.main {
    background-color: #f5f7fa;
}

/* Title styling */
h1 {
    color: #2c3e50;
    text-align: center;
}

/* Sidebar styling */
section[data-testid="stSidebar"] {
    background-color: #1f2933;
}

section[data-testid="stSidebar"] h1, 
section[data-testid="stSidebar"] label {
    color: white;
}

/* Dataframe */
[data-testid="stDataFrame"] {
    background-color: white;
    border-radius: 10px;
}

/* Buttons */
.stButton > button {
    background-color: #2563eb;
    color: white;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)


# Page config
st.set_page_config(page_title="Student Dashboard", layout="wide")

# Load data
data = pd.read_csv("data.csv")

# ---- SIDEBAR NAVIGATION ----
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Overview", "Visual Analysis", "Summary & Feedback"]
)

# ---- PAGE 1: OVERVIEW ----
if page == "Overview":
    st.title("📊 Student Performance Dashboard")
    st.markdown("### 📌 Dataset Preview")
    st.caption("This dashboard helps analyze student performance interactively.")

    st.subheader("Overview Page")

    st.write("This page provides an overview of the dataset.")
    st.dataframe(data)

# ---- PAGE 2: VISUAL ANALYSIS ----
elif page == "Visual Analysis":
    st.title("📈 Visual Analysis")

    col1, col2 = st.columns([1, 2])

    with col1:
        min_marks = st.slider(
            "🎯 Select Minimum Marks",
            int(data["Marks"].min()),
            int(data["Marks"].max()),
            int(data["Marks"].min())
        )

    filtered_data = data[data["Marks"] >= min_marks]

    with col2:
        fig, ax = plt.subplots()
        ax.bar(filtered_data["Name"], filtered_data["Marks"])
        ax.set_xlabel("Student")
        ax.set_ylabel("Marks")
        st.pyplot(fig)


# ---- PAGE 3: SUMMARY & FEEDBACK ----
elif page == "Summary & Feedback":
    st.title("📝 Summary & Feedback")
    st.write("This page shows summary statistics and user feedback.")

    st.subheader("📊 Summary Statistics")
    st.write(data.describe())

    feedback = st.text_area("Enter your feedback or observations:")
    if feedback:
        st.success("Thank you for your feedback!")
        st.write(feedback)



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

# Feedback section
feedback = st.text_area("✍️ Enter your feedback")

if feedback:
    st.success("Thank you for your feedback!")
    st.write(feedback)