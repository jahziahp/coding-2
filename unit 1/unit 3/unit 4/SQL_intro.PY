import sqlite3
# 1. bring in the sql lite module to get acess to all sql methods (function) to work our database.

connect= sqlite3.connect('myDb.db')
# 2. we need to estasblish an actual database file using the connect method.

# 3. create a pbject that will be sent to the new database
cursor = connect.cursor()

# 4. need to create a schema (structure) for our data. 
# in sql text is the same as string. ALSO we capitilize the data types
cursor.execute('''
            CREATE TABLE gameSale(
                id INTERGER PRIMARY KEY,
                name TEXT,
                platform TEXT,
                developer TEXT,
                price INTEGER,
                genre TEXT,
                totalSales INTEGER
                )
             ''')

# 5. we can now create our first databse object
#cursor.execute('''
#               INSERT INTO gameSales(name, platform, developer, price, genre, totalSales)
#               VALUES('Crimson Dersert','PS5', 'pearl abyss',70, 'action/ adventure', 5000000 )
#               ''')

# 6. once we have new object, we can commit this to our database
#connect.commit()
#connect.close()

#cursor.execute('''
#               INSERT INTO gameSale(name, platform, developer, price, genre, totalSales)
#               VALUES('Call of duty','Steam', 'Actvison',70, 'action' , 6000000)
#               ''')

#connect.commit()
#connect.close()

# NUL means nothing and a data type and have no vaule

#cursor.execute('''
#               INSERT INTO gameSale(name, platform, developer, price, genre, totalSales)
#               VALUES('Starfeild','Steam', 'Bethesda',50, 'Sci-fi/Action' , 3000000)
#               ''')
# update computers
# set platform
# cursor.execute('''
#                UPDATE
#                SET platform = 'PS5'
#                WHERE name = 'Call od Duty' 
               
#                ''')


#connect.commit()
#connect.close()