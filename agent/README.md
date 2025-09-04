# PDF Question Answering AI Agent

This project is a web-based AI agent that allows users to ask questions and receive answers based on the content of PDF documents. The application uses a Flask backend, OpenAI's GPT model for answering questions, and a simple HTML/JavaScript frontend.

## Features
- **PDF-based QA:** Answers user questions by referring to the content of PDFs in a specified folder.
- **Web Interface:** Clean, simple UI for asking questions and viewing answers.
- **OpenAI Integration:** Uses OpenAI's GPT model to generate answers based on PDF context.
- **Automatic PDF Text Extraction:** Extracts and searches text from all PDFs in the `pdf` folder.

## Project Structure
```
├── app.py                # Flask backend
├── requirements.txt      # Python dependencies
├── pdf/                  # Folder containing your PDF files
├── templates/
│   └── index.html        # Frontend HTML UI
└── README.md             # This file
```

## Setup Instructions

### 1. Clone the Repository
```
git clone <repo-url>
cd <repo-folder>
```

### 2. Place Your PDFs
- Create a folder named `pdf` in the project root (if it doesn't exist).
- Add your PDF files to the `pdf` folder.

### 3. Install Dependencies
Make sure you have Python 3.7+ installed. Then run:
```
pip install -r requirements.txt
```

### 4. Set Your OpenAI API Key
Export your OpenAI API key as an environment variable:
- **Windows (PowerShell):**
  ```powershell
  $env:OPENAI_API_KEY="your-openai-api-key"
  ```
- **Linux/macOS:**
  ```bash
  export OPENAI_API_KEY="your-openai-api-key"
  ```

### 5. Run the Application
```
python app.py
```

The app will start on [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Usage
1. Open your browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
2. Enter your question in the text area and click **Ask**.
3. The app will extract text from all PDFs in the `pdf` folder, find relevant context, and use OpenAI to answer your question.
4. The answer will be displayed below the form.

## How It Works
- The backend extracts text from all PDFs in the `pdf` folder using PyMuPDF.
- When a question is submitted, it searches for the most relevant chunk of text using a simple keyword overlap method.
- The question and the relevant context are sent to OpenAI's GPT model to generate an answer.
- The answer is returned and displayed in the web UI.

## Customization & Extensions
- **Semantic Search:** For better context retrieval, you can integrate embeddings (e.g., OpenAI Embeddings + FAISS/ChromaDB).
- **File Upload:** Add a file upload feature to allow users to add PDFs via the web UI.
- **Multi-user Support:** Add authentication and user-specific PDF storage if needed.

## Dependencies
- Flask
- PyMuPDF
- openai

## License
MIT License (add your own license as needed)
