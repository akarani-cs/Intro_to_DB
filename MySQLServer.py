#!/usr/bin/env python3

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (adjust host, user, and password as needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password_here'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
            "except mysql.connector.Error"

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Close cursor and connection if they were opened
        try:
            if connection.is_connected():
                cursor.close()
                connection.close()
                # Optional: print confirmation message for closure
                # print("MySQL connection closed.")
        except NameError:
            pass

if __name__ == '__main__':
    create_database()
