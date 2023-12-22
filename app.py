from flask import Flask, request, jsonify
from OpsAi import Ai

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def receive_message():
    data = request.get_json()
    received_message = data.get('message', '')
    req = Ai(query=received_message)
    res = req.chat()
    response_data = {'status': 'success', 'message': res}
    return jsonify(response_data)
