"""  API that returns basic information"""

from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime, timezone
import os


app = Flask(__name__)  #creates flask instance


# get environment variables
email = os.getenv('EMAIL')
github_url = os.getenv('GITHUB_URL')

# Handle Cross Origin Resource Sharing for security
CORS(app, resources={r"/": {"origins": "*"}})

@app.route("/", methods=['GET'])   # app endpoint
def basic_info():
    """ method returns email, current datetime and github url"""
    current_datetime = (
        datetime.now(timezone.utc)   # datetime in iso format utc
        .isoformat()
        .replace("+00:00", "Z")
    )
    data = {
        "email": email,
        "current_datetime": current_datetime,
        "github_url": github_url
    }
    return jsonify(data), 200   

if __name__ == '__main__':
    app.run(debug=True)