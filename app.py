from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/',methods=["GET"])
def hello():
    return "Hello world"
@app.route('/add', methods=['POST'])
def add1():
    # print("Received Body:", request.data)
    print("Received Headers:", request.headers.get('Content-Type'))
    if request.headers.get('Content-Type') != 'application/json; charset=utf-8':
        return jsonify({'error': 'Content-Type must be application/json'}), 400

    try:
        data = request.get_json()
        if data is None:
            return jsonify({'error': 'Invalid JSON data'}), 400

        return jsonify({'message': 'Success', 'received_data': data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
