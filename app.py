from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"error": "No message provided"})

    url = 'http://localhost:11434/api/generate'
    data = {
        'model': 'qwen3:1.7b',
        'prompt': user_message,
        'stream': False
    }

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        generated_response = response.json()['response']
        return jsonify({"response": generated_response})
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to generate response", "details": str(e)})

if __name__ == '__main__':
    app.run(debug=True)