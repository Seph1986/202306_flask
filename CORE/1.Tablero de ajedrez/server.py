#FLASK
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")      
def base(x = 4, y = 4, color1 = "peachpuff", color2 = "blueviolet"):
    return render_template("index.html", num_x = x , num_y = y, color1 = color1, color2 = color2)


@app.route("/<int:x>/")      
def filas(x, y = 4, color1 = "peachpuff", color2 = "blueviolet"):
    return render_template("index.html", num_x = x , num_y = y, color1 = color1, color2 = color2)


@app.route("/<int:x>/<int:y>/")      
def filas_columnas(x, y, color1 = "peachpuff", color2 = "blueviolet"):
    return render_template("index.html", num_x = x , num_y = y, color1 = color1, color2 = color2)


@app.route("/<int:x>/<int:y>/<color1>/")      
def color1(x, y, color1, color2 = "blueviolet"):
    return render_template("index.html", num_x = x , num_y = y, color1 = color1, color2 = color2)


@app.route("/<int:x>/<int:y>/<color1>/<color2>")      
def color2(x, y, color1, color2):
    return render_template("index.html", num_x = x , num_y = y, color1 = color1, color2 = color2)


if __name__=="__main__":    
    app.run(debug=True)