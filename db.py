from pymongo import MongoClient
from werkzeug.security import generate_password_hash

client = MongoClient("mongodb+srv://magax1977:xagam7719@flask-chat-app-q7ywn.mongodb.net/test?retryWrites=true&w=majority")
chat_db = client.get_database("chatdb")
users_collection = chat_db.get_collection("users")


def save_user(username, email, password):
    password_hash = generate_password_hash(password)
    users_collection.insert_one({
        '_id': username,
        'email': email,
        'password': password_hash
    })


save_user('magax', 'magax@yandex.ru', '123456')