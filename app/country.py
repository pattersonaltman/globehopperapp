#Define all functions related to Country APIs

from flask import Flask, request, jsonify
import services

#Function to get all Countries by continent
def getallcountriesbycontinentview(continent):
    results = services.getallcountriesbycontinentservice(continent)

    data = []
    for row in results:
        data.append({
            "CountryId":row[0],
            "Name":row[1],
            "Population":row[2],
            "Continent":row[3] 
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
    results = services.getallcountriesservice()

    data = []
    for row in results:
        data.append({
            "CountryId":row[0],
            "Name":row[1],
            "Population":row[2],
            "Continent":row[3]
        })

    return jsonify(data)