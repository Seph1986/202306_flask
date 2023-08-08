from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"

@app.route("/")
def landing():

    return render_template("landing.html")

@app.route("/result/")
def result():

    return render_template("info.html")

@app.route("/form/", methods = ["POST"])
def form_recive():

    keys = ["user_name","location","language","comment"]

    for key in keys:
        session[key] = request.form[key]
    

    print(session["user_name"],session["location"],session["language"],session["comment"] )
    

    return redirect("/result/")

@app.route("/reset/")
def reset_user():

    keys = ["user_name","location","language","comment"]

    for key in keys:
        del session[key]

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)