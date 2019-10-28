'''
    Module to serve the data from de database
'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/tone")
def tone():
    return render_template("Tone.js")

@app.route("/test-button")
def test_button():
    return render_template("piano.html")

def serve():
    app.run(host='0.0.0.0')

if __name__ == "__main__":
    app.run(debug=True)
