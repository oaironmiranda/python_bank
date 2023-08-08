from conUser import *
from createTable import *
from verify import tryCode as random_generator
from verify import tryEmail

def insertData():
    con = user()
    insert = con.cursor()
    code = random_generator()
    
    name = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    password = input("Digite seu password: ")
    
    while tryEmail(email):
        print("Email already exists. Please enter your information again.")
        name = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        password = input("Digite seu password: ")
    
    sql = "INSERT INTO user (code, name, email, password) VALUES (%s, %s, %s, %s)"
    val = (code, name, email, password)
    insert.execute(sql, val)
    con.commit()
    createUserInfo(code)
    return print(f"User {code} added")
