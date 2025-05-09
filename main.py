import streamlit as st
import os
from dotenv import load_dotenv
from db_logger import init_db, log_query
import sqlite3
from datetime import datetime
from langchain_community.document_loaders import PyPDFLoader

from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema.runnable import Runnable

load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

init_db()

#Streamlit UI
st.set_page_config(page_title="Nemosora", layout="wide")
st.title("Nemosora: AI Research Assistant")

st.markdown("---")

selected_category = st.selectbox("Choose a category", ["engineering", "medical", "politics"])
query = st.text_input("What do you want to know?")


if st.button("Search"):
    if not query:
        st.warning("Please enter a query.")
    else:
        st.info("Processing your request...")

        #Loading documents
        docs = []
        category_path = os.path.join("research data", selected_category)
        for filename in os.listdir(category_path):
            if filename.endswith(".txt"):
                loader = TextLoader(os.path.join(category_path, filename))
                docs.extend(loader.load())

        if not docs:
            st.error("No documents found in the selected category.")
        else:
            splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            chunks = splitter.split_documents(docs)

            embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GEMINI_KEY)
            vectordb = Chroma.from_documents(chunks, embedding, persist_directory="vector_store")

            retriever = vectordb.as_retriever()
            model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.4, google_api_key=GEMINI_KEY)
            qa_chain: Runnable = RetrievalQA.from_chain_type(llm=model, retriever=retriever)

            result = qa_chain.invoke({"query": query})
            answer = result["result"]

            st.markdown("### Here's what I found:")
            st.markdown(
                f"""
                <div style='background-color: #d1f5d3; padding: 15px; border-radius: 10px; color: #1e4b2e;'>
                    {answer}
                </div>
                """,
                unsafe_allow_html=True
            )

            log_query(query, selected_category, answer)