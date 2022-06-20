import sqlite3

from sqlalchemy.engine import cursor

con = sqlite3.connect("supermarket.db")
cursor = con.cursor()
cursor.execute('''create table if not exists Gadgets
 (id INTEGER PRIMARY KEY AUTOINCREMENT, name text UNIQUE  , quantity integer, price integer ) ''')
products = [(1, "HP-AE12", 100, 25000),
            (2, "DELL", 100, 35000),
            (3, "ASUS", 100, 28000),
            (4, "APPLE", 100, 60000),
            (5, "ACER", 100, 24000),
            (6, "SAMSUNG", 100, 35000),
            (7, "OPPO", 100, 15000),
            (8, "XAOMI", 100, 45000),
            (9, "HUAWEI", 100, 20000),
            (10, "VIVO", 100, 12000)]
cursor.executemany(f'''INSERT INTO  Gadgets VALUES(?,?,?,?) ''', products)
con.commit()
cursor.execute('''select * from Gadgets''')
records = cursor.fetchall()
print(records)
for row in records:
    print(row)
