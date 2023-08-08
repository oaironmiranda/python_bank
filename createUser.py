from conUser import *
from createTable import *
from verify import tryCode as random_generator
from verify import tryEmail

def insertData():
    con = user()
    insert = con.cursor()
    code = random_generator()
    
    while True:
        name = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        password = input("Digite seu password: ")

        if tryEmail(email) == 'False':

            sql = "INSERT INTO user (code, name, email, password) VALUES (%s, %s, %s, %s)"
            val = (code, name, email, password)
            insert.execute(sql, val)
            con.commit()
            createUserInfo(code)
            return print(f"User {code} added")
        
        
        else:
            print("Email already exists. Please enter your information again.")