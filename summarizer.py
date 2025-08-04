# summarizer.py
import pandas as pd
from ydata_profiling import ProfileReport

def generate_summary(df: pd.DataFrame) -> str:
    profile = ProfileReport(df, minimal=True)
    return profile.to_html()
