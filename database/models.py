from .database import db


class User(db.Document):
    name = db.StringField(required=True)
