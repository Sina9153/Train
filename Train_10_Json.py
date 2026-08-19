import json
users={1:{"name":"Ali","age":"20"},2:{"name":"Mohsen","age:":"22"}}
with open("users.json","w") as file:
    json.dump(users,file)
with open("users.json","r") as file:
    json.load(file)