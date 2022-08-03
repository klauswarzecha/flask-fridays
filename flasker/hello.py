from flask import Flask, render_template
import waitress

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


# custom error pages

# invalid URL
@app.errorhandler(404)
def page_not_found(statuscode):
    return render_template('404.html'), 404

# internal server error
@app.errorhandler(500)
def page_not_found(statuscode):
    return render_template('500.html'), 500



if __name__ == '__main__':
    app.run(debug=True)
