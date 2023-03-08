#Define all functions realted to City APIs

from flask import Flask, request, jsonify
import services
import country

#Function to update a City by id
def updatecityview(cityid, data):
    services.updatecityservice(cityid, data)
    return jsonify({'message':f'Record [{cityid}] updated successfully'})

#Function to create a new City
def createcityview(data):
    services.createcityservice(data)
    return jsonify({'message':'Data inserted successfully'})

#Function to get all cities
def getallcitiesview():
    results = services.getallcitiesservice()

    data = []
    for row in results:
        data.append({
            "CityId":row[0],
            "Name":row[1],
            "CountryId":row[2],
            "Capital":row[3],
            "FirstLandMark":row[4],
            "SecondLandMark":row[5],
            "ThirdLandMark":row[6]
        })

    return jsonify(data)