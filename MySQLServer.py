import mysql.connector
try: 
    connection = mysql.connector.connect( 
        host ='LocalHost',
        user ='root',
        passwd ='killMOnger09&',
        )

    cursor = connection.cursor()
    value =cursor.execute('CREATE DATABASE IF NOT EXISTS alx_book_store')
    connection.commit()
    print("Database 'alx_book_store'created successfully")
except mysql.connector.Error as e:
    print(e)
