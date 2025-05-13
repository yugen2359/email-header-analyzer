from flask import Flask, render_template, request, jsonify
import os  # Added to read PORT from environment

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    header = request.json.get('header', '')
    lines = header.split('\n')
    result = {}

    for line in lines:
        if line.startswith('From:'):
            result['from'] = line[5:].strip()
        elif line.startswith('To:'):
            result['to'] = line[3:].strip()
        elif line.startswith('Subject:'):
            result['subject'] = line[8:].strip()
        elif line.startswith('Date:'):
            result['date'] = line[5:].strip()
        elif line.startswith('Message-ID:'):
            result['message_id'] = line[11:].strip()
        elif line.startswith('Return-Path:'):
            result['return_path'] = line[12:].strip()
        elif line.startswith('Received:'):
            result.setdefault('received', []).append(line[9:].strip())

    return jsonify(result)

if __name__ == '__main__':
    # Bind to 0.0.0.0 and use dynamic port for Render deployment
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
