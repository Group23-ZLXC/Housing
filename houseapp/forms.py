from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, IntegerField, RadioField, SelectField
from wtforms.validators import DataRequired

class PredictForm(FlaskForm):
    lng = StringField('Lng')
    lat = StringField('Lat')
    square = StringField('*Square', validators=[DataRequired()])
    living_room = SelectField('*Living Room', choices = [
        (0,0),(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9)]
        , validators=[DataRequired()]) #0-9
    drawing_room = SelectField('*Drawing Room', choices = [
        (0,0),(1,1),(2,2),(3,3),(4,4),(5,5)], validators=[DataRequired()]) #0-5
    kitchen = SelectField('*Kitchen', choices = [
        (0,0),(1,1),(2,2),(3,3),(4,4),(5,5)], validators=[DataRequired()]) #0-5
    bathroom = SelectField('*Bathroom', choices = [
        (0,0),(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7)], validators=[DataRequired()]) #0-7
    floor = IntegerField('*Floor', validators=[DataRequired()])
    elevator = BooleanField('*Elevator')
    subway = BooleanField('*Subway')
    district = SelectField('*District', choices = [(1, 'DongCheng'), (2, 'FengTai'),
        (3, 'TongZhou'), (4, 'DaXing'), (5, 'FangShan'), (6, 'ChangPing'), (7, 'ChaoYang'),
        (8, 'HaiDian'), (9, 'ShiJingShan'), (10, "XiCheng"), (11, 'PingGu'), (12, 'MenTouGou'),
        (13, 'ShunYi')], validators=[DataRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Your Comment', validators=[DataRequired()])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')


# render_kw: https://www.cnblogs.com/FRESHMANS/p/8529992.html
class SignupForm(FlaskForm):
    username = StringField('', validators=[DataRequired()], description="Username",
                           render_kw={"class": "form-control", "placeholder": "Username", "required": 'required'})
    email = StringField('', validators=[DataRequired()],
                        render_kw={"class": "form-control", "placeholder": "Email", "required": 'required'})
    password = PasswordField('', validators=[DataRequired()],
                             render_kw={"class": "form-control", "placeholder": "Password", "required": 'required'})
    password2 = PasswordField('', validators=[DataRequired()],
                              render_kw={"class": "form-control", "placeholder": "Repeat Password",
                                         "required": 'required'})

    submit = SubmitField('Register')
