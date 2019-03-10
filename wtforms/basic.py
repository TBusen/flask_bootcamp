from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField, RadioField,
                     SelectField, TextField, TextAreaField, SubmitField)
from wtforms.validators import DataRequired


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey


class InfoForms(FlaskForm):

    breed = StringField('What breed are you?', validators=[DataRequired()])
    neutered = BooleanField("Have you been neutered?")
    mood = RadioField("Please choose your mood:",
                      choices=[('mood_one', 'Happy'), ('mood_two', 'Excited')])
    food_choice = SelectField("Pick your favorite food:",
                              choices=[('chi', 'chicken'), ('bf', 'beef'), ('fish', 'fish')])
    feedback = TextAreaField("Please provide any feedback:")
    submit = SubmitField("Submit")

# get/post methods allows passing form to html template


@app.route('/', methods=['GET','POST']) 
def index():

    form = InfoForms()

    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food_choice'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        return redirect(url_for('thankyou'))
    return render_template('index.html', form=form)


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


if __name__ ==  '__main__':
    @app.run(debug=True)