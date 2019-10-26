'''
    Module to serve the data from de database
'''
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

def serve():
    app.run(host='0.0.0.0')

if __name__ == "__main__":
    app.run(debug=True)
