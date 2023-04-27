from db import db


class TodoModel(db.Model):
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(256), nullable=False)
    status = db.Column(db.String(40), nullable=False)