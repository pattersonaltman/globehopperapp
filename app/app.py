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

#Update - PUT API
@app.route('/countries/<int:country_id>', methods=['PUT'])
def updateCountry(country_id):
    print(country_id)
    data = request.json
    return country.updateCountry(country_id, data)

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