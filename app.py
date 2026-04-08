from flask import Flask, render_template, request
import random
import time

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        jugador = request.form["jugador"]
        edad = request.form["edad"]

        return f"Bienvenido {jugador}, edad {edad}"

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)