from flask import render_template, request, redirect, url_for
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


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """
    To render the add category
    """
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")
