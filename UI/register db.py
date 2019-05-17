
import sqlite3
def creat_database():

   conn = sqlite3.connect('Database.db')
   with conn:
      cursor=conn.cursor()

   cursor.execute('CREATE TABLE IF NOT EXISTS register (ID INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT,password  TEXT,re_password1 TEXT,re_password2 TEXT,re_password3 TEXT,re_password4 TEXT,re_password5 TEXT)')
   #cursor.execute('INSERT INTO register (username, password, re_password1, re_password2, re_password3, re_password4, re_password5) VALUES(2,2,2,2,2,2,2)')
   conn.commit()


def add_data(username, password, re_password1, re_password2, re_password3, re_password4, re_password5):

   conn = sqlite3.connect('Database.db')
   with conn:
      cursor=conn.cursor()

   cursor.execute('INSERT INTO register (username, password, re_password1, re_password2, re_password3, re_password4, re_password5) VALUES(?,?,?,?,?,?,?)',(username, password, re_password1, re_password2, re_password3, re_password4, re_password5,))
   conn.commit()


def save_db2excle():

   conn = sqlite3.connect('Database.db')
   import pandas as pd
   # Create your connection.

   df = pd.read_sql_query("SELECT * FROM register", conn)
   df.to_excel('registerDATA.xlsx')

   conn.commit()

creat_database()
add_data('ahmed',34,34,34,34,34,34)
save_db2excle()