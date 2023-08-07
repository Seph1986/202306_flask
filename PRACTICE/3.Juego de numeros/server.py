# Flask
from flask import Flask, render_template, redirect, request, session
import random

#Instanciando Flask
app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"

@app.route("/")
def landing():

   
    if "ran_num" in session:
       pass
    else:
       session["ran_num"] = random.randint(1,100)

    if "trys" in session:
        session["trys"] += 1
    else:
        session["trys"] = 0 
       
    print(f'--------{session["ran_num"]}---------')
    print("Paso por landing y comenzo session")

    return render_template("index.html")

@app.route("/number/", methods = ["POST"])
def guess_number():

    
    session["response"] = int(request.form["number"])

    print("Paso por guess number y acepto el input")
    return redirect("/")

@app.route("/restart/", methods = ["POST"])
def reset_game():

    session.pop("ran_num")

    if "response" in session:
        session.pop("response")
        
    session.pop("trys")

    return redirect("/")



#Comenzando debugger para desarrollo
if __name__ == "__main__":
    app.run(debug=True)