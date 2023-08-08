from login import *
from conUser import userData
from getUserData import getName

def check_table(table_name):
    con = userData()
    cursor = con.cursor()
    database = userData().database

    cursor.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %s AND table_name = %s", (database, table_name))

    if cursor.fetchone()[0] == 1:
        cursor.close()
        return True
    else:
        cursor.close()
        return False
    


'''if check_table(table_name):
    print(f"A tabela {table_name} existe.")
else:
    print(f"A tabela {table_name} não existe.")'''