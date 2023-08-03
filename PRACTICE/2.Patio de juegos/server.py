#Flask

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def land_page():
    return render_template('index.html')

@app.route('/play/<int:count>')
def number(count):
    return render_template('counts.html', num = count)

@app.route('/play/<int:count>/<color>')
def estilo(count, color):
    return render_template('color.html', num = count, estilo = color)


if __name__=="__main__":  
    app.run(debug=True)