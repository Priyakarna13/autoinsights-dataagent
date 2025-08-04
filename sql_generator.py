# sql_generator.py
from llm_agent import ask_gpt

def generate_sql(question: str, table_name: str, columns: list[str]) -> str:
    column_str = ", ".join(columns)
    prompt = f"""
    You are an expert SQL assistant. Given a table called `{table_name}` with columns: {column_str}
    Write an SQL query for the following question: {question}
    """
    return ask_gpt(prompt)
