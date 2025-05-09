# Nemosora: AI-Powered Research Assistant  
**Tagline:** *Recall. Refine. Radiate.*

Nemosora is a minimal and intelligent research assistant that helps users—especially students, researchers, and professionals—ask research-based questions and get concise, relevant answers.  
It uses LangChain, ChromaDB, and Gemini (Google's LLM) to retrieve and summarize information from categorized research documents.

---

## Features

- **Clean Streamlit UI**
- **Category-based filtering** (Engineering, Medical, Politics)
- **Semantic search using ChromaDB**
- **Response generation via Gemini (Gemini 1.5 Flash)**
- **Styled, readable output**
- **Query logging stored in SQLite**

---

## Technologies Used

- `Python`
- `Streamlit` - UI framework
- `LangChain` - Framework for LLM pipelines
- `ChromaDB` - Vector store for semantic retrieval
- `Gemini API (Google Generative AI)`
- `SQLite` - For logging user queries
- `dotenv` - To securely load API keys

---

## Folder Structure

AI Research Assistant/
├── main.py
├── db_logger.py
├── setup_db.sql
├── .env
├── .gitignore
├── requirements.txt
└── research data/
  ├── engineering/
  ├── medical/
  └── politics/

---

## How to Run

1. Clone the repository  
2. Create a `.env` file with your Gemini API key.
3. Create virtual environment:
```
python -m venv .venv
.venv\Scripts\activate
```
4. Install dependencies
   `pip install -r requirements.txt`
5. Run the app
   `streamlit run main.py`

### Credits
> Built as a final year project under internship guidance of developer @Workcohol

[Presenation](https://www.canva.com/design/DAGm7Xhlgm4/vukouUIlRHZOWu-CrC6sdQ/edit)
