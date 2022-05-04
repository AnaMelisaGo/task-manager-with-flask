from flask import render_template
from taskmanager import app, db # noqa


@app.route("/")
def home():
    """
    To render the base.html
    """
    return render_template("base.html")
