from flask import Flask, request, jsonify, render_template
import os
import fitz  # PyMuPDF
import openai

app = Flask(__name__)

PDF_FOLDER = os.path.join(os.path.dirname(__file__), 'pdf')
openai.api_key = os.getenv('OPENAI_API_KEY')

# Helper: Extract text from all PDFs in the folder
def extract_text_from_pdfs(pdf_folder):
    all_text = ""
    for filename in os.listdir(pdf_folder):
        if filename.lower().endswith('.pdf'):
            filepath = os.path.join(pdf_folder, filename)
            doc = fitz.open(filepath)
            for page in doc:
                all_text += page.get_text()
            doc.close()
    return all_text

# Helper: Find relevant context (simple keyword search)
def find_relevant_context(text, question, max_length=1500):
    # Naive approach: return the chunk containing the most question keywords
    question_words = set(question.lower().split())
    best_chunk = text[:max_length]
    max_overlap = 0
    for i in range(0, len(text), max_length):
        chunk = text[i:i+max_length]
        overlap = sum(1 for word in question_words if word in chunk.lower())
        if overlap > max_overlap:
            best_chunk = chunk
            max_overlap = overlap
    return best_chunk

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question', '')
    if not question:
        return jsonify({'error': 'No question provided'}), 400
    # Extract text from PDFs
    pdf_text = extract_text_from_pdfs(PDF_FOLDER)
    # Find relevant context
    context = find_relevant_context(pdf_text, question)
    # Compose prompt
    prompt = f"Answer the following question based on the provided context from PDF documents.\n\nContext:\n{context}\n\nQuestion: {question}\nAnswer:"
    # Call OpenAI
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=256,
            temperature=0.2,
            n=1,
            stop=None
        )
        answer = response.choices[0].text.strip()
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True) 