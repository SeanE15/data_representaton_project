from flask import Flask, render_template, request, abort, jsonify
from partDAO import partDAO

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
    return render_template('part_viewer.html')
    

@app.route('/parts/')
def getAll():
    results = partDAO.getAll()
    return jsonify(results)

@app.route('/parts/<int:id>')
def findById(id):
    part = partDAO.find_by_id(id)
    if part:
        return jsonify(part)
    else:
        return jsonify({}), 204

@app.route('/parts/', methods=['POST'])
def create():
    if not request.json:
        abort(400)
    
    values = (
        request.json.get("Part_Name"),
        request.json.get("Part_No"),
        request.json.get("Price"),
    )


    new_id = partDAO.create(values)
    return jsonify({"id": new_id}), 201

@app.route('/parts/<int:id>', methods=['PUT'])
def update(id):
    part = partDAO.find_by_id(id)
    if not part:
        abort(404)
    
    if not request.json:
        abort(400)
    
    values = (

        request.json.get("Part_Name"),
        request.json.get("Part_No"),
        request.json.get("Price"),
        id
    )

    partDAO.update(values)
    return jsonify({"id": id, "updated": True})

@app.route('/parts/<int:id>', methods=['DELETE'])
def delete(id):
    part = partDAO.find_by_id(id)
    if not part:
        return jsonify({}), 404

    partDAO.delete(id)
    return jsonify({"id": id, "deleted": True})


if __name__ == "__main__":
    app.run(debug=True)