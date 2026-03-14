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
⬇  
Streamlit Chat Interface  
⬇  
LangChain Retriever
⬇  
FAISS Vector Database
⬇  
Medical Knowledge Dataset (CSV)
⬇  
Groq LLM
⬇  
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

**Shravani Mugalikar**
AI | Machine Learning | Generative AI Enthusiast