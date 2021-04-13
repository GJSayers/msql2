import os
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
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "select * from Artist;"
        cursor.execute(sql)
        for row in cursor:
            print(row)
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
