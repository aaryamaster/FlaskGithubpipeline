# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, CI/CD with Docker!"

@app.route('/health')
def health_check():
    return "OK"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
