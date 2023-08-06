#Flask
from flask import Flask, render_template, request, redirect, session



#Instancia app de la clase Flask
app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"


#Controladores    
@app.route("/")
def base():
    
    if "contador" in session:
       session["contador"] += 1
    else:
        session["contador"] = 1  
    
    return render_template("base.html", count = session["contador"])


@app.route("/destroy_session/")
def eliminte_session():

    session.pop("contador")

    return redirect("/")


@app.route("/plus/", methods = ["POST"])
def double_plus():

    print("Paso por double plus")

    request.form
    
    if "contador" in session:
        session["contador"] += 1
    else:
        session["contador"] = 2

    return redirect("/")

@app.route("/user_input/", methods = ["POST"])
def user_imput():

    user_number = request.form["user_input"]

    if "contador" in session:
        session["contador"] += (int(user_number) - 1)
    else:
        session["contador"] = (int(user_number) - 1)

    return redirect("/")

#Corredor del servidor
if __name__ == "__main__":
     app.run(debug=True)