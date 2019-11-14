'''
    Module to serve the data from de database
'''
from flask import Flask, render_template

APP = Flask(__name__)

@APP.route("/")
def home():
    '''Server testing endpoint.'''
    return "Hello, World!"

@APP.route("/1-7")
def one_to_seven():
    '''Exposes 1 to 7 buttons.'''
    return render_template("1-7.html")

@APP.route("/8-14")
def eight_to_fourteen():
    '''Exposes 8 to 14 buttons.'''
    return render_template("8-14.html")

@APP.route("/1")
def c4_button():
    '''Exposes a note button.'''
    return render_template("button-note.html", note="c4", note_number="1")

@APP.route("/2")
def d4_button():
    '''Exposes a note button.'''
    return render_template("button-note.html", note="d4", note_number="2")

@APP.route("/3")
def e4_button():
    '''Exposes a note button.'''
    return render_template("button-note.html", note="e4", note_number="3")

@APP.route("/4")
def f4_button():
    '''Exposes a note button.'''
    return render_template("button-note.html", note="f4", note_number="4")

@APP.route("/5")
def g4_button():
    '''Exposes a note button.'''
    return render_template("button-note.html", note="g4", note_number="5")

@APP.route("/6")
def a4_button():
    '''Exposes a note button.'''
    return render_template("button-note.html", note="a4", note_number="6")

@APP.route("/7")
def g3_button():
    '''Exposes a note button.'''
    return render_template("button-note.html", note="g3", note_number="7")

@APP.route("/8")
def a3_button():
    '''Exposes a note button.'''
    return render_template("button-note.html", note="a3", note_number="8")

@APP.route("/9")
def b3_button():
    '''Exposes a note button.'''
    return render_template("button-note.html", note="b3", note_number="9")

@APP.route("/10")
def f3_button():
    '''Exposes a note button.'''
    return render_template("button-note.html", note="f3", note_number="10")

@APP.route("/11")
def e3_button():
    '''Exposes a note button.'''
    return render_template("button-note.html", note="e3", note_number="11")

@APP.route("/12")
def d3_button():
    '''Exposes a note button.'''
    return render_template("button-note.html", note="d3", note_number="12")

@APP.route("/13")
def a2_button():
    '''Exposes a note button.'''
    return render_template("button-note.html", note="a2", note_number="13")

@APP.route("/14")
def g2_button():
    '''Exposes a note button.'''
    return render_template("button-note.html", note="g2", note_number="14")

def serve():
    '''Exposes server to all interfaces.'''
    APP.run(host='0.0.0.0')

'''Entry point to serve the endpoints via poetry.'''
if __name__ == "__main__":
    APP.run(debug=True)
