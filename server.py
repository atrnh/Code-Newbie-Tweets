import os
from flask import Flask, render_template

from secrets import keys
from config import DB_URI, HOST, PORT
from util.connect import connect_to_db


app = Flask(__name__)
app.secret_key = keys["flask_key"]
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


@app.route("/")
def index():
    """Index."""

    # TODO: Make the homepage more sensible

    return render_template("todo.html")


@app.route("/api/pins")
def get_pins():
    """Get all pins."""

    # TODO: Finish this

    return render_template("todo.html")


@app.route("/api/pin", methods=["POST"])
def create_pin():
    """Create a pin."""

    # TODO: Finish this

    return render_template("todo.html")


if __name__ == "__main__":
    app.debug = True
    app.run(host=HOST, port=PORT)
