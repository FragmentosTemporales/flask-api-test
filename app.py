from flask import Flask
from routes.products import products
from models.models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

app.register_blueprint(products)

if __name__ == "__main__":
    app.run(debug=True)