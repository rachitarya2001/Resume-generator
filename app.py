from flask import Flask, request, render_template, send_file
import PyPDF2
import openai
import io

app = Flask(__name__)
openai.api_key = 'YOUR_OPENAI_API_KEY'  # Replace with your OpenAI API key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_resume():
    if 'pdf_file' not in request.files:
        return 'No file part', 400
    
    file = request.files['pdf_file']
    if file.filename == '':
        return 'No selected file', 400

    pdf_reader = PyPDF2.PdfFileReader(file)
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Convert this text into an HTML resume: {text}",
        max_tokens=1500
    )

    html_resume = response.choices[0].text
    
    return html_resume, 200, {'Content-Type': 'text/html'}

if __name__ == '__main__':
    app.run(debug=True)
