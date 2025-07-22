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

if __name__ == '__main__':
    app.run(debug=True)
