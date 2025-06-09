from uuid import uuid4
from os import path
from flask import Blueprint, render_template, url_for, redirect
from flask_login import login_required

from src.views.product.forms import ProductForm
from src.models.product import Product
from src.config import Config
from src.utils import admin_required

product_blueprint = Blueprint("products", __name__)


@product_blueprint.route("/add_product", methods=["GET", "POST"])
@admin_required
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        file = form.image.data
        _, extension = path.splitext(file.filename)
        filename = f"{uuid4()}{extension}"
        file.save(path.join(Config.UPLOAD_PATH, filename))

        new_product = Product(name=form.name.data, author=form.author.data, price=form.price.data, image=filename)
        new_product.create()

        return redirect(url_for("main.index"))

    return render_template("product/create_product.html", form=form)


@product_blueprint.route("/edit_product/<int:id>", methods=["GET", "POST"])
@admin_required
def edit_product(id):
    product = Product.query.get(id)

    form = ProductForm(name=product.name, author=product.author, price=product.price)
    if form.validate_on_submit():
        product.name = form.name.data
        product.author = form.author.data
        product.price = form.price.data

        if form.image.data:
            file = form.image.data
            _, extension = path.splitext(file.filename)
            filename = f"{uuid4()}{extension}"
            file.save(path.join(Config.UPLOAD_PATH, filename))

            product.image = filename

        product.save()
        return redirect(url_for("main.index"))

    return render_template("product/create_product.html", form=form)


@product_blueprint.route("/delete_product/<int:id>")
@admin_required
def delete_product(id):
    product = Product.query.get(id)
    product.delete()

    return redirect(url_for("main.index"))


@product_blueprint.route("/view/<int:product_id>")
def view_product(product_id):
    chosen_product = Product.query.get(product_id)
    return render_template("product/view_product.html", product=chosen_product)
