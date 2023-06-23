from flask import Blueprint, render_template, request, redirect, url_for
from models.product import Product
from utils.db import db

products = Blueprint("products", __name__)


@products.route("/")
def home():
    products = Product.query.all()
    return render_template("products.html", products=products)


@products.route("/products", methods=["POST"])
def add_product():
    product = Product()
    product.name = request.form["name"]
    product.brand = request.form["brand"]
    product.avatar = request.form["avatar"]
    db.session.add(product)
    db.session.commit()

    return redirect(url_for('products.home'))


@products.route("/delete/<id>")
def delete(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    
    return redirect(url_for('products.home'))


@products.route("/update/<id>")
def update(id):
    print(id)
    return render_template("update.html")


if __name__ == "__main__":
    print("Test unitarios para products.py")
