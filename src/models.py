
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name =db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    # favorite_character = db.relationship("Favorite_Character",backref ="user", lazy=True)

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email":self.email,
            # do not serialize the password, its a security breach
        }
    
class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    # height =db.Column(db.Integer, nullable=False)
    # mass =db.Column(db.Integer, nullable=False)
    # hair_color =db.Column(db.String(50), nullable=False)
    # skin_color =db.Column(db.String(50), nullable=False)
    # eye_color =db.Column(db.String(50), nullable=False)
    # gender =db.Column(db.String(50), nullable=False)
    # favorite_character =db.relationship("Favorite_Character", backref = "character", lazy=True)


    def __repr__(self):
        return '<Character %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # "height": self.height,
            # "hair_color": self.hair_color,
            # "skin_color": self.skin_color,
            # "eye_color": self.eye_color,
            # "gender": self.gender,
        }

            # do not serialize the password, its a security breach
        

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Planet %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Vehicle %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }




class Favorite_Character(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    character_id =db.Column(db.Integer, db.ForeignKey("character.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    
    def __repr__(self):
        return '<Favorite_Character %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "character_id": self.character_id,
            "user_id": self.user_id
        }


