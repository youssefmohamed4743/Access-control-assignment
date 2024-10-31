users = {
    "admin": {"password": "admin12", "role": "admin"},
    "user": {"password": "user12", "role": "user"},
}

def check_access(user, password):
    if user in users and users[user]["password"] == password:
        return users[user]["role"]
    else:
        return None


def roles():
    name = input("Enter your Username")
    password = input("Enter your Password")
    role = check_access(name,password)
    if role:
        print(f"Access for {role}")
        while True:
            command = speech_recognize()
            if command:
                if role == "admin":
                    if command == "shutdown":
                        print("shutting down...")
                    else:
                        print("Unknown Command")
                elif role == "user":
                    if command == "add":
                        print("Adding profile...")
                    else:
                        print("Unknown command")
    else:
        print("denied access")