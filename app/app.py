#Starting point of our WebApp - main
#pip install Flask

from flask import Flask, request, jsonify
import country

#Using Flash framework
app = Flask(__name__)

#Create - POST API
@app.route('/countries', methods=['POST'])
def createCountry():
    data = request.json
    return country.createCountry(data)

#Read API
@app.route('/countries')
def getAllCountries():
    return country.getCountries()






#Execute on the terminal
if __name__ == '__main__':
    app.run(debug=True)