"""  API that returns basic information"""

from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

email = os.getenv('EMAIL')
github_url = os.getenv('GITHUB_URL')

#CORS(app, resources={r"/api": {"origins": http://127.0.0.1:5000/}})
print(email)


@app.route("/", methods=['GET'])
def basic_info():
    """ method returns email, current datetime and github url"""
    current_datetime = datetime.utcnow().isoformat() + 'Z'
    data = {
        "email": email,
        "current time": current_datetime,
        "github url": github_url
    }
    return jsonify(data), 200
if __name__ == '__main__':
    app.run(debug=True)