from project import db


class TestModel(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
