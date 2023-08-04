from flask import Flask, request, jsonify
from processor import chatbot_response

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data['message']

    response = chatbot_response(message)

    return jsonify({'response': response})

if __name__ == '__main__':
    # Replace '0.0.0.0' with your machine's IP address
    app.run(host='0.0.0.0', debug=True)
