from ..extensions import db

class Book(db.Model):
  bid = db.Column(db.Integer, primary_key = True)
  book_name = db.Column(db.String(50))
  author_name = db.Column(db.String(50))
  book_price = db.Column(db.Float)