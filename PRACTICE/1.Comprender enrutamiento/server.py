#FLASK

from flask import Flask
app = Flask(__name__)    
@app.route('/')          
def hola_mundo():
    return 'Hola Mundo!' 

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:par>')
def greeting(par):
    return f'¡Hola, {par}!'

@app.route('/repeat/<int:count>/<string:word>')
def repeat(count,word):
    return f'{word*count} '

if __name__=="__main__":  
    app.run(debug=True)