from flask import Blueprint, render_template

users = Blueprint("users", __name__)


@users.route("/users")
def home():
    return render_template("users.html")


if __name__ == "__main__":
    print("Test unitarios para users.py")
