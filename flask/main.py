from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return {"Hello": "World"}


@app.route("/users", methods=["POST"])
def read_item():
    new_user = request.json
    return_value = f'{new_user["name"]},{new_user["age"]},{new_user["location"]},'
    return {"data": "".join([return_value for _ in range(0, 1024)])}
