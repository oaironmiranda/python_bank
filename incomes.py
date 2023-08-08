from login import *
from getUserData import getName
from verify import *

log = f"{login()}"
lLog = eval(log)
email, password = lLog

insertInTable(checkTable(getName(email, password)), "Incomes")