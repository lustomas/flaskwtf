from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired()])
    description = StringField('Opis', validators=[DataRequired()])
    done = BooleanField('Czy zapłacone?')
    

