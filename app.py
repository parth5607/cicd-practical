from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to SentinelAI", "status": "running"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})
