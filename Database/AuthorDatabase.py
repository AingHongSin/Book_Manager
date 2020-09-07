import os
import sqlite3

os.chdir('/Users/macbook/Documents/Project/Book_Manager/Database')
conn = sqlite3.connect('Libraries.db')
c = conn.cursor()

#c.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
#
#table_in_Database = []
#
#for item in c.fetchall():
#    table_in_Database.append(item[0])

c.execute("SELECT * FROM Data_list ")
for Author in c.fetchall():
    print(Author[1])