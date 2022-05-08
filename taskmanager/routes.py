from flask import render_template
from taskmanager import app, db # noqa
from taskmanager.models import Category, Task # noqa


@app.route("/")
def home():
    """
    To render the base.html
    """
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    """
    To render the categories.html
    """
    return render_template("categories.html")


@app.route("/add_category", method=["GET", "POST"])
def add_category():
    """
    To render the add category
    """
    return render_template("add_category.html")
