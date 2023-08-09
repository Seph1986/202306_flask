#Importamos la clase Flask
from flask import Flask, render_template, redirect, session, request
import random
import datetime

#Iniciamos instancia de Flask con el nombre de app
app = Flask(__name__)
app.secret_key = "keep it secrete please"

#Controladores

@app.route("/")
def landing():

    if "gold" not in session:
        session["gold"] = 0

    if "console" not in session:
        session["console"] = [""]

    return render_template("index.html")


@app.route("/process_money/", methods=["POST"])
def money_process():

    bulding = request.form["bulding"]
    print(bulding)

    current_time = datetime.datetime.now()

    if bulding == "farm":

        value = random.randint(10,20)
        session["gold"] += value

        session["console"].insert(0, f"<div style='color: green'>Ganaste {value} de oro de la Granja. {current_time}</div>")

    elif bulding == "cave":

        value = random.randint(5,10)
        session["gold"] += value

        session["console"].insert(0, f"<div style='color: green'>Ganaste {value} de oro de la Cueva. {current_time}</div>")

    elif bulding == "house":

        value = random.randint(2,5)
        session["gold"] += value

        session["console"].insert(0, f"<div style='color: green'>Ganaste {value} de oro de la Casa. {current_time}</div>")

    else:
        if random.randint(0,10) <= 7:

            value = random.randint(0,50)
            session["gold"] -= value

            session["console"].insert(0, f"<div style='color: red'>Perdiste {value} en el Casino. {current_time} </div>")

        else:

            value = random.randint(0,50)
            session["gold"] += value

            session["console"].insert(0, f"<div style='color: green' >Ganaste {value} en el casino. {current_time}</div>")


    for con in session["console"]:
        print(con)
    

    return redirect("/")

@app.route("/reset/")
def reset():

    session.clear()

    return redirect("/")


#Iniciamos el servidor
if __name__ == "__main__":
    app.run(debug=True)