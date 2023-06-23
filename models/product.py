from utils.db import db


class Product(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    brand = db.Column(db.String(50), nullable=False)
    avatar = db.Column(db.String(200), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "brand": self.name,
            "avatar": self.avatar,
        }
