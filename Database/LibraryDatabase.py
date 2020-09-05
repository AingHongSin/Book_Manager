import sqlite3

#conn = sqlite3.connect(':memory:')

conn = sqlite3.connect('Libraries.db')

# Create a cursor
c = conn.cursor()

# create a tabel
c.execute("""CREATE TABLE Data_list 
    (
        Title text,
        Author text,
        Number_of_Pages integer,
        Category text,
        Last_Read text
    )""")


# NULL
# INTERGER
# REAL
# TEXT
# BLOB

# Commit our comand
conn.commit()


# Close our connection 
conn.close()
