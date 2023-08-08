from conUser import *

def createData():
    con = user()
    mycursor = con.cursor()
    mycursor.execute("""CREATE TABLE IF NOT EXISTS user (
                     code VARCHAR(255) NOT NULL,
                     name VARCHAR(255) NOT NULL, 
                     email VARCHAR(255) NOT NULL, 
                     password VARCHAR(255) NOT NULL CHECK(LENGTH(password) >=6), 
                     PRIMARY KEY (code))""")
    return print("Table created")

def createUserInfo(code):
    con = userData()
    mycursor = con.cursor()
    mycursor.execute(f"""CREATE TABLE IF NOT EXISTS {code}(
                     price VARCHAR(255) NOT NULL,
                     type VARCHAR(255) NOT NULL,
                     description VARCHAR(255) NOT NULL)""")
    return print(f"{code} table added")