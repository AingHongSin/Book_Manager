import sqlite3
import os

def CreateDatabase():
    
    os.chdir('/Users/privateman/Documents/Project/Book_Manager/Database')
    #conn = sqlite3.connect(':memory:')
    conn = sqlite3.connect('Libraries.db')
    # Create a cursor
    c = conn.cursor()

    # create a tabel
    c.execute("""CREATE TABLE Data_list 
            (
                ID integer,
                Title text,
                Author text,
                Number_of_Pages integer,
                Last_Readed datetime,
                Added_Date text
            )
        """)
    conn.commit()

    c.execute("""CREATE TABLE Favorite 
            (
                ID integer,
                Title text,
                Author text, 
                Number_of_Pages integer,
                Last_Readed datetime,
                Added_Date text
            )
        """)
    conn.commit()

    c.execute("""CREATE TABLE Recent
            (
                ID integer,
                Title text,
                Author text, 
                Number_of_Pages integer,
                Last_Readed datetime,
                Added_Date text
            )
        """)
    conn.commit()
    
    c.execute("""CREATE TABLE Album
            (
                Album_NameList text
            )
        """)
    # Commit our comand
    conn.commit()
    
    c.execute("""CREATE TABLE Authors
            (
                Authors_NameList text
            )
        """)
    conn.commit()


    # Close our connection 
    conn.close()
CreateDatabase()
