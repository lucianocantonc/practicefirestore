from google.cloud import firestore
from flask import Flask, jsonify, request
import os 

app = Flask(__name__)

db = firestore.Client()

@app.route('/save-user-info', methods=['POST'])
def save_user_info():
    
    data = request.get_json()

    db.collection('user').document(data['username']).set(data)

    response = {
        'message' : 'Thank You'
    }

    return jsonify(response), 200

if __name__ == '__main__':
    if os.environ.get('GAE_ENV') != 'standard':
        app.run(host='127.0.0.1', port=8080, debug=True)