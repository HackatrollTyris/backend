from flask import Flask
import methods

app = Flask(__name__)

@app.route("/districts")
def hello_world():
    return "<p>Hello, World!</p>"

