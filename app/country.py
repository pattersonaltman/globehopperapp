#Define all functions related to Country APIs

from flask import Flask, request, jsonify
import services

#Function to get all Countries by continent
def getallcountriesbycontinentview(continent):
    resultsandcities = services.getallcountriesbycontinentservice(continent)
    results = resultsandcities[0]
    cities = resultsandcities[1]

    citydata = []
    for row in cities:
        citydata.append({
            "CityId":row[0],
            "Name":row[1],
            "CountryId":row[2],
            "Capital":row[3],
            "FirstLandMark":row[4],
            "SecondLandMark":row[5],
            "ThirdLandMark":row[6]
        })

    data = []
    for row in results:

        cityappendlist = []
        for city in citydata:
            if row[0] == city['CountryId']:
                cityappendlist.append(city)

        data.append({
            "CountryId":row[0],
            "Name":row[1],
            "Population":row[2],
            "Continent":row[3],
            "Cities":cityappendlist
        })

    return jsonify(data)

#Function to delete a country by id
def deletecountryview(country_id):
    services.deletecountryservice(country_id)
    return jsonify({'message': f'Record [{country_id}] deleted successfully'})

#Function to update a country by id
def updatecountryview(country_id, data):
    services.updatecountryservice(country_id, data)
    return jsonify({'message': f'Record [{country_id}] updated successfully'})

#Function to create new Country
def createcountryview(data):
    services.createcountryservice(data)
    return jsonify({'message': 'Data inserted successfully'})

#Function to get all countries and return as a JSON object
def getallcountriesview():
    resultsandcities = services.getallcountriesservice()
    results = resultsandcities[0]
    cities = resultsandcities[1]

    citydata = []
    for row in cities:
        citydata.append({
            "CityId":row[0],
            "Name":row[1],
            "CountryId":row[2],
            "Capital":row[3],
            "FirstLandMark":row[4],
            "SecondLandMark":row[5],
            "ThirdLandMark":row[6]
        })

    data = []
    for row in results:

        cityappendlist = []
        for city in citydata:
            if row[0] == city['CountryId']:
                cityappendlist.append(city)

        data.append({
            "CountryId":row[0],
            "Name":row[1],
            "Population":row[2],
            "Continent":row[3],
            "Cities":cityappendlist
        })

    return jsonify(data)