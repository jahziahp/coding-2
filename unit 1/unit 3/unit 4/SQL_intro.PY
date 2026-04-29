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
                platform TEXT,
                devloper TEXT,
                price INTEGR,
                genre TETX,
                totalSales INTEGER
                )
             ''')

# 5. we can now create our first databse object
#cursor.execute('''
#               INSERT INTO gameSales(platform, developer, price, genre, totalSales)
#               VALUES('Crimson Dersert','PS5', 'oearl abyss',70, 'action/ adventure', 5000000 )
#               ''')

# 6. once we have new object, we can commit this to our database
#connect.commit()
#connect.close()

cursor.execute('''
               INSERT INTO gameSale(platform, developer, price, genre, totalSales)
               VALUES('Call of duty','Steam', 'Actvison',70, 'action' , 6000000)
               ''')

connect.commit()
connect.close()