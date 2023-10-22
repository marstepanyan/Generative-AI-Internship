from enum import Enum
from mongoengine import Document, StringField, FileField, ReferenceField


class User(Document):
    full_name = StringField(required=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
    role = StringField(required=True)


class Book(Document):
    name = StringField(required=True)
    author_name = StringField(required=True)
    tag = StringField(choices=['Python', 'C++', 'JavaScript', 'Java'], required=True)
    file = FileField()


class UserProfile(Document):
    user = ReferenceField(User, required=True)
    image = FileField()


class UserRole(Enum):
    NEW = 'new'
    STANDARD = 'standard'
    BANNED = 'banned'
    ADMIN = 'admin'
