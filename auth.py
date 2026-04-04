import firebase_admin
from firebase_admin import credentials, firestore

# 🔌 Initialize Firebase (only once)
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase_key.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()


# 👤 SIGNUP
def add_user(username, password):
    user_ref = db.collection("users").document(username)

    if user_ref.get().exists:
        return False   # user already exists

    user_ref.set({
        "username": username,
        "password": password
    })

    return True


# 🔐 LOGIN
def login_user(username, password):
    user_ref = db.collection("users").document(username)
    user = user_ref.get()

    if user.exists:
        data = user.to_dict()
        if data["password"] == password:
            return True

    return False