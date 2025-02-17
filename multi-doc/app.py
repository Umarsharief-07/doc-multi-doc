from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! Welcome to my website!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
