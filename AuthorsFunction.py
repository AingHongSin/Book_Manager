import os
import sqlite3
import Database

class Function():
    def __init__(self, ID, Title, Author, Category, Number_of_Pages, Last_Read, Add_Date):

        self.AuthorNameList_Databas = []
        if Author == None:
            Author = 'Unknown Author'

        os.chdir('/Users/privateman/Documents/Project/Book_Manager/Database')
        self.conn = sqlite3.connect('Libraries.db')
        self.c = self.conn.cursor()

        self.c.execute("SELECT * FROM Authors ")
        items = self.c.fetchall()

        for item in items:
            self.AuthorNameList_Databas.append(item[0])

        if Author in self.AuthorNameList_Databas:

            AuthorName = [Author]
            if AuthorName[0] == None:
                AuthorsData = [
                            (ID, Title, 'Unkonwn Author', Number_of_Pages, Category, Last_Read, Add_Date)
                            ]
                self.c.executemany(f"INSERT INTO [{Author}] VALUES (?,?,?,?,?,?,?)" , AuthorsData)
                self.conn.commit()

            else: 
                AuthorsData = [
                            (ID, Title, AuthorName[0], Number_of_Pages, Category, Last_Read, Add_Date)
                            ]
                self.c.executemany(f"INSERT INTO [{Author}] VALUES (?,?,?,?,?,?,?)" , AuthorsData)
                self.conn.commit()

        else: 
            if Author != self.AuthorNameList_Databas:
                if Author == None:
                    Author = 'Unknown Author'
                AuthorName = [Author]

                self.c.execute("INSERT INTO Authors (Authors_NameList) VALUES (?)", AuthorName)
                self.conn.commit()

                Database.addAuthors_Name(AuthorName[0])

                if AuthorName[0] == None:
                    AuthorsData = [
                                (ID, Title, 'Unkonwn Author', Number_of_Pages, Category, Last_Read, Add_Date)
                                ]
                    self.c.executemany(f"INSERT INTO [{Author}] VALUES (?,?,?,?,?,?,?)" , AuthorsData)
                    self.conn.commit()

                else: 
                    AuthorsData = [
                                (ID, Title, AuthorName[0], Number_of_Pages, Category, Last_Read, Add_Date)
                                ]
                    self.c.executemany(f"INSERT INTO [{AuthorName[0]}] VALUES (?,?,?,?,?,?,?)" , AuthorsData)
                    self.conn.commit()

        self.conn.close()
