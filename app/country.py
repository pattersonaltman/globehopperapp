#Define all functions related to Country APIs

from flask import Flask, request, jsonify
import services

#Function to create new Country
def createCountry(data):
    services.createCountry(data)
    return jsonify({'message': 'Data inserted successfully'})

#Function to get all countries and return as a JSON object
def getCountries():
    results = services.allCountries()

    data = []
    for row in results:
        data.append({
            "CountryId":row[0],
            "Name":row[1],
            "Population":row[2],
            "Continent":row[3]
        })

    return jsonify(data)