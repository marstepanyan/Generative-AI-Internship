from flask import Blueprint, jsonify, request
from models import Book
from bson import ObjectId


book_routes = Blueprint('books', __name__)


@book_routes.route('/books', methods=['GET'])
def list_books():
    books = Book.objects()
    # Convert the QuerySet to a list of dictionaries and stringify the ObjectId
    book_list = [book.to_mongo().to_dict() for book in books]
    for book in book_list:
        book['_id'] = str(book['_id'])  # Convert ObjectId to string
    return jsonify(book_list)


@book_routes.route('/books/filter', methods=['GET'])
def filter_books():
    author = request.args.get('author_name')
    tag = request.args.get('tag')

    if author:
        print(author)
        books = Book.objects(author_name=author)
    elif tag:
        books = Book.objects(tag=tag)
    else:
        books = []  # Create an empty list if neither 'author' nor 'tag' is provided.

    return jsonify(books)


@book_routes.route('/books/<book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.objects(id=ObjectId(book_id)).first()  # Convert book_id to ObjectId
    if book:
        # Convert the Book object to a dictionary
        book_dict = book.to_mongo().to_dict()

        # Convert ObjectId fields to string in the dictionary
        book_dict['_id'] = str(book_dict['_id'])

        return jsonify(book_dict)
    else:
        return jsonify({'message': 'Book not found'}), 404


@book_routes.route('/books/upload', methods=['POST'])
def upload_book():
    data = request.form
    name = data.get('name')
    author_name = data.get('author_name')
    tag = data.get('tag')
    uploaded_file = request.files['file']

    book = Book(name=name, author_name=author_name, tag=tag, file=uploaded_file.read())
    book.save()
    return jsonify({'message': 'Book uploaded successfully'}), 201
