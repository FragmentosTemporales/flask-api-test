from flask import Flask, render_template
from routes.products import products
from routes.users import users
from flask_migrate import Migrate
from utils.db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(products)
app.register_blueprint(users)

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port="8080")