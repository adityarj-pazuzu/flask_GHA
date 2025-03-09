"""A simple Hello world code in Flask"""

from flask import Flask

app = Flask(__name__)

MSG = "Hello, World"


@app.route("/")
def hello_world():
    """
    This function prints the msg as defined
    :return: msg string
    """
    return f"{MSG}"


if __name__ == "__main__":
    app.run(debug=True)
