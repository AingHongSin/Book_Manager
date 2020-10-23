import sqlite3
import os

def addAlbum(AlbumName):
    
    #conn = sqlite3.connect(':memory:')
    conn = sqlite3.connect('Libraries.db')
    # Create a cursor
    c = conn.cursor()
    
    c.execute(f"""CREATE TABLE [{AlbumName}]
            (
                ID integer,
                Title text,
                Author text, 
                Number_of_Pages integer,
                Last_Readed datetime,
                Added_Date text
            )
        """)
    # Commit our comand
    conn.commit()
    # Close our connection 
    conn.close()

def addCategories(CategoryName):
    #conn = sqlite3.connect(':memory:')
    conn = sqlite3.connect('Libraries.db')
    # Create a cursor
    c = conn.cursor()
    
    c.execute(f"""CREATE TABLE [{CategoryName}]
            (
                ID integer,
                Title text,
                Author text, 
                sNumber_of_Pages integer,
                Last_Readed datetime,
                Added_Date text
            )
        """)
    # Commit our comand
    conn.commit()
    # Close our connection 
    conn.close()

def addAuthors_Name(AuthorName):
    #conn = sqlite3.connect(':memory:')
    conn = sqlite3.connect('Libraries.db')
    # Create a cursor
    c = conn.cursor()
    
    c.execute(f"""CREATE TABLE [{AuthorName}]
            (
                ID integer,
                Title text,
                Author text, 
                Number_of_Pages integer,
                Last_Readed datetime,
                Added_Date text
            )
        """)
    # Commit our comand
    conn.commit()
    # Close our connection 
    conn.close()



# NULL
# INTERGER
# REAL
# TEXT
# BLOB

