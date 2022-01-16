from cryptography.fernet import Fernet

'''
below code needs to be run only once to generate the key.key file. 

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)        

def view():
    with open('password_manager.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()

            name, password = data.split("-")
            print("User:", name, "- Password:",
                  fer.decrypt(password.encode()).decode())

def add():
    name = input("Enter the name: ").lower()
    password = input("Enter passsword: ").lower()

    with open("password_manager.txt", 'a') as f:
        f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")


while True:
    action = input("View or Add? or Q to Exit").lower()
    if action == 'q':
        break

    if action == "view":
        view()
    elif action == 'add':
        add()
    else:
        print("Enter valid details.")