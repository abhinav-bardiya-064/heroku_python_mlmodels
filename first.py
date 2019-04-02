from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Welcome to machine learning model APIs! my first app"


if __name__ == '__main__':
    app.run(debug=True)