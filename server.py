import os

from flask import (Flask, jsonify, render_template)
from sqlalchemy import desc

from secrets import keys


DEFAULT_DB_URI = "postgresql:///pinbored"
DEFAULT_LISTEN_HOST = "127.0.0.1"
DEFAULT_LISTEN_PORT = "5000"

app = Flask(__name__)
app.secret_key = keys["flask_key"]


DB_URI = os.environ.get(
    'FLASK_DB_URI',
    DEFAULT_DB_URI,
)
LISTEN_HOST = os.environ.get(
    'FLASK_LISTEN_HOST',
    DEFAULT_LISTEN_HOST,
)
LISTEN_PORT = int(os.environ.get(
    'FLASK_LISTEN_PORT',
    DEFAULT_LISTEN_PORT,
))


@app.route("/")
def index():
    """Index."""

    # TODO: Make the homepage more sensible

    return render_template("home.html")


@app.route("/about")
def about():
    """About page."""

    return render_template("about.html")


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
    connect_to_db(app, DB_URI)
    app.run(host=LISTEN_HOST, port=LISTEN_PORT)

