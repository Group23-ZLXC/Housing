from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class CommentForm(FlaskForm):
    comment = TextAreaField('Your Comment', validators=[DataRequired()])
    submit = SubmitField('Submit')
