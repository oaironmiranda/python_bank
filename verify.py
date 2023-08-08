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