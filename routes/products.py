from flask import Blueprint, render_template, request, redirect, url_for, flash
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
    
    flash("Producto added succefully!")

    return redirect(url_for("products.home"))


@products.route("/delete/<id>")
def delete(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()

    flash("Product deleted succefully!")
    
    return redirect(url_for("products.home"))


@products.route("/update/<id>", methods=["POST", "GET"])
def update(id):
    product = Product.query.get(id)
    
    if request.method == 'POST':
        product.name = request.form["name"]
        product.brand = request.form["brand"]
        product.avatar = request.form["avatar"]
        
        db.session.commit()
        
        flash("Product update succefully!")
        
        return redirect(url_for("products.home"))
        
    return render_template("update.html", product=product)


if __name__ == "__main__":
    print("Test unitarios para products.py")
