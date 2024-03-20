from flask_wtf import FlaskForm
from wtforms import StringField, FileField, IntegerField, TextAreaField, SelectField
from flask_wtf.file import FileRequired, FileAllowed
from wtforms.validators import InputRequired, DataRequired


class PropertyForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    numOfBeds = IntegerField('numOfBeds', validators=[InputRequired()])
    numOfBaths = IntegerField('numOfBaths', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    price = StringField('Price', validators=[InputRequired()])
    type = SelectField('Type', choices=["House", "Apartment"])
    description = TextAreaField('Description', validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
