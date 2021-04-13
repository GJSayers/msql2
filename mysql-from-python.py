import os
import datetime
import pymysql

# Get username from workspace
# (Modify this variable if running on another environment)
username = os.getenv('GJSayers')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE Friends SET age = %s where name = %s;", (23, 'Bob'))
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
