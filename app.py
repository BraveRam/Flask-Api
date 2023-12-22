from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def receive_message():
    data = request.get_json()
    received_message = data.get('message', '')    
    response_data = {'status': 'success', 'message': 'Message received successfully'}
    return jsonify(response_data)
