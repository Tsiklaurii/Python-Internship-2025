from flask import Blueprint, render_template

from src.models.product import Product

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/")
def index():
    products = Product.query.all()
    return render_template("main/index.html", products=products)


@main_blueprint.route("/about")
def about():
    return render_template("main/about.html")