from conUser import *

def getData():
    con = user()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM user")
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)

def getName(email, password):
    con = user()
    cursor = con.cursor()

    query = "SELECT code FROM user WHERE email = %s AND password = %s"
    cursor.execute(query, (email, password))
    
    myresult = cursor.fetchall()
    for x in myresult:
         return str(x[0])