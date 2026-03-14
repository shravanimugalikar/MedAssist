# MedAssist (LangChain + RAG)

An AI-powered healthcare chatbot that answers medical questions using a **Retrieval-Augmented Generation (RAG)** pipeline.  
The system retrieves information from a medical PDF knowledge base and generates context-aware responses using an LLM.

Built using **LangChain, vector embeddings, and a vector database** to provide accurate and contextual health-related information.

---

#  Features

- AI-powered healthcare question answering
- Retrieval-Augmented Generation (RAG)
- Medical knowledge extracted from PDF
- Vector search for relevant medical context
- Interactive chatbot interface
- Modular architecture for easy scaling

---

#  Project Architecture
User Query
↓
LangChain Retriever
↓
Vector Database (Medical Knowledge)
↓
Relevant Context
↓
LLM
↓
AI Response

---

# How It Works

- Medical PDF is loaded
- Text is split into chunks
- Chunks are converted into vector embeddings
- Stored in a vector database
- User query retrieves relevant chunks
- LLM generates response using retrieved context

---

# Technologies Used

- Python
- LangChain
- Streamlit
- Vector Databases
- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)

---

# Author

**Shravani Mugalikar**