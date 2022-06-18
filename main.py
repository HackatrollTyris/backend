from flask import Flask
import methods

app = Flask(__name__)

@app.route("/shops")
def get_shops():
    return "<p>Hello, World!</p>"

