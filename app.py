from flask import Flask, request
from src.main import add, subtract

app = Flask(__name__)

@app.route("/add")
def add_route():
    a = request.args.get("a")
    b = request.args.get("b")

    if a is None or b is None:
        return {"error": "missing params"}, 400

    a = int(a)
    b = int(b)

    return {"result": add(a, b)}

@app.route("/sub")
def sub_route():
    a = request.args.get("a")
    b = request.args.get("b")

    if a is None or b is None:
        return {"error": "missing params"}, 400

    a = int(a)
    b = int(b)

    return {"result": subtract(a, b)}

if __name__ == "__main__":
    app.run(debug=True)