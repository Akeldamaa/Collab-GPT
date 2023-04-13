from flask import Flask, render_template, request, jsonify
import openai
import os

# Set up OpenAI API key
openai.api_key = os.environ.get('OPENAI_API_KEY')

# Initialize Flask app
app = Flask(__name__)

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint for generating text
@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    response = openai.Completion.create(
        engine='davinci',
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return jsonify({'text': response.choices[0].text})

if __name__ == '__main__':
    app.run(debug=True)
