#imports all the methods we will need to send/ receieve data from DB
#import sqlite3

# just function
#def getALLData():
    # setting up the connection to our db (the road)
    #connect= sqlite3.connect('myDb.db')

    # setting up or vehicle to send/ recive data
    # to/frpm the DB (the vehicle)
    #cursor= connect.cursor()

    # the data we want to get
    # SELCET = our selction
    #query = "SELECT platform FROM gameSale"

    #cursor.execute(query)

    #results = cursor.fetchall()

    #print(results)

#getALLData()

import sqlite3
def getALLData():
    connect= sqlite3.connect('myDb.db')
    
    cursor= connect.cursor()
    
    query = "SELECT name FROM gameSale WHERE developer = Starfeild"

    cursor.execute(query)

    results = cursor.fetchall()

    print(results)

#getALLData()

def deleteData():
    connect= sqlite3.connect('myDb.db')

    cursor =" DELETE FROM gamesale WHERE name= Starfeild"

    cursor.execute(query)