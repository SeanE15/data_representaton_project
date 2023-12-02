from flask import Flask, render_template, request, abort, jsonify
from partDAO import partDAO

app = Flask(__name__, static_url_path='', static_folder='staticpages')

part = [

    {"id": 1, "Part_No": "03L152652B", "Part_Name": "Oil Filter", "Price": 12.52},
    {"id": 2, "Part_No": "04K664532B", "Part_Name": "Pollen Filter", "Price": 30.60},
    {"id": 3, "Part_No": "05L332169", "Part_Name": "Sump Plug", "Price": 2.86}

]

nextId=4

@app.route('/')
def index():
    return render_template('part_viewer.html')
    

@app.route('/parts/')
def getAll():
    results = partDAO.getAll()
    return jsonify(results)

@app.route('/parts/<int:id>')
def findById(id):
    foundparts = list(filter (lambda t : t["id"]== id, part))
    if len(foundparts) == 0:
        return jsonify({}) , 204
    return jsonify(foundparts[0])

@app.route('/parts/', methods=['POST'])
def create():
    global nextId
    if not request.json:
        abort(400)
    
    new_part = {

        "id": nextId,
        "Part_No": request.json["Part_Number"],
        "Part_Name": request.json["Part_Name"],
        "Price": request.json["Price"],
    }

    part.append(new_part)
    nextId += 1 
    return jsonify(new_part)

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
    return jsonify(currentPart)

@app.route('/parts/<int:id>', methods=['DELETE'])
def delete(id):
    foundparts = list(filter(lambda t: t["id"] == id, part))
    if len(foundparts) == 0:
        return jsonify({}), 404
    part.remove(foundparts[0])

    return jsonify({"done":True})


if __name__ == "__main__":
    app.run(debug=True)