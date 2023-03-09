#Define all services for Country and City

from flask import Flask, request, jsonify
import conn

    #City Services

#Get a capital city record by country name
def getcapitalcitybycountryservice(countryname):
    #Open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Execute the SQL
    mysql = f"select * from city join country on country.CountryId = city.CountryId where country.Name = '{countryname}' and city.Capital = 1"
    mycursor.execute(mysql)
    results = mycursor.fetchall()

    #Close connection
    mycursor.close()
    conn.myconn.close()

    return results

#Delete a City record by id
def deletecityservice(cityid):
    #Open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Execute the SQL
    mysql = f"delete from City where CityId = {cityid}"
    mycursor.execute(mysql)

    #Close connection
    mycursor.close()
    conn.myconn.close()

#Update a City record by id
def updatecityservice(cityid, data):
    #Open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Parse the Data
    name = data['Name']
    countryid = data['CountryId']
    capital = data['Capital']
    firstlandmark = data['FirstLandMark']
    secondlandmark = data['SecondLandMark']
    thirdlandmark = data['ThirdLandMark']

    #Execute the SQL
    mysql = f"update City set Name = %s, CountryId = %s, Capital = %s, FirstLandMark = %s, SecondLandMark = %s, ThirdLandMark = %s where CityId = {cityid}"
    values = (name, countryid, capital, firstlandmark, secondlandmark, thirdlandmark)
    mycursor.execute(mysql, values)

    #Close connection
    mycursor.close()
    conn.myconn.close()

#Create a City record
def createcityservice(data):
    #Open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Parse the Data
    cityid = data['CityId']
    name = data['Name']
    countryid = data['CountryId']
    capital = data['Capital']
    firstlandmark = data['FirstLandMark']
    secondlandmark = data['SecondLandMark']
    thirdlandmark = data['ThirdLandMark']

    #Execute the SQL
    mysql = "insert into City (CityId, Name, CountryId, Capital, FirstLandMark, SecondLandMark, ThirdLandMark) values (%s, %s, %s, %s, %s, %s, %s)"
    values = (cityid, name, countryid, capital, firstlandmark, secondlandmark, thirdlandmark)
    mycursor.execute(mysql, values)

    #Close connection
    mycursor.close()
    conn.myconn.close()

#gets all records from City table using SQL
def getallcitiesservice():
    #Open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Execute the SQL
    mycursor.execute("select * from City")
    results = mycursor.fetchall()

    #Close connection
    mycursor.close()
    conn.myconn.close()

    return results




    #Country Services

#Get all Country records given a continent
def getallcountriesbycontinentservice(continent):
    #Open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Execute the SQL
    mycursor.execute(f"select * from Country where Continent = '{continent}'")
    results = mycursor.fetchall()

    #Close connection
    mycursor.close()
    conn.myconn.close()

    return results


#Delete a Country record
def deletecountryservice(country_id):
    #Open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Execute the SQL
    mysql = f"delete from Country where CountryId = {country_id}"
    mycursor.execute(mysql)

    #Close connection
    mycursor.close()
    conn.myconn.close()

#Update a Country record
def updatecountryservice(country_id, data):
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
def createcountryservice(data):
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
def getallcountriesservice():
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

