from flask import Flask
from flask import jsonify


app = Flask('wtf')


@app.route("/")
def hello_world():
        return "Hello World! <strong>I am learning Flask</strong>", 200


@app.route("/<name>")
def index(name):
        if name.lower() == "kamilla":
            return "Hello, {}".format(name), 200
        else:
            return "Not Found", 404


@app.route("/json_api")
def json_api():
    pessoas = [{"nome": "Bruno Rocha"},
               {"nome": "Arjen Lucassen"},
               {"nome": "Anneke van Giersbergen"},
               {"nome": "Steven Wilson"}]
    return jsonify(pessoas=pessoas, total=len(pessoas))


app.run(debug=True, use_reloader=True)
