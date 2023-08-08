import mysql.connector

def user():
    con = mysql.connector.connect(
        user='uxxcowaxmgkfjg6u',
        password='MZtIzMxQJ4ilrfPc9FdE',
        host='b8slne28tznwl2pk5osc-mysql.services.clever-cloud.com',
        database='b8slne28tznwl2pk5osc')
    return con

def userData():
    con = mysql.connector.connect(
        user='u9xxcwd52xgsbxhn',
        password='xAmpLSndXB0f8uXRlYSX',
        host='bqhycl6e8bf84nckajnv-mysql.services.clever-cloud.com',
        database='bqhycl6e8bf84nckajnv')
    return con