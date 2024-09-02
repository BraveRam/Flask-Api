from flask import Flask, request, jsonify
from OpsAi import Ai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#AI

@app.route('/ask', methods=['POST'])
def receive_message():
    data = request.get_json()
    recv = data.get('message', '')
    req = Ai(query=recv)
    res = req.chat()
    response_data = {'status': 'success', 'message': res}
    return jsonify(response_data)
