from apis import bp
from flask import jsonify, abort, make_response, request


@bp.errorhandler(404)
def error_404(error):
    return make_response(jsonify({"error": "Not found"}), 404)


grocery = [
    {"name": "apple", "calories": 40},
    {"name": "milk", "calories": 150},
    {"name": "cheese", "calories": 90},
    {"name": "pizza", "calories": 250},
    {"name": "extra", "calories": None}
]

# Get all grocery
@bp.route('/grocery', methods=['GET'])
def get_grocery():
    return jsonify(grocery)

# Get grocery by name
@bp.route('/grocery/<name>', methods=['GET'])
def get_grocery_name(name):
    grocery_item = [item for item in grocery if item["name"] == name]
    if len(grocery_item) == 0:
        abort(404)

    return jsonify(grocery_item[0])

# Add a new grocery
@bp.route('/grocery', methods=["POST"])
def post_grocery_name():
    if not request.json or 'name' not in request.json:
        abort(404)
    item = {
        "name": request.json['name'],
        "calories": request.json.get("calories", None)
    }
    grocery.append(item)
    return jsonify(item), 201

# Update a grocery
@bp.route('/grocery/<name>', methods=["PUT"])
def put_grocery_name(name):
    grocery_item = [item for item in grocery if item["name"] == name]
    if len(grocery_item) == 0:
        abort(404)

    if not request.json:
        abort(404)
    old = grocery_item[0].copy()

    grocery_item[0]["name"] = request.json.get("name", grocery_item[0]["name"])
    grocery_item[0]["calories"] = request.json.get("calories", grocery_item[0][
        "name"])

    return jsonify([{"old":old},{"new" : grocery_item[0]}]), 201



#test curl

# curl -i -H "Content-Type: application/json" -X POST -d "{"""name""":"""Burger""", """calories""": null}"  http://127.0.0.1:5000/api/grocery

# curl -i -H "Content-Type: application/json" -X POST -d "{"""name""":"""Bread""", """calories""": 100}"  http://127.0.0.1:5000/api/grocery

# curl -i  http://127.0.0.1:5000/api/grocery/apple

# curl -i  http://127.0.0.1:5000/api/grocery/orange

#curl -i -H "Content-Type: application/json" -X PUT -d "{"""name""":"""Juice""", """calories""": 75}"  http://127.0.0.1:5000/api/grocery/extra