from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/message")
def message():
    return jsonify("Hello world!")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
