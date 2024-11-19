from flask import Flask, request, jsonify, render_template
from generator import generate_text

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Optional web interface

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', '')
    max_length = data.get('max_length', 50)
    
    try:
        result = generate_text(prompt, max_length)
        return jsonify({"status": "success", "generated_text": result})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
