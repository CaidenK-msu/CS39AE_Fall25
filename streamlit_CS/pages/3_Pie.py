import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.title("🥧 Interactive Pie Chart")

chart_title = st.text_input("Chart title", value="My Budget Breakdown")

st.write("Upload a CSV (columns: Label, Value) or use the example at data/pie_demo.csv.")
uploaded = st.file_uploader("CSV file", type=["csv"])

#Should load uploaded CSV file or the example file from the repo
if uploaded is not None:
    df = pd.read_csv(uploaded)
else:
    path = Path("data") / "pie_demo.csv"
    if not path.exists():
        st.error("Missing data/pie_demo.csv. Create it first.")
        st.stop()
    df = pd.read_csv(path)

#Validation
if not {"Label", "Value"}.issubset(df.columns):
    st.error("CSV must contain columns: Label, Value")
    st.dataframe(df.head())
    st.stop()

with st.expander("Preview / edit data"):
    df = st.data_editor(df, num_rows="dynamic")

fig = px.pie(df, names="Label", values="Value", title=chart_title)
st.plotly_chart(fig, use_container_width=True)

st.caption("Tip: edit numbers above or change the title; refresh/rerun to see updates.")
