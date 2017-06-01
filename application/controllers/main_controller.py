from flask import Blueprint, render_template

blueprint = Blueprint("MainController", __name__)


@blueprint.route("/")
def index():
    return render_template("page.html.jinja2", context={"title": "Welcome"})
