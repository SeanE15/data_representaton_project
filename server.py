from flask import Flask, render_template, request, abort, jsonify
from partDAO import partDAO
from pointsDAO import pointsDAO

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
    # Render the main page for the part viewer
    return render_template('part_viewer.html')
    
@app.route('/parts/')
def getAll():
    # Retrieve all parts from the database and return as JSON
    results = partDAO.getAll()
    return jsonify(results)

@app.route('/parts/<int:id>')
def findById(id):
    # Retrieve a specific part by ID from the database and return as JSON
    part = partDAO.find_by_id(id)
    if part:
        return jsonify(part)
    else:
        return jsonify({}), 204

@app.route('/parts/', methods=['POST'])
def create():
    # Create a new part in the database using data from the request JSON
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
    # Update an existing part in the database using data from the request JSON
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
    # Delete a part from the database by ID
    part = partDAO.find_by_id(id)
    if not part:
        return jsonify({}), 404

    partDAO.delete(id)
    return jsonify({"id": id, "deleted": True})

@app.route('/points/', methods=['GET'])
def getPenaltyPoints():
    # Retrieve all penalty points details from the 'points' table and return as JSON
    penalty_points = pointsDAO.getAll()
    return jsonify(penalty_points)


# Run the Flask app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
