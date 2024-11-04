from flask_restx import Namespace, Resource
from ..extensions import db
from .api_models import book_model, book_input_model
from ..models.models import Book

ns = Namespace('api')

@ns.route('/books')
class BookAPI(Resource):
  @ns.marshal_list_with(book_model)
  def get(self):
    return Book.query.all()
  @ns.expect(book_input_model)
  @ns.marshal_with(book_model)
  def post(self):
    book = Book(book_name=ns.payload['book_name'], author_name=ns.payload['author_name'], book_price=ns.payload['book_price'])
    db.session.add(book)
    db.session.commit()
    return book, 201
  
@ns.route('/books/<book_name>')
class SearchBookAPI(Resource):
  @ns.marshal_with(book_model)
  def get(self, book_name):
    book = Book.query.filter_by(book_name=book_name).first()
    print(book)
    return book