import json

users = {1: {"name": "Ali", "age": "20"},2: {"name": "Mohsen", "age": "22"}}

def save(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

def load_users():
    with open("users.json", "r") as file:
        return json.load(file)

def add():
    users = load_users()
    users["3"] = {"name": "Ahmad","age": "14"}
    save(users)

save(users)

users = load_users()
print(users)

add()

users = load_users()
print(users)