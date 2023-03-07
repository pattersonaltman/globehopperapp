#Define all services for Country and City

from flask import Flask, request, jsonify
import conn


#gets all records from Country table using SQL
def allCountries():
    #Open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Execute the SQL
    mycursor.execute("select * from Country")
    results = mycursor.fetchall()

    #Close connection
    mycursor.close()
    conn.myconn.close()

    return results