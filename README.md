# MedAssist (LangChain + RAG)

MedAssist AI is an AI-powered healthcare chatbot that answers medical questions using a Retrieval-Augmented Generation (RAG) pipeline.

The system retrieves relevant medical information from a structured medical dataset and generates context-aware responses using a Large Language Model (LLM).

This project is built using LangChain, HuggingFace embeddings, FAISS vector database, Groq LLM, and Streamlit to provide fast and contextual health-related responses.

---

#  Features

- AI-powered healthcare assistant
- Retrieval-Augmented Generation (RAG)
- Medical knowledge retrieval from dataset
- HuggingFace embeddings for semantic search
- FAISS vector database for fast similarity search
- Groq-powered LLM responses
- Interactive chatbot interface using Streamlit
- Modular and scalable architecture

---

#  Project Architecture


User Query  
⬇️  
Streamlit Chat Interface  
⬇️  
LangChain Retriever  
⬇️  
FAISS Vector Database  
⬇️  
Medical Knowledge Dataset (CSV)  
⬇️  
Groq LLM  
⬇️  
AI Response

---

# How It Works

- The medical dataset (CSV) is loaded.
- The text is split into smaller chunks.
- Chunks are converted into vector embeddings using HuggingFace models.
- The embeddings are stored in a FAISS vector database.
- When a user asks a question, the system retrieves the most relevant medical information.
- The retrieved context is passed to a Groq LLM.
- The LLM generates a context-aware healthcare response.

---

## Dependencies

This project was built using the following key libraries:

- Python 3.11
- langchain >= 0.2.0
- langchain-community >= 0.2.0
- langchain-groq >= 0.1.0
- sentence-transformers >= 2.6.0
- faiss-cpu >= 1.7.4
- streamlit >= 1.32.0
- pandas >= 2.0.0
- python-dotenv >= 1.0.0

All required libraries and versions are listed in `requirements.txt`.

Install them using:
pip install -r requirements.txt 


---

# Technologies Used

- Python
- LangChain
- Groq API
- HuggingFace Embeddings
- FAISS Vector Database
- Streamlit
- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)

---

**Author**

Developed by **Shravani Mugalikar**

AI | Machine Learning | Generative AI Enthusiast