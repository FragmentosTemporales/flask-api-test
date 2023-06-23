from flask import Blueprint, render_template, request, redirect
from models.product import Product
from utils.db import db

products = Blueprint("products", __name__)


@products.route("/products")
def home():
    return render_template("products.html")


@products.route("/products", methods=["POST"])
def add_product():
    product = Product()
    product.name = request.form["name"]
    product.brand = request.form["brand"]
    product.avatar = request.form["avatar"]
    print(product)
    db.session.add(product)
    db.session.commit()

    return redirect('/')


if __name__ == "__main__":
    print("Test unitarios para products.py")
