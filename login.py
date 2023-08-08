from verify import tryLogin

def login():
    email = input("Email: ")
    password = input("Password: ")

    while not tryLogin(email, password):
        email = input("Email: ")
        password = input("Password: ")

    return email, password