from flask import Flask, render_template

# create a flask instance
app = Flask(__name__)

# create a route decorator
# @app.route('/')
# def index():
#     return "<h1>Hello World!</h1>"

@app.route('/')
def index():
    return render_template('index.html')



# localhost:5000/user/name
@app.route('/user/<name>')
def user(name):
    # pass an argument to the "website"
    return "<h1>Hello {}</h1>".format(name)
