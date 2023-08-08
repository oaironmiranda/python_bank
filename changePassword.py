from verify import changePassword
from verify import tryEmail

email = input("Email: ")

while not tryEmail(email):
    email = input("Email: ")
else:
    password = input("Password: ")
    changePassword(email, password)