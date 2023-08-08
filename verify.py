from conUser import *
from randomCode import random_generator
from getUserData import getName

def tryCode():
    # Conecte-se ao banco de dados MySQL
    cnx = user()
    cursor = cnx.cursor()

    # Substitua 'your_table' e 'code_column' pelos nomes apropriados da sua tabela e coluna
    query = "SELECT 1 FROM user WHERE code = %s"
    code = random_generator()

    # Execute a consulta
    cursor.execute(query, (code,))

    while cursor.fetchone():
        # Se o código existir, gere um novo código
        code = random_generator()
        cursor.execute(query, (code,))

    # Feche a conexão com o banco de dados
    cursor.close()
    cnx.close()

    return code

def tryEmail(email):
    cnx = user()
    cursor = cnx.cursor()

    # Substitua 'your_table' e 'code_column' pelos nomes apropriados da sua tabela e coluna
    query = "SELECT * FROM user WHERE email = %s"
    checkEmail = email

    cursor.execute(query, (checkEmail,))
    
    if cursor.fetchone():
        cursor.close()
        cnx.close()
        return True
    else:
        cursor.close()
        cnx.close()
        return False
    
def tryLogin(email, password):
    cnx = user()
    cursor = cnx.cursor()

    query = "SELECT * FROM user WHERE email = %s AND password = %s"
    cursor.execute(query, (email, password))
    result = cursor.fetchone()
    cursor.close()
    cnx.close()

    if result:
        getName(email, password)
        return True
    else:
        print("Repeat Information")
        return False

def changePassword(email, password):
    cnx = user()
    cursor = cnx.cursor()

    sql = "UPDATE user SET password = %s WHERE email = %s"
    val = (password, email)
    cursor.execute(sql, val)

    cnx.commit()

    return print("New Password updated")

def checkTable(code):
     
    con = userData()
    cursor = con.cursor()
    database = userData().database

    cursor.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %s AND table_name = %s", (database, code))
    if cursor.fetchone()[0] == 1:
        cursor.close()
        return code
    else:
        cursor.close()
        return print(f"A tabela {code} não existe.")
    
def insertInTable(code, where):
    con = userData()
    insert = con.cursor()

    price = input("Price: ")
    typo = where
    desc = input("Description: ")
    date = int(input("Date: "))
    month = int(input("Month: "))
    year = int(input("Year: "))

    sql = "INSERT INTO %s (price, type, description, date, month, year) VALUES (%s, %s, %s, %s, %s, %s)" % (code, '%s', '%s', '%s', '%s', '%s', '%s')
    val = (price, typo, desc, date, month, year)
    insert.execute(sql, val)
    con.commit()

    return print(f"{desc} from date {date}/{month}/{year}\nwith the value {price} has been added to {typo} in table {code}")
