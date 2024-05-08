from pymongo import MongoClient
from werkzeug.security import generate_password_hash
from user import User
from datetime import datetime

client = MongoClient("mongodb+srv://user1:user1123@cluster0.atp6stl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

chat_db = client.get_database("ChatDB")
users_collection = chat_db.get_collection("chatApp")
messages_collection = chat_db.get_collection("messages")

def save_user(username, email, password):
    password_hash = generate_password_hash(password)
    users_collection.insert_one({'_id': username, 'email': email, 'password': password_hash})


def get_user(username):
    user_data = users_collection.find_one({'_id': username})
    return User(user_data['_id'], user_data['email'], user_data['password']) if user_data else None

'''def save_message(room_id, text, sender):
    messages_collection.insert_one({'room_id': room_id, 'text': text, 'sender': sender, 'created_at': datetime.now()})
'''