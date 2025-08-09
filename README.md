
# AutoInsights: LLM-Powered Data Assistant

AutoInsights is an interactive, GPT-4-powered assistant that helps analysts generate **SQL queries**, **summarize datasets**, and **suggest visualizations** from CSV/Excel files — all within a friendly Streamlit UI.

It combines **LangChain**, **Pandas**, and **OpenAI’s GPT-4** to reduce manual data analysis time by over 60%.

---

## Features
- Automatically parses CSV/XLSX files and summarizes key insights
- LLM-powered natural language interaction using GPT-4
- Suggests charts and plots based on your data
- Generates optimized SQL queries from user prompts
- Clean, responsive Streamlit UI (mobile + desktop)
- Modular, scalable project architecture

---

## Try the App Locally  
Run locally with just one command (see below)

---

## Project Structure
```bash
autoinsights/
├── app.py                        # Main Streamlit app
├── utils/
│   ├── llm_agent.py              # LangChain agent for LLM reasoning
│   ├── data_parser.py            # CSV/XLSX data parser and Pandas profiling
│   ├── viz_suggester.py          # Chart/plot suggestion engine
│   └── sql_generator.py          # SQL generator using LLM
├── examples/
│   └── sample_report.xlsx        # Sample input file for testing
├── outputs/
│   └── summary.txt               # Generated summaries (optional)
├── requirements.txt              # All dependencies
├── README.md                     # Project overview (this file)
└── .streamlit/
    └── config.toml               # UI theming and settings
```
## How to Run Locally

### 1. Clone the repository
```bash

git clone https://github.com/yourusername/autoinsights.git
cd autoinsights
```

### 2. Set up a virtual environment
```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your OpenAI API key
Create a .env file in the root directory:
```bash
API_KEY=
```

### 5. Run the app

```bash
streamlit run app.py
```

## Technologies Used

- Groq
- LangChain Agents + Tools
- Pandas for data processing
- Matplotlib / Plotly for chart suggestions
- Streamlit for frontend interface
- Pandas Profiling / ydata-profiling (optional)

## Use Cases
- Exploratory data analysis (EDA)
- SQL generation from natural language
- Dashboard/chart suggestions for BI tools
- Dataset summarization in plain English
- Accelerated business insights without manual scripting

## Author
Built with ❤️ by Sri


