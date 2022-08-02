from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    name = 'Klaus'
    stuff = 'My hovercraft is full of eels!'
    cheeses = ['Blue Stilton', 'Cheddar', 'Wensleydale', 'Sage Derby', 56]
    
    return render_template(
        'index.html', 
        name=name,
        stuff=stuff, 
        cheeses=cheeses
    )

@app.route('/user/<username>')
def user(username):
    return render_template('user.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
