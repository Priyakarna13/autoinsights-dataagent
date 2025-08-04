# visualizer.py
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def plot_column(df, column):
    fig, ax = plt.subplots()
    if df[column].dtype == "object":
        df[column].value_counts().plot(kind='bar', ax=ax)
    else:
        sns.histplot(df[column], ax=ax)
    st.pyplot(fig)
