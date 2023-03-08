#Define all functions related to Country APIs

from flask import Flask, request, jsonify
import services

#Function to delete a country by id
def deleteCountryView(country_id):
    services.deleteCountryService(country_id)
    return jsonify({'message': f'Record [{country_id}] deleted successfully'})

#Function to update a country by id
def updateCountryView(country_id, data):
    services.updateCountryService(country_id, data)
    return jsonify({'message': f'Record [{country_id}] updated successfully'})

#Function to create new Country
def createCountryView(data):
    services.createCountryService(data)
    return jsonify({'message': 'Data inserted successfully'})

#Function to get all countries and return as a JSON object
def getAllCountriesView():
    results = services.getAllCountriesService()

    data = []
    for row in results:
        data.append({
            "CountryId":row[0],
            "Name":row[1],
            "Population":row[2],
            "Continent":row[3]
        })

    return jsonify(data)