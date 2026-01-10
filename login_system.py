import json 
import hashlib

#load the file
def load_data():
    file = open("users.json")
    users = json.load(file)
    file.close()
    return users

def save_data(users):
    with open("users.json", "w") as file:
        json.dump(users, file)

def register_users(users):
    username = input("Username: ")
    while username in users:
        print("Username is taken.")
        print("Username: ")

    password = input("Password: ") 
    #turns the string into bytes for hashing 
    password_bytes = password.encode('utf-8')

    #creats the hash obj
    hashed_password = hashlib.sha256(password_bytes).hexdigest()
    users[username] = hashed_password
    save_data(users)
    print("Regisered successfully!")

    



    
    
    



    
    
    