from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for local testing

@app.route('/')
def index():
    return render_template('index.html')  # Render the frontend

@app.route('/analyze', methods=['POST'])
def analyze_email():
    data = request.get_json()
    email_text = data.get('email_text', '')

    suspicious_phrases = [
        'verify your account', 'urgent', 'click here', 
        'login', 'password', 'update your information', 
        'you have been selected', 'act now', 'risk'
    ]

    found_phrases = [phrase for phrase in suspicious_phrases if phrase in email_text.lower()]
    suspicious_links = [word for word in email_text.split() if word.lower().startswith('http')]

    return jsonify({
        'found_phrases': found_phrases,
        'suspicious_links': suspicious_links
    })

if __name__ == '__main__':
    app.run(debug=True)
