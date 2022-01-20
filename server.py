from flask import Flask, render_template

app = Flask(__name__)

@app.route("/play/")
def patioDeJuegos():
    return render_template("index.html", cantidad=3, color="blue")

@app.route("/play/<int:cantidad>")
def patioDeJuegosCantidad(cantidad:int):
    return render_template("index.html", cantidad=cantidad, color="blue")

@app.route("/play/<int:cantidad>/<color>")
def patioDeJuegosCantidadColor(cantidad:int,color:str):
    return render_template("index.html", cantidad=cantidad, color=color)
if(__name__ == "__main__"):
    app.run(debug=True)