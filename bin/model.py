# -*- coding: utf-8 -*-
##class and functions##
import sqlite3
conn = sqlite3.connect("database.db")
c = conn.cusor()

class database:
## TODO: Create databaseclass

class table:
##TODO Create tableclass




def createdb():
    c.execute('CREATE DATABASE ' + db_name + '.db'())
    c.commit()
    createtable()


def createtable():
    c.execute('''CREATE TABLE ' + filename + '
             (id NOT NULL UNIQUE, filename varchar(255), lastmod varchar(255) , dirname varchar(255) )''')
    c.commit()
    c.close()

def createtableobj():
    ##TODO

def writetotable(tablename,filename, dirname,):
    c.execute('INSET INTO ('"+ tablename +"') ('" + filename + "'," + dirname + " )'(tablename, filename, dirname))
    c.commit()






