from houseapp import db
from datetime import datetime, date

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    comment = db.relationship('Comment', backref='author', lazy='dynamic')
    answer = db.relationship('Answer', backref='author', lazy='dynamic')
    house = db.relationship('House', backref='owner', lazy='dynamic')
    recommendation = db.relationship('Recommendation', backref='author', lazy='dynamic')
    favorite = db.relationship('Favorite', backref='user', lazy='dynamic')
    private_com = db.Column(db.Integer, default=0)
    private_fav = db.Column(db.Integer, default=0)
    order = db.Column(db.Integer, default=0)
    background = db.relationship('Background', backref='owner', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Check(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    total_price = db.Column(db.Integer)
    average_price = db.Column(db.Integer)
    square = db.Column(db.Integer)
    living_room = db.Column(db.Integer)
    drawing_room = db.Column(db.Integer)
    kitchen = db.Column(db.Integer)
    bathroom = db.Column(db.Integer)
    floor = db.Column(db.Integer)
    building_type = db.Column(db.Integer)
    renovation_con = db.Column(db.Integer)
    elevator = db.Column(db.Integer)
    subway = db.Column(db.Integer)

class Checked(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    total_price = db.Column(db.Integer)
    average_price = db.Column(db.Float)
    square = db.Column(db.Float)
    living_room = db.Column(db.Integer)
    drawing_room = db.Column(db.Integer)
    kitchen = db.Column(db.Integer)
    bathroom = db.Column(db.Integer)
    floor = db.Column(db.Integer)
    building_type = db.Column(db.Integer)
    renovation_con = db.Column(db.Integer)
    elevator = db.Column(db.Boolean)
    subway = db.Column(db.Boolean)
    house_id = db.Column(db.Integer, db.ForeignKey('house.id'))

class House(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    lng = db.Column(db.Float)
    lat = db.Column(db.Float)
    total_price = db.Column(db.Integer)
    square = db.Column(db.Float)
    living_room = db.Column(db.Integer)
    drawing_room = db.Column(db.Integer)
    kitchen = db.Column(db.Integer)
    bathroom = db.Column(db.Integer)
    floor = db.Column(db.Integer)
    building_type = db.Column(db.Integer)
    renovation_con = db.Column(db.Integer)
    elevator = db.Column(db.Integer)
    subway = db.Column(db.Integer)
    district = db.Column(db.Integer)
    status = db.Column(db.Integer) #0:pending; 1: finshed; 2: uploaded
    date = db.Column(db.Date, index=True, default = datetime.now)
    comment = db.relationship('Comment', backref='house', lazy='dynamic')
    recommendation = db.relationship('Recommendation', backref='house', lazy='dynamic')
    image = db.relationship('Image', backref='house', lazy='dynamic')
    rank = db.Column(db.Integer, default=0) #用户收藏 +1

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    house_id = db.Column(db.Integer, db.ForeignKey('house.id'))

class Recommendation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    house_id = db.Column(db.Integer, db.ForeignKey('house.id'))
    reason = db.Column(db.String)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String)
    filepath = db.Column(db.String)
    house_id = db.Column(db.Integer, db.ForeignKey('house.id'))

class Background(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String)
    filepath = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    type = db.Column(db.Integer) #0:头像；1:背景图

    
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    answers = db.relationship('Answer', backref='question', lazy='dynamic')
    house_id = db.Column(db.Integer, db.ForeignKey('house.id'))

    def __repr__(self):
        return '<At {} : {} >'.format(str(self.timestamp)[0:10],self.body)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now)
    question_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Money(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    house_id = db.Column(db.Integer, db.ForeignKey('house.id'))
    price_percentage = db.Column(db.Integer)
    month = db.Column(db.Integer)
    money_type = db.Column(db.Integer)
    house_number = db.Column(db.Integer)
    error_type = db.Column(db.Integer)
