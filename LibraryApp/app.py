from flask import Flask
from flask_pymongo import PyMongo
import mongoengine
from authentication import auth_routes
from book import book_routes

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/my_database'
app.config['SECRET_KEY'] = 'your_secret_key'
mongo = PyMongo(app)
mongoengine.connect(db='my_database', host='mongodb://localhost:27017')

# Register routes from other files
app.register_blueprint(auth_routes)
app.register_blueprint(book_routes)

if __name__ == '__main__':
    app.run(debug=True)
