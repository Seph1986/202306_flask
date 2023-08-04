#Flask
from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template('index.html')

@app.route('/checkout/', methods=['POST'])         
def checkout():

    strawberry_count = request.form['strawberry']
    apple_count = request.form['apple']
    raspberry_count = request.form['raspberry']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    id = request.form['student_id']

    fruit_plus = [int(strawberry_count), int(apple_count), int(raspberry_count)]

    fruit_count = sum(fruit_plus)

    print(request.form)
    print(f'-%-%-%-%- Cobrando a {first_name} {last_name} por {fruit_count} frutas -%-%-%-%-')

    return render_template('checkout.html', strawberry = strawberry_count,
                            apple = apple_count, raspberry = raspberry_count,
                            name = first_name, last = last_name, id = id)

@app.route('/fruits/')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    