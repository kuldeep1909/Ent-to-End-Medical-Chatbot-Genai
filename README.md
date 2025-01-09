# End-to-End Medical Chatbot with Generative AI

This project is an end-to-end medical chatbot powered by Generative AI. It leverages LangChain, Pinecone, and Hugging Face embeddings to provide accurate and context-aware responses to medical queries. The chatbot is built using Flask for the web interface and Groq for the language model.

## Features

- **Medical Query Handling**: The chatbot is designed to handle medical-related queries using a retrieval-augmented generation (RAG) approach.
- **Context-Aware Responses**: Utilizes Pinecone for vector storage and retrieval to provide contextually relevant answers.
- **User-Friendly Interface**: Built with Flask, the chatbot offers a simple and intuitive web interface for users to interact with.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.10
- Conda (for environment management)
- Pinecone API Key
- Groq API Key

## Installation

### Step 1: Clone the Repository

Clone the repository

```bash
Project repo: https://github.com/
```
### Step 02:  Create a cnda environment after opening the repository
```bash
conda create -n ragmed python=3.10 -y
```

```bash
conda activate ragmed
```

### Step 02 - Install the requirements
```bash
pip install -r requirements.txt
```
