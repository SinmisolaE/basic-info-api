"""  API that returns basic information"""

from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime
import os


app = Flask(__name__)



email = os.getenv('EMAIL')
github_url = os.getenv('GITHUB_URL')

CORS(app, resources={r"/": {"origins": https://basic-info-api-kgli.onrender.com/}})
print(email)


@app.route("/", methods=['GET'])
def basic_info():
    """ method returns email, current datetime and github url"""
    current_datetime = datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z")
    data = {
        "email": email,
        "current time": current_datetime,
        "github url": github_url
    }
    return jsonify(data), 200
if __name__ == '__main__':
    app.run(debug=True)