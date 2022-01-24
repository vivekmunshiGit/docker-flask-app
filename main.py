from flask import Flask

app = Flask(__name__)


# Pass the required route to the decorator.
@app.route("/hello")
def hello():
    return "Hello, Docker"


@app.route("/")
def index():
    return "Homepage of Docker"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
