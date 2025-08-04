# app.py
import streamlit as st
import pandas as pd
from summarizer import generate_summary
from visualizer import plot_column
from sql_generator import generate_sql
from llm_agent import ask_gpt

st.set_page_config(page_title="AutoInsights", layout="wide")
st.title("AutoInsights: LLaMA 3 Data Assistant (Powered by Groq)")


uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])
if uploaded_file:
    df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)
    st.subheader("Data Preview")
    st.dataframe(df.head())

    if st.button("Generate Summary"):
        st.components.v1.html(generate_summary(df), height=800, scrolling=True)

    st.subheader("Ask a Question (SQL/Insights)")
    user_q = st.text_input("E.g., Show average revenue by category")

    if st.button("🔍 Analyze"):
        sql_query = generate_sql(user_q, "data", df.columns.tolist())
        st.write("SQL Query GPT-4 wrote:")
        st.code(sql_query, language="sql")

        # Just showing GPT result here (optional real SQL execution later)
        st.write("Answer:")
        st.write(ask_gpt(user_q))

    st.subheader("Visualization")
    col = st.selectbox("Select column to plot", df.columns)
    if st.button("Plot"):
        plot_column(df, col)
