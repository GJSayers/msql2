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
            "DELETE FROM Friends WHERE name in ['bob', 'jim'])
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
