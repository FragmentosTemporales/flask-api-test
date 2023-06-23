from utils.db import db

class Rol(db.Model):
    __tablename__ = 'rol'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    user = db.relationship("User", back_populates="rol", overlaps="user")
    
    def serialize(self):
        return {
            "id" : self.id,  
            "name" : self.name,
            "user" : [user.serialize() for user in self.user],
        }
        
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True )
    name = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(9), nullable=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    rol_id = db.Column(db.Integer, db.ForeignKey('rol.id'), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "email": self.email,
            "phone": self.phone
        }

class Product(db.Model):
    __tablename__='product'

    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    brand = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    first_url = db.Column(db.String(200), nullable=False)
    second_url = db.Column(db.String(200), nullable=False)
    third_url = db.Column(db.String(200), nullable=False)
    rol_id = db.Column(db.Integer, db.ForeignKey('rol.id'), nullable=False)
    