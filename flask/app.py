from flask import Flask
import os

PORT = os.environ.get('PORT', 8080)


app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask!'

app.run(host='0.0.0.0', port=PORT)