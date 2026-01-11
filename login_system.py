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
        new_username = input("Username: ")
        username = new_username 

    password = input("Password: ") 
    #turns the string into bytes for hashing 
    password_bytes = password.encode('utf-8')

    #creats the hash obj
    hashed_password = hashlib.sha256(password_bytes).hexdigest()
    users[username] = hashed_password
    save_data(users)
    print("Regisered successfully!")

def login_user(users):
    username = input("Enter username: ")
    while username not in users:
        print("Invalid username or password.")
        new_username = input("Username: ")
        username = new_username 


    password = input("Password: ") 
    password_bytes = password.encode('utf-8')
    hashed_password = hashlib.sha256(password_bytes).hexdigest()

    if users[username] == hashed_password:
        print("Login successful! ")
        return True
    
    else:
        print("Invalid username or password. ")
        return False





    



    
    
    



    
    
    