import sqlite3
import os
from contextlib import contextmanager

def CreateDatabase():
    
    with change_dir('Database'):
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
                    Last_Readed text,
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
                    Last_Readed text,
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
                    Last_Readed text,
                    Added_Date text
                )
            """)
        conn.commit()

        c.execute("""CREATE TABLE Album
                (
                    Album_NameList text,
                    None
                )
            """)
        # Commit our comand
        conn.commit()

        c.execute("""CREATE TABLE Authors
                (
                    Authors_NameList text,
                    None
                )
            """)
        conn.commit()
        # Close our connection 
        conn.close()

@contextmanager
def change_dir(Destination):
    try:
        cwd = os.getcwd()
        os.chdir(Destination)
        yield
    finally:
        os.chdir(cwd)



if __name__ == "__main__":
    CreateDatabase()
