#Define all services for Country and City

from flask import Flask, request, jsonify
import conn

def updateCountry(country_id, data):
    #Open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Parse the Data
    name = data['Name']
    population = data['Population']
    continent = data['Continent']

    #Execute the SQL
    mysql = "UPDATE `globehopperapp`.`Country` SET `Name` = %s, `Population` = %s, `Continent` = %s WHERE CountryId = %s"
    values = (name, population, continent, country_id)
    mycursor.execute(mysql, values)

    #Close connection
    mycursor.close()
    conn.myconn.close()

#Create a Country record
def createCountry(data):
    #Open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    countryId = data['CountryId']
    name = data['Name']
    population = data['Population']
    continent = data['Continent']
    
    #Execute the SQL
    mysql = "INSERT INTO Country (CountryId, Name, Population, Continent) VALUES (%s, %s, %s, %s)"
    values = (countryId, name, population, continent)
    mycursor.execute(mysql, values)

    #Close connection
    mycursor.close()
    conn.myconn.close()

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

