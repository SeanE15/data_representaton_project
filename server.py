from flask import Flask, request, abort, jsonify
from partDAO import partDAO

app = Flask(__name__, static_url_path='', static_folder='staticpages')

part=[
    {"id": 1, "Part_Number": "03L152652B", "Part_Name": "Oil Filter", "Price": 12.52, "Assoc_Vehicle": "VW Golf", "Availability": "12"},
    {"id": 2, "Part_Number": "04K664532B", "Part_Name": "Pollen Filter", "Price": 30.60, "Assoc_Vehicle": "VW Golf", "Availability": "1"},
    {"id": 3, "Part_Number": "05L332169", "Part_Name": "Sump Plug", "Price": 2.86, "Assoc_Vehicle": "VW Golf", "Availability": "100"}
]
nextId=4

@app.route('/')
def index():
    return "This is the start of the parts catalogue"

@app.route('/parts')
def getAll():
    results = partDAO.getAll()
    return jsonify(results)

@app.route('/parts/<int:id>')
def findById(id):
    foundparts = list(filter (lambda t : t["id"]== id, part))
    if len(foundparts) == 0:
        return jsonify({}) , 204
    return jsonify(foundparts[0])

@app.route('/parts', methods=['POST'])
def create():
    global nextId
    if not request.json:
        abort(400)
    
    part = {
        "id": nextId,
        "Part_Number": request.json["Part_Number"],
        "Part_Name": request.json["Part_Name"],
        "Price": request.json["Price"],
        "Assoc_Vehicle": request.json["Assoc_Vehicle"],
        "Availability": request.json["Availability"]
    }
    values =(part['id'],part['Part_Number'],part['Part_Name'],part['Price'],part['Assoc_Vehicle'],part['Availability'],)
    newId = partDAO.create(values)
    part['id'] = newId
    return jsonify(part)

@app.route('/parts/<int:id>', methods=['PUT'])
def update(id):
    foundparts = list(filter(lambda t: t["id"] == id, part))
    if not foundparts:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json

    if 'price' in reqJson and type(reqJson['price']) is not int:
        abort(400)
    if len(foundparts) == 0:
        return jsonify({}), 404
    
    currentPart = foundparts[0]
    if 'Part_Number' in request.json:
        currentPart['Part_Number'] = request.json['Part_Number']
    if 'Part_Name' in request.json:
        currentPart['Part_Name'] = request.json['Part_Name']
    if 'Price' in request.json:
        currentPart['Price'] = request.json['Price']
    if 'Associated_Vehicle' in request.json:
        currentPart['Associated_Vehicle'] = request.json['Associated_Vehicle']
    if 'Availability' in request.json:
        currentPart['Availability'] = request.json['Availability']

    return jsonify(currentPart)

@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    foundparts = list(filter(lambda t: t["id"] == id, part))
    if len(foundparts) == 0:
        return jsonify({}), 404
    part.remove(foundparts[0])

    return jsonify({"done":True})


if __name__ == "__main__":
    app.run(debug=True)