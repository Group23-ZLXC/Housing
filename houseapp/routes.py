from houseapp import app, db
from flask import render_template, flash, redirect, url_for, session, request, jsonify
from houseapp.forms import CommentForm, LoginForm, SignupForm, PredictForm
from werkzeug.security import generate_password_hash, check_password_hash
from houseapp.models import User, House, Comment, Answer
from houseapp.static import data



@app.route('/')
@app.route('/homepage', methods=['GET'])
def homepage():
    owner = User.query
    if not session.get("USERNAME") is None:
        username = session.get("USERNAME")
        user_in_db = User.query.filter(User.username == username).first()
        return render_template('homepage.html', title='Home', user=user_in_db, owner=owner)
    return render_template('homepage.html', owner=owner)


@app.route('/details', methods=['GET','POST'])
def details():
    house_id = request.args.get('house_id')
    house = House.query.filter(House.id == house_id).first()
    owner = User.query.filter(User.id == house.user_id).first()
    form = CommentForm()
    if not session.get("USERNAME") is None:
        username = session.get("USERNAME")
        user_in_db = User.query.filter(User.username == username).first()
        if form.validate_on_submit():
            flash("upload")
        return render_template('details.html', title='Details', form=form, user=user_in_db, house = house, owner=owner)
            # here just wait the database for house
    return render_template('details.html', title='Details', form=form, house=house, owner=owner)


@app.route('/buy')
def buy():
     # read file
    if not session.get("USERNAME") is None:
        username = session.get("USERNAME")
        user_in_db = User.query.filter(User.username == username).first()
    data = []
    with open(r"houseapp/static/data/data.csv", encoding='gbk', errors='ignore') as fin:
        is_first_line =True
        for f in fin.readlines():
            if is_first_line:
                is_first_line = False
                continue
            f = f[:-1]
            a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z = f.split(",")
            data.append((a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z))
    return render_template('buy.html', data=data, user=user_in_db)

@app.route('/predict', methods=['GET','POST'])
def predict():
    form = PredictForm()

    if not session.get("USERNAME") is None:
        username = session.get("USERNAME")
        user_in_db = User.query.filter(User.username == username).first()
        if form.validate_on_submit():
            house = House(user_id = user_in_db.id, lng=form.lng.data, lat = form.lat.data, square = form.square.data,
                living_room=form.living_room.data, drawing_room=form.drawing_room.data, kitchen=form.kitchen.data,
                bathroom = form.bathroom.data, floor=form.floor.data, building_type = form.building_type.data,
                renovation_con = form.renovation_con.data, elevator=form.elevator.data, subway=form.subway.data,
                district = form.district.data, status = 0)
            db.session.add(house)
            db.session.commit()
            return redirect(url_for('personal'))
        return render_template('predict.html', title='Predict', user=user_in_db, form=form)


    return render_template('predict.html', title='Predict', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_in_db = User.query.filter(User.username == form.username.data).first()
        if not user_in_db:
            flash('No user found with username: {}'.format(form.username.data))
            return redirect(url_for('login'))
        if check_password_hash(user_in_db.password_hash, form.password.data):
            session["USERNAME"] = user_in_db.username
            print(session["USERNAME"])
            return redirect(url_for('homepage'))
        # should go to the logged-in page
        flash('Incorrect Password')
        return redirect(url_for('login'))
    return render_template('login.html', title='Log In', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        if form.password.data != form.password2.data:
            flash('Passwords do not match!')
            return redirect(url_for('signup'))
        user_in_db = User.query.filter(User.username == form.username.data).first()
        if user_in_db:
            flash('Username already existed!')
            return redirect(url_for('signup'))
        passw_hash = generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password_hash=passw_hash)
        db.session.add(user)
        db.session.commit()
        flash('User registered with username:{}'.format(form.username.data))
        session["USERNAME"] = user.username
        return redirect(url_for('login'))
    return render_template('signup.html', title='Register', form=form)

@app.route('/logout')
def logout():
    # session.pop("USERNAME", None)
    # return redirect(url_for('login'))
    return render_template('logout.html', title='Log Out')

@app.route('/personal')
def personal():
    if not session.get("USERNAME") is None:
        username = session.get("USERNAME")
        user_in_db = User.query.filter(User.username == username).first()
        houses = House.query.filter(House.user_id == user_in_db.id).all()
        return render_template('personalpage.html', title="Personal Page", user=user_in_db, houses = houses)
    else:
        flash("User needs to login first")
        return redirect(url_for('login'))

@app.route('/checkuser', methods=['POST'])
def check_username():
    chosen_name = request.form['username']
    user_in_db = User.query.filter(User.username == chosen_name).first()
    if not user_in_db:
        return jsonify({'text': 'Username is available',
                        'returnvalue': 0})
    else:
        return jsonify({'text': 'Sorry! Username is already taken',
                        'returvalue': 1})


@app.route('/checkemail', methods=['POST'])
def check_email():
    chosen_email = request.form['email']
    user_in_db = User.query.filter(User.email == chosen_email).first()
    if not user_in_db:
        return jsonify({'text': 'Email is available',
                        'returnvalue': 0})
    else:
        return jsonify({'text': 'Sorry! Email is already taken',
                        'returvalue': 1})
