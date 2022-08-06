from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisnotsecretatallbutwecanchangethatlater'

class NamerForm(FlaskForm):
    name = StringField('What\'s Your Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/')
def index():
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

@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        
    return render_template(
        'name.html', 
        name=name, 
        form=form
    )



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
