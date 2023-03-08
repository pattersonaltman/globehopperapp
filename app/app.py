#Starting point of our WebApp - main
#pip install Flask

from flask import Flask, request, jsonify
import country
# from flask_wtf.csrf import CSRFProtect  #pip install flask_wtf

#Using Flash framework
app = Flask(__name__)
# csrf = CSRFProtect()
# csrf.init_app(app)

#Delete - DELETE API
@app.route('/countries/<int:country_id>', methods=['DELETE'])
def deleteCountryAPI(country_id):
    return country.deleteCountryView(country_id)

#Update - PUT API
@app.route('/countries/<int:country_id>', methods=['PUT'])
def updateCountryAPI(country_id):
    data = request.json
    return country.updateCountryView(country_id, data)

#Create - POST API
@app.route('/countries', methods=['POST'])
def createCountryAPI():
    data = request.json
    return country.createCountryView(data)

#Read API
@app.route('/countries')
def getAllCountriesAPI():
    return country.getAllCountriesView()






#Execute on the terminal
if __name__ == '__main__':
    app.run(debug=True)