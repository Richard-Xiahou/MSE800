from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_flask():
    return "<p>Hello, Flask!</p>"

# 通过 http://127.0.0.1:5000/bye 访问
@app.route("/bye")
def bye():
    return "<p>Bye, Flask!</p>"

# New POST API
@app.route("/api/greet", methods=["POST"])
def greet():
    # 1. Read JSON data from the request body，需要处理请求体不是json的情况
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    # 2. Get the name field
    name = data.get("name", "Guest")

    # 3. Build a JSON response
    return jsonify({
        "message": f"Hello, {name}!",
        "success": True
    })

@app.route("/username/<name>")
def username(name):
    return f" {name} is learning Flask"

@app.route("/product/<int:id>")
def product_id(id):
    return f"Product ID is {id}"


if __name__ == "__main__":
    app.run(debug=True)
