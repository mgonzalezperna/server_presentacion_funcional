'''
    Module to serve the data from de database
'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

# @app.route("/test")
# def test():
#     return render_template("test.html")

# @app.route("/test-button")
# def testButton():
#     return render_template("test-button.html")

# @app.route("/1-to-5")
# def oneToFive():
#     return render_template("1-to-5.html")

# @app.route("/6-to-9")
# def sixToNine():
#     return render_template("6-to-9.html")

@app.route("/1-7")
def oneToSeven():
    return render_template("1-7.html")

@app.route("/8-14")
def eightToFourteen():
    return render_template("8-14.html")

@app.route("/1")
def c4Button():
    return render_template("button-note.html", note="c4", note_number="1" )

@app.route("/2")
def d4Button():
    return render_template("button-note.html", note="d4", note_number="2" )

@app.route("/3")
def e4Button():
    return render_template("button-note.html", note="e4", note_number="3" )

@app.route("/4")
def f4Button():
    return render_template("button-note.html", note="f4", note_number="4" )

@app.route("/5")
def g4Button():
    return render_template("button-note.html", note="g4", note_number="5" )

@app.route("/6")
def a4Button():
    return render_template("button-note.html", note="a4", note_number="6" )

@app.route("/7")
def g3Button():
    return render_template("button-note.html", note="g3", note_number="7" )

@app.route("/8")
def a3Button():
    return render_template("button-note.html", note="a3", note_number="8" )

@app.route("/9")
def b3Button():
    return render_template("button-note.html", note="b3", note_number="9" )

@app.route("/10")
def f3Button():
    return render_template("button-note.html", note="f3", note_number="10" )

@app.route("/11")
def e3Button():
    return render_template("button-note.html", note="e3", note_number="11" )

@app.route("/12")
def d3Button():
    return render_template("button-note.html", note="d3", note_number="12" )

@app.route("/13")
def a2Button():
    return render_template("button-note.html", note="a2", note_number="13" )

@app.route("/14")
def g2Button():
    return render_template("button-note.html", note="g2", note_number="14" )

def serve():
    app.run(host='0.0.0.0')

if __name__ == "__main__":
    app.run(debug=True)
