from flask import Blueprint, jsonify, request, current_app as app
import bcrypt
import jwt
from models import User, UserRole, Book

auth_routes = Blueprint('auth', __name__)


@auth_routes.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if 'email' not in data or 'password' not in data:
        return jsonify({'message': 'Email and password are required'}), 400

    user = User.objects(email=data['email']).first()
    if user:
        return jsonify({'message': 'Email already used'}), 409

    hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    new_user = User(
        full_name=data['full_name'],
        email=data['email'],
        password=hashed_password,
        role=UserRole.NEW.value
    )
    new_user.save()
    return jsonify({'message': 'Successfully added'}), 201


@auth_routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if 'email' not in data or 'password' not in data:
        return jsonify({'message': 'Email and password are required'}), 400

    user = User.objects(email=data['email']).first()
    if not user:
        return jsonify({'message': 'User not found'}), 401

    received_password = data['password'].encode('utf-8')

    if isinstance(user.password, bytes):
        stored_password = user.password
    else:
        stored_password = user.password.encode('utf-8')

    if bcrypt.checkpw(received_password, stored_password):
        token = jwt.encode({'email': user.email, 'role': user.role}, app.config['SECRET_KEY'])
        return jsonify({'token': token, 'user': {'full_name': user.full_name, 'role': user.role}})
    else:
        return jsonify({'message': 'Invalid password'}), 401


# Admin - Change User Role
@auth_routes.route('/admin/change_role', methods=['POST'])
def change_role():
    data = request.get_json()
    if 'email' not in data or 'new_role' not in data:
        return jsonify({'message': 'Email and new_role are required'}), 400

    user = User.objects(email=data['email']).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404

    if user.role == UserRole.ADMIN.value:
        return jsonify({'message': 'Admin role cannot be changed'}), 400

    if user.role == UserRole.NEW.value and data['new_role'] not in [UserRole.STANDARD.value, UserRole.BANNED.value]:
        return jsonify({'message': 'Invalid role change'}), 400

    if user.role == UserRole.STANDARD.value and data['new_role'] == UserRole.ADMIN.value:
        return jsonify({'message': 'Cannot promote to admin'}), 400

    user.role = data['new_role']
    user.save()
    return jsonify({'message': 'Role updated successfully'}), 200


# Admin - List All Users
@auth_routes.route('/admin/users', methods=['GET'])
def list_users():
    users = User.objects().exclude('password').to_json()
    return users, 200


# Admin - Add a Book
@auth_routes.route('/admin/books/add', methods=['POST'])
def add_book():
    data = request.get_json()

    name = data.get('name')
    author_name = data.get('author_name')
    tag = data.get('tag')

    new_book = Book(name=name, author_name=author_name, tag=tag)
    new_book.save()

    return jsonify({'message': 'Book added successfully'}), 201


# Admin - Delete a Book
@auth_routes.route('/admin/books/delete/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.objects(id=book_id).first()

    if book:
        book.delete()
        return jsonify({'message': 'Book deleted successfully'}), 200
    else:
        return jsonify({'message': 'Book not found'}), 404
