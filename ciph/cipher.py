# import ..database as base
# from ..database import db
import db as base



db = base.connecter()
cursor = db.cursor()


query = "SELECT * FROM cipher"
cursor.execute(query)
data = cursor.fetchall()

print(data)

# import os

# print(os.getcwd())


for user in data:
    d = ""
    e = user[1]
    n = user[2]
    print(n ," ===== " , e)
    # d = calculate_d(e, user)