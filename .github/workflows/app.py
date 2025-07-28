from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask!'

@app.route('/signup', methods=['POST'])
def signUp():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': 'Username and password required'}), 400
    # Here you would normally add logic to save the user to a database
    return jsonify({'message': f'User {username} signed up successfully!'}), 201

@app.route('/testing', methods=['GET'])
def testing():
    return jsonify({'message': 'Testing endpoint reached! OMG'}), 200

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello from the new endpoint!'}), 200

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'pong'})

@app.route('/status', methods=['GET'])
def status():
    return jsonify({'status': 'ok', 'service': 'dummy'})

@app.route('/user/<username>', methods=['GET'])
def get_user(username):
    return jsonify({'user': username, 'info': 'dummy user info'})

if __name__ == '__main__':
    app.run(debug=True)
