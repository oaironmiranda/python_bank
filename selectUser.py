from conUser import *

def selectData(code):
    con = user()
    mycursor = con.cursor()
    mycursor.execute(f"SELECT name, email FROM `user` WHERE `code` LIKE '{code}'")

    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)