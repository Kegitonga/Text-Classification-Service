"""service.py - tiny Flask app that classifies text using a stub model
Install: pip install flask scikit-learn
"""
from flask import Flask, request, jsonify

app = Flask('text_classifier')

@app.route('/classify', methods=['POST'])
def classify():
    data = request.json or {}
    text = data.get('text','')
    # stub rules
    if 'refund' in text.lower():
        label = 'support'
    elif 'error' in text.lower() or 'bug' in text.lower():
        label = 'engineering'
    else:
        label = 'general'
    return jsonify({'label':label})

if __name__ == '__main__':
    app.run(port=8080)
