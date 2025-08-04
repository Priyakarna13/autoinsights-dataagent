# llm_agent.py
import os
from langchain_groq import ChatGroq

# For local dev, fallback to .env or system env
groq_api_key = os.getenv("GROQ_API_KEY")

# For Streamlit Cloud: read key from st.secrets
try:
    import streamlit as st
    if "GROQ_API_KEY" in st.secrets:
        groq_api_key = st.secrets["GROQ_API_KEY"]
except:
    pass

# Build Groq LLM with LLaMA3
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama3-8b-8192"
)

def ask_gpt(prompt: str) -> str:
    return llm.invoke(prompt)
