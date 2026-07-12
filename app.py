from flask import Flask, request
from src.main import add, subtract, multiply, divide

app = Flask(__name__)

@app.route("/add")
def add_route():
    a = request.args.get("a")
    b = request.args.get("b")

    if a is None or b is None:
        return {"error": "missing params"}, 400

    a = int(a)
    b = int(b)

    return f"result: {add(a, b)}"

@app.route("/sub")
def sub_route():
    a = request.args.get("a")
    b = request.args.get("b")

    if a is None or b is None:
        return "error: missing params", 400

    a = int(a)
    b = int(b)

    return f"result: subtract(a, b)"

@app.route("/mul")
def mul_route():
    a = request.args.get("a")
    b = request.args.get("b")

    if a is None or b is None:
        return "error: missing params", 400

    a = int(a)
    b = int(b)

    return f"result: {multiply(a, b)}"

@app.route("/div")
def div_route():
    a = request.args.get("a")
    b = request.args.get("b")

    if a is None or b is None:
        return "error: missing params", 400

    a = int(a)
    b = int(b)

    return f"result: {divide(a, b)}"

@app.route("/roulete")
def roulete_route():
    import random
    number = random.randint(0, 6)
    number_2 = random.randint(0, 6)
    if number == number_2:
        return "You lose"
    else: 
        return "You win"

    return "Roulete"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)