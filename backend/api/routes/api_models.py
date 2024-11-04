from ..extensions import api
from flask_restx import fields

book_model = api.model('Book', {
  'bid':fields.Integer,
  'book_name':fields.String,
  'author_name':fields.String,
  'book_price':fields.Float
})

book_input_model = api.model('Book', {
  'book_name':fields.String,
  'author_name':fields.String,
  'book_price':fields.Float
})