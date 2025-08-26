import mysql.connector

def create_database():
    try:
        connection = mysql.connector.connect(
            host = 'localhost',
            user = 'austinej',
            password = 'Jum@7627'
        )

        if connection.is_connected():
            cursor = connection.cursor()

            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as e:
        print(f'Error while connecting to MySQL: {e}')
    
    finally:
        try:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed.")
            
        except:
            pass

if __name__ == "__main__":
    create_database()

        