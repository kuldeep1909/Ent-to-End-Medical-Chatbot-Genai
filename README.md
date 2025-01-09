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

```bash
git clone https://github.com/your-repo/End-to-End-Medical-Chatbot-Genai.git
cd End-to-End-Medical-Chatbot-Genai
```

### Step 2: Create a Conda Environment

```bash
conda create -n ragmed python=3.10 -y
conda activate ragmed
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables

Create a `.env` file in the root directory and add your API keys:

```plaintext
PINECONE_API_KEY=your_pinecone_api_key
GROQ_API_KEY=your_groq_api_key
```

## Running the Application

To start the Flask application, run:

```bash
python app.py
```

The application will be available at `http://0.0.0.0:8080`.

## Project Structure

```
End-to-End-Medical-Chatbot-Genai/
├── src/
│   ├── __init__.py
│   ├── helper.py
│   └── prompt.py
├── templates/
│   └── index.html
├── .env
├── requirements.txt
├── setup.py
├── app.py
├── README.md
└── research/
    └── trials.ipynb
```

## Usage

1. Open your web browser and navigate to `http://0.0.0.0:8080`.
2. Enter your medical query in the input box and press "Enter".
3. The chatbot will process your query and return a response.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **LangChain**: For the powerful framework enabling the RAG approach.
- **Pinecone**: For vector storage and retrieval.
- **Groq**: For the high-performance language model.
- **Hugging Face**: For the embeddings used in the project.

## Contact

For any questions or feedback, please contact [Kuldeep Malviya](mailto:malviyakuldeep38@gmail.com).
```

This `README.md` provides a comprehensive overview of your project, including installation instructions, usage, and project structure. It also includes sections for contributing, licensing, and acknowledgments.
