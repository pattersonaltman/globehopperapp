#Starting point of our WebApp - main
#pip install Flask

from flask import Flask, request, jsonify
import country
import city
# from flask_wtf.csrf import CSRFProtect  #pip install flask_wtf

#Using Flash framework
app = Flask(__name__)
# csrf = CSRFProtect()
# csrf.init_app(app)


    # Country APIs

#Delete - DELETE API
@app.route('/countries/<int:country_id>', methods=['DELETE'])
def deletecountryapi(country_id):
    return country.deletecountryview(country_id)

#Update - PUT API
@app.route('/countries/<int:country_id>', methods=['PUT'])
def updatecountryapi(country_id):
    data = request.json
    return country.updatecountryview(country_id, data)

#Create - POST API
@app.route('/countries', methods=['POST'])
def createcountryapi():
    data = request.json
    return country.createcountryview(data)

#Read API
@app.route('/countries')
def getallcountriesapi():
    return country.getallcountriesview()



    # City APIs

#Delete - DELETE API
@app.route('/cities/<int:cityid>', methods=['DELETE'])
def deletecityapi(cityid):
    return city.deletecityview(cityid)

#Update - PUT API
@app.route('/cities/<int:cityid>', methods=['PUT'])
def updatecityapi(cityid):
    data = request.json
    return city.updatecityview(cityid, data)

#Create - POST API
@app.route('/cities', methods=['POST'])
def createcityapi():
    data = request.json
    return city.createcityview(data)

#Read API
@app.route('/cities')
def getallcitiesapi():
    return city.getallcitiesview()




#Execute on the terminal
if __name__ == '__main__':
    app.run(debug=True)