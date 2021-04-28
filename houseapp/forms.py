from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, IntegerField, RadioField, SelectField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class BuyForm(FlaskForm):
    price = SelectField('Price', choices = [(0,'All Price'),(1,'Below ¥1M'),(2,'¥1M - ¥3M'),(3,'¥3M - ¥5M'),(4,'¥5M - ¥10M'),(5,'Over ¥10M')])
    average_price = SelectField('Average Price', choices=[(0,'All Average Price'),(1,'Below ¥10K'),(2,'¥10K - ¥30K'),(3,'¥30K - ¥50K'),(4,'¥50K - ¥100K'),(5,'Over ¥100K')])
    square = SelectField('Square', choices=[(0,'All Square'),(1,'Below 50sq.m.'),(2,'50sq.m. - 100sq.m.'),(3,'100sq.m. - 150sq.m.'),(4,'150sq.m. - 200sq.m.'),(5,'Over 200sq.m.')])
    living_room = SelectField('Living Room', choices=[(0,'All Living Room'),(1,0),(2,1),(3,2),(4,3),(5,4),(6,5),(7,6),(8,7),(9,8),(10,9)])
    drawing_room = SelectField('Drawing Room', choices=[(0,'All Drawing Room'),(1,0),(2,1),(3,2),(4,3),(5,4),(6,5),(7,6),(8,7),(9,8),(10,9)])
    kitchen = SelectField('*Kitchen', choices = [(0,'All Kitchen'),(1,0),(2,1),(3,2),(4,3),(5,4),(6,5)])
    bathroom = SelectField('Bathroom', choices = [(0,'All Bathroom'),(1,0),(2,1),(3,2),(4,3),(5,4),(6,5),(7,6),(8,7)])
    floor = SelectField('Floor',choices=[(0,'All Floor'),(1,'1st - 3rd'),(2,'4th - 10th'),(3,'11th - 20th'),(4,'Over 21st')])
    building_type = SelectField('Type',choices = [(0,'All Type'),(1,"Tower"), (2, "Bungalow"), (3, "Combination of plate and tower"), (4, "Plate")])
    renovation_con = SelectField('Renovation', choices = [(0,'All Renovation'),(1, 'Other'), (2, 'Rough'),(3, 'Simplicity'), (4, 'Hardcover')])
    elevator = SelectField('Elevator', choices = [(0,'Anyway'),(1, 'No'), (2, 'Yes')])
    subway = SelectField('Subway', choices = [(0,'Anyway'),(1, 'No'), (2, 'Yes')])
    check = SubmitField('Check')

class PredictForm(FlaskForm):
    lng = StringField('Lng')
    lat = StringField('Lat')
    square = StringField('*Square', validators=[DataRequired()])
    living_room = SelectField('*Bedroom', choices = [
        (0,0),(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9)]
        , validators=[DataRequired()]) #0-9
    drawing_room = SelectField('*Drawing Room', choices = [
        (0,0),(1,1),(2,2),(3,3),(4,4),(5,5)], validators=[DataRequired()]) #0-5
    kitchen = SelectField('*Kitchen', choices = [
        (0,0),(1,1),(2,2),(3,3),(4,4),(5,5)], validators=[DataRequired()]) #0-5
    bathroom = SelectField('*Bathroom', choices = [
        (0,0),(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7)], validators=[DataRequired()]) #0-7
    floor = IntegerField('*Floor', validators=[DataRequired()])
    building_type = SelectField('Building Type', choices = [
        (1,"Tower"), (2, "Bungalow"), (3, "Combination of plate and tower"), (4, "Plate")])
    renovation_con = SelectField('Renovation Condition', choices = [
        (1, 'Other'), (2, 'Rough'),(3, 'Simplicity'), (4, 'Hardcover')])
    elevator = SelectField('*Elevator', choices=[(0,'Not Available'),(1,'Available')], validators=[DataRequired()])
    subway = SelectField('*Subway', choices=[(0,'Not Available'),(1,'Available')], validators=[DataRequired()])

    district = SelectField('*District', choices = [(1, 'DongCheng'), (2, 'FengTai'),
        (3, 'TongZhou'), (4, 'DaXing'), (5, 'FangShan'), (6, 'ChangPing'), (7, 'ChaoYang'),
        (8, 'HaiDian'), (9, 'ShiJingShan'), (10, "XiCheng"), (11, 'PingGu'), (12, 'MenTouGou'),
        (13, 'ShunYi')], validators=[DataRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Your Comment', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ReplyForm(FlaskForm):
    comment = TextAreaField('Your Reply', validators=[DataRequired()])
    submit = SubmitField('Reply')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')

class RecommendationForm(FlaskForm):
    reason = TextAreaField('Recommendation', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EditRecomForm(FlaskForm):
    reason = TextAreaField('Recommendation', validators=[DataRequired()])
    edit = SubmitField('Edit')
    #delete = SubmitField('Delete')

class EditHouseForm(FlaskForm):
    price = StringField('Total Price', validators=[DataRequired()])
    reason = TextAreaField('Recommendation', validators=[DataRequired()])
    img = FileField('Image')
    # , validators=[FileAllowed(['jpg', 'png'], 'only .jpg or .png are accepted')]
    submit = SubmitField('Save')


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

    submit = SubmitField('Sign Up')
