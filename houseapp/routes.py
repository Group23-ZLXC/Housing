from houseapp import app, db, Config, model
from flask import render_template, flash, redirect, url_for, session, request, jsonify
from houseapp.forms import CommentForm, LoginForm, SignupForm, PredictForm, BuyForm, RecommendationForm, EditRecomForm, ReplyForm, EditHouseForm
from werkzeug.security import generate_password_hash, check_password_hash
from houseapp.models import User, House, Comment, Answer, Check, Recommendation, Favorite, Checked, Image
from houseapp.static import data
import numpy as np
import datetime

from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, User=User, House=House, Comment=Comment, Answer=Answer, Check=Check,
        Recommendation=Recommendation, Favorite=Favorite, Checked=Checked, Image=Image)
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@app.route('/')
@app.route('/homepage', methods=['GET'])
def homepage():
    owner = User.query.all()
    houses = House.query.filter(House.status == 2).order_by(House.id.desc()).limit(11)
    recommendations = Recommendation.query.all()
    # data = []
    # with open(r"houseapp/static/data/total_data.csv", encoding='gbk', errors='ignore') as fin:
    #     is_first_line =True
    #     for f in fin.readlines():
    #         if is_first_line:
    #             is_first_line = False
    #             continue
    #         f = f[:-1]
    #         a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z = f.split(",")
    #         data.append((a,b,c,d,e,f[0:4],g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z))
    # year=[0,0,0,0,0,0,0,0,0,0]
    # price=0
    # followers=0
    # for d in data:
    #     if d[5] == "2010":
    #         year[1]+=1
    #     if d[5] == "2011":
    #         year[2]+=1
    #     if d[5] == "2012":
    #         year[3]+=1
    #     if d[5] == "2013":
    #         year[4]+=1
    #     if d[5] == "2014":
    #         year[5]+=1
    #     if d[5] == "2015":
    #         year[6]+=1
    #     if d[5] == "2016":
    #         year[7]+=1
    #     if d[5] == "2017":
    #         year[8]+=1
    #     if d[5] == "2018":
    #         year[9]+=1
    #     if d[5] == "2002" or d[5] == "2003" or d[5] == "2008" or d[5] == "2009":
    #         year[0]+=1
    #     price+=float(d[8])/100000
    #     followers+=int(d[7])
    if not session.get("USERNAME") is None:
        username = session.get("USERNAME")
        user_in_db = User.query.filter(User.username == username).first()
        return render_template('homepage.html', title='Home', user=user_in_db, owner=owner,houses=houses,recommendations=recommendations)
    return render_template('homepage.html', owner=owner,houses=houses,recommendations=recommendations)

@app.route('/tips')
def tips():
    houses = House.query.filter(House.status == 2).all()
    liv_0 = House.query.filter(House.status == 2).filter(House.living_room == 0).count()
    liv_1 = House.query.filter(House.status == 2).filter(House.living_room == 1).count()
    liv_2 = House.query.filter(House.status == 2).filter(House.living_room == 2).count()
    liv_3 = House.query.filter(House.status == 2).filter(House.living_room == 3).count()
    liv_4 = House.query.filter(House.status == 2).filter(House.living_room == 4).count()
    liv_5 = House.query.filter(House.status == 2).filter(House.living_room == 5).count()
    dra_0 = House.query.filter(House.status == 2).filter(House.drawing_room == 0).count()
    dra_1 = House.query.filter(House.status == 2).filter(House.drawing_room == 1).count()
    dra_2 = House.query.filter(House.status == 2).filter(House.drawing_room == 2).count()
    dra_3 = House.query.filter(House.status == 2).filter(House.drawing_room == 3).count()
    dra_4 = House.query.filter(House.status == 2).filter(House.drawing_room == 4).count()
    dra_5 = House.query.filter(House.status == 2).filter(House.drawing_room == 5).count()
    kit_0 = House.query.filter(House.status == 2).filter(House.kitchen == 0).count()
    kit_1 = House.query.filter(House.status == 2).filter(House.kitchen == 1).count()
    kit_2 = House.query.filter(House.status == 2).filter(House.kitchen == 2).count()
    kit_3 = House.query.filter(House.status == 2).filter(House.kitchen == 3).count()
    kit_4 = House.query.filter(House.status == 2).filter(House.kitchen == 4).count()
    kit_5 = House.query.filter(House.status == 2).filter(House.kitchen == 5).count()
    bat_0 = House.query.filter(House.status == 2).filter(House.bathroom == 0).count()
    bat_1 = House.query.filter(House.status == 2).filter(House.bathroom == 1).count()
    bat_2 = House.query.filter(House.status == 2).filter(House.bathroom == 2).count()
    bat_3 = House.query.filter(House.status == 2).filter(House.bathroom == 3).count()
    bat_4 = House.query.filter(House.status == 2).filter(House.bathroom == 4).count()
    bat_5 = House.query.filter(House.status == 2).filter(House.bathroom == 5).count()

    squ_1 = House.query.filter(House.status == 2).filter(House.square < 50).count()
    squ_2 = House.query.filter(House.status == 2).filter(House.square > 50).filter(House.square < 100).count()
    squ_3 = House.query.filter(House.status == 2).filter(House.square > 100).filter(House.square < 150).count()
    squ_4 = House.query.filter(House.status == 2).filter(House.square > 150).filter(House.square < 200).count()
    squ_5 = House.query.filter(House.status == 2).filter(House.square > 200).count()

    tot_1 = House.query.filter(House.status == 2).filter(House.total_price < 1000000).count()
    tot_2 = House.query.filter(House.status == 2).filter(House.total_price > 1000000).filter(House.total_price < 3000000).count()
    tot_3 = House.query.filter(House.status == 2).filter(House.total_price > 3000000).filter(House.total_price < 5000000).count()
    tot_4 = House.query.filter(House.status == 2).filter(House.total_price > 5000000).filter(House.total_price < 10000000).count()
    tot_5 = House.query.filter(House.status == 2).filter(House.total_price > 10000000).count()

    ave_1 = House.query.filter(House.status == 2).filter(House.total_price/House.square < 10000).count()
    ave_2 = House.query.filter(House.status == 2).filter(House.total_price/House.square > 10000).filter(House.total_price/House.square < 30000).count()
    ave_3 = House.query.filter(House.status == 2).filter(House.total_price/House.square > 30000).filter(House.total_price/House.square < 50000).count()
    ave_4 = House.query.filter(House.status == 2).filter(House.total_price/House.square > 50000).filter(House.total_price/House.square < 100000).count()
    ave_5 = House.query.filter(House.status == 2).filter(House.total_price/House.square > 100000).count()

    data_living=[liv_0,liv_1,liv_2,liv_3,liv_4,liv_5]
    data_drawing=[dra_0,dra_1,dra_2,dra_3,dra_4,dra_5]
    data_kitchen=[kit_0,kit_1,kit_2,kit_3,kit_4,kit_5]
    data_bathroom=[bat_0,bat_1,bat_2,bat_3,bat_4,bat_5]
    square = [squ_1,squ_2,squ_3,squ_4,squ_5]
    total_price = [tot_1,tot_2,tot_3,tot_4,tot_5]
    average_price = [ave_1,ave_2,ave_3,ave_4,ave_5]

    return render_template('tips.html', data_living=data_living, data_drawing=data_drawing,data_kitchen=data_kitchen,data_bathroom=data_bathroom,square=square,total_price=total_price,average_price=average_price)

@app.route('/details', methods=['GET','POST'])
def details():
    house_id = request.args.get('house_id')
    comment_id = request.args.get('comment_id')
    reply = request.args.get('reply')
    house = House.query.filter(House.id == house_id).first()
    owner = User.query.filter(User.id == house.user_id).first()
    stored_images = Image.query.filter(Image.house_id == house.id).all()
    image_names = []
    if stored_images:
        for i in stored_images:
            image_names.append(i.filename)
    comments = Comment.query.filter(Comment.house_id == house.id).all()
    answers = {}
    for c in comments:
        answers[c.id] = Answer.query.filter(Answer.question_id == c.id).all()

    stored_recomm = Recommendation.query.filter(Recommendation.house_id == house.id).first()
    # recom_id = request.args.get('recom_id')
    form = CommentForm()
    form1 = RecommendationForm()
    form2 = EditRecomForm()
    form3 = ReplyForm()
    if not session.get("USERNAME") is None:
        username = session.get("USERNAME")
        user_in_db = User.query.filter(User.username == username).first()
        favorite = Favorite.query.filter(Favorite.user_id == user_in_db.id, Favorite.house_id == house.id).first()
        if not reply is None:
            if form3.validate_on_submit():
                answer = Answer(body=form3.comment.data,question_id=comment_id, user_id=user_in_db.id)
                db.session.add(answer)
                db.session.commit()
                return redirect(url_for('details', house_id=house.id))
            else:
                # form3.comment.data = "Reply to "+ comment_id +" : "
                return render_template('details.html', title='Details', form=form, form1=form1, user=user_in_db, house = house, owner=owner, comments=comments,
                    stored_recomm=stored_recomm, favorite=favorite, form2=form2,form3=form3, reply=reply, answers=answers, stored_images=stored_images, image_names=image_names)
        else:
            if form.validate_on_submit():
                comment = Comment(body=form.comment.data, user_id = user_in_db.id, house_id = house.id)
                db.session.add(comment)
                db.session.commit()
                return redirect(url_for('details', house_id=house.id))

        if stored_recomm:
            if form2.validate_on_submit():
                stored_recomm.reason = form2.reason.data
                db.session.commit()
                return redirect(url_for('details', house_id=house.id))
            else:
                form2.reason.data = stored_recomm.reason
                return render_template('details.html', title='Details', form=form, form1=form1, user=user_in_db,
                    house = house, owner=owner, comments=comments, stored_recomm=stored_recomm, favorite=favorite,
                    form2=form2,form3=form3, reply=reply, answers=answers, stored_images=stored_images, image_names=image_names)

        else:
            if form1.validate_on_submit():
                recommendation = Recommendation(reason=form1.reason.data, user_id=user_in_db.id, house_id=house.id)
                db.session.add(recommendation)
                db.session.commit()
                return redirect(url_for('details', house_id=house.id))
            else:
                return render_template('details.html', title='Details', form=form, form1=form1, user=user_in_db, house = house,
                    owner=owner, comments=comments, favorite=favorite, form3=form3, reply=reply, answers=answers,
                    stored_images=stored_images, image_names=image_names)

    return render_template('details.html', title='Details', form=form, form1=form1, house=house, owner=owner, commennts=comments,
        stored_recomm=stored_recomm,form3=form3, reply=reply, answers=answers, stored_images=stored_images, image_names=image_names)


@app.route('/upload_house')
def upload_house():
    house_id = request.args.get('house_id1')
    house_in_db = House.query.filter(House.id == house_id).first()
    house_in_db.status = 2
    db.session.commit()
    stored_recomm = Recommendation.query.filter(Recommendation.house_id == house_in_db.id).first()
    return redirect(url_for('details', house_id=house_id, stored_recomm=stored_recomm))

@app.route('/add_to_favorite')
def add_to_favorite():
    user_id = request.args.get('user_id2')
    house_id = request.args.get('house_id2')
    favorite = Favorite(user_id=user_id, house_id=house_id)
    db.session.add(favorite)
    db.session.commit()
    return redirect(url_for('details', house_id=house_id))

@app.route('/remove_favorite')
def remove_favorite():
    house_id = request.args.get('house_id2')
    user_id = request.args.get('user_id2')
    favorite_in_db = Favorite.query.filter(Favorite.house_id == house_id, Favorite.user_id == user_id).first()
    db.session.delete(favorite_in_db)
    db.session.commit()
    return redirect(url_for('details', house_id=house_id))

# @app.route('/edit_recom')
# def edit_recom():
#     recom_id = request.args.get('recom_id')

@app.route('/buy', methods=['GET','POST'])
def buy():
    form = BuyForm()
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
    # read file
    checked_data = []
    checked_data_1 = []
    # for d in data:
    #     if d[21] == '1':
    #         ele = True
    #     if d[21] == '0':
    #         ele = False
    #     if d[23] == '1':
    #         sub = True
    #     if d[23] == '0':
    #         sub = False
    #     house = House(user_id = 4, lng=d[2], lat = d[3],total_price=round(float(d[8])*10000), square = d[10],
    #     living_room=d[11], drawing_room=d[12], kitchen=d[13],
    #     bathroom = d[14], floor=d[15], building_type = d[16],
    #     renovation_con = d[18], elevator=ele, subway=sub,
    #     district = d[24], status = 2)
    #     db.session.add(house)
    #     db.session.commit()
    houses = House.query.filter(House.status == 2).all()
    houses_recent = House.query.filter(House.status == 2).order_by(House.id.desc()).limit(4)
    if not session.get("USERNAME") is None:
        username = session.get("USERNAME")
        user_in_db = User.query.filter(User.username == username).first()
        if form.validate_on_submit():
            check = Check(user_id = user_in_db.id, total_price = form.price.data, average_price = form.average_price.data, square = form.square.data,
                living_room=form.living_room.data, drawing_room=form.drawing_room.data, kitchen=form.kitchen.data,
                bathroom = form.bathroom.data, floor=form.floor.data, building_type = form.building_type.data,
                renovation_con = form.renovation_con.data, elevator=form.elevator.data, subway=form.subway.data)
            db.session.add(check)
            db.session.commit()
            # checked_before = Checked.query.all()
            db.session.query(Checked).filter(Checked.user_id == user_in_db.id).delete()
            db.session.commit()
            # Checked.query.delete()
            for house in houses:
                checked_data_1.append((house.user_id, house.total_price, round(house.total_price/house.square, 2), house.square, house.living_room, house.drawing_room, house.kitchen, house.bathroom, house.floor, house.building_type, house.renovation_con, house.elevator, house.subway, house.id))
            if check.living_room != 0:
                for d in data:
                    if int(check.living_room) == int(d[11])+1:
                        checked_data.append(d)
                for i in range(len(checked_data_1)-1,-1,-1):
                    if int(check.living_room) != int(checked_data_1[i][4])+1:
                        checked_data_1.remove(checked_data_1[i])
            if check.living_room == 0:
                for d in data:
                    checked_data.append(d)
            if check.drawing_room != 0:
                for i in range(len(checked_data)-1,-1,-1):
                    if int(check.drawing_room) != int(checked_data[i][12])+1:
                        checked_data.remove(checked_data[i])
                for i in range(len(checked_data_1)-1,-1,-1):
                    if int(check.drawing_room) != int(checked_data_1[i][5])+1:
                        checked_data_1.remove(checked_data_1[i])
            if check.kitchen != 0:
                for i in range(len(checked_data)-1,-1,-1):
                    if int(check.kitchen) != int(checked_data[i][13])+1:
                        checked_data.remove(checked_data[i])
                for i in range(len(checked_data_1)-1,-1,-1):
                    if int(check.kitchen) != int(checked_data_1[i][6])+1:
                        checked_data_1.remove(checked_data_1[i])
            if check.bathroom != 0:
                for i in range(len(checked_data)-1,-1,-1):
                    if int(check.bathroom) != int(checked_data[i][14])+1:
                        checked_data.remove(checked_data[i])
                for i in range(len(checked_data_1)-1,-1,-1):
                    if int(check.bathroom) != int(checked_data_1[i][7])+1:
                        checked_data_1.remove(checked_data_1[i])
            if check.building_type != 0:
                for i in range(len(checked_data)-1,-1,-1):
                    if int(check.building_type) != int(checked_data[i][16]):
                        checked_data.remove(checked_data[i])
                for i in range(len(checked_data_1)-1,-1,-1):
                    if int(check.building_type) != int(checked_data_1[i][9]):
                        checked_data_1.remove(checked_data_1[i])
            if check.renovation_con != 0:
                for i in range(len(checked_data)-1,-1,-1):
                    if int(check.renovation_con) != int(checked_data[i][18]):
                        checked_data.remove(checked_data[i])
                for i in range(len(checked_data_1)-1,-1,-1):
                    if int(check.renovation_con) != int(checked_data_1[i][10]):
                        checked_data_1.remove(checked_data_1[i])
            if check.elevator != 0:
                for i in range(len(checked_data)-1,-1,-1):
                    if int(check.elevator) != int(checked_data[i][21])+1:
                        checked_data.remove(checked_data[i])
                for i in range(len(checked_data_1)-1,-1,-1):
                    if int(check.elevator) != int(checked_data_1[i][11])+1:
                        checked_data_1.remove(checked_data_1[i])
            if check.subway != 0:
                for i in range(len(checked_data)-1,-1,-1):
                    if int(check.subway) != int(checked_data[i][23])+1:
                        checked_data.remove(checked_data[i])
                for i in range(len(checked_data_1)-1,-1,-1):
                    if int(check.subway) != int(checked_data_1[i][12])+1:
                        checked_data_1.remove(checked_data_1[i])
            if check.total_price == 1:
                for i in range(len(checked_data)-1,-1,-1):
                    if float(checked_data[i][8]) >= 100:
                        checked_data.remove(checked_data[i])
                for i in range(len(checked_data_1)-1,-1,-1):
                    if float(checked_data_1[i][1]) >= 1000000:
                        checked_data_1.remove(checked_data_1[i])
            if check.total_price == 2:
                for i in range(len(checked_data)-1,-1,-1):
                    if (float(checked_data[i][8]) < 100) | (float(checked_data[i][8]) >= 300):
                        checked_data.remove(checked_data[i])
                for i in range(len(checked_data_1)-1,-1,-1):
                    if (float(checked_data_1[i][1]) < 1000000) | (float(checked_data_1[i][1]) >= 3000000):
                        checked_data_1.remove(checked_data_1[i])
            if check.total_price == 3:
                for i in range(len(checked_data)-1,-1,-1):
                    if (float(checked_data[i][8]) < 300) | (float(checked_data[i][8]) >= 500):
                        checked_data.remove(checked_data[i])
                for i in range(len(checked_data_1)-1,-1,-1):
                    if (float(checked_data_1[i][1]) < 3000000) | (float(checked_data_1[i][1]) >= 5000000):
                        checked_data_1.remove(checked_data_1[i])
            if check.total_price == 4:
                for i in range(len(checked_data)-1,-1,-1):
                    if (float(checked_data[i][8]) < 500) | (float(checked_data[i][8]) >= 1000):
                        checked_data.remove(checked_data[i])
                for i in range(len(checked_data_1)-1,-1,-1):
                    if (float(checked_data_1[i][1]) < 5000000) | (float(checked_data_1[i][1]) >= 10000000):
                        checked_data_1.remove(checked_data_1[i])
            if check.total_price == 5:
                for i in range(len(checked_data)-1,-1,-1):
                    if (float(checked_data[i][8]) < 1000):
                        checked_data.remove(checked_data[i])
                for i in range(len(checked_data_1)-1,-1,-1):
                    if (float(checked_data_1[i][1]) < 10000000):
                        checked_data_1.remove(checked_data_1[i])
            if check.average_price == 1:
                for i in range(len(checked_data)-1,-1,-1):
                    if float(checked_data[i][9]) >= 10000:
                        checked_data.remove(checked_data[i])
                for i in range(len(checked_data_1)-1,-1,-1):
                    if (float(checked_data_1[i][2]) >= 10000):
                        checked_data_1.remove(checked_data_1[i])
            if check.average_price == 2:
                for i in range(len(checked_data)-1,-1,-1):
                    if (float(checked_data[i][9]) < 10000) | (float(checked_data[i][9]) >= 30000):
                        checked_data.remove(checked_data[i])
                for i in range(len(checked_data_1)-1,-1,-1):
                    if (float(checked_data_1[i][2]) < 10000) | (float(checked_data_1[i][2]) >= 30000):
                        checked_data_1.remove(checked_data_1[i])
            if check.average_price == 3:
                for i in range(len(checked_data)-1,-1,-1):
                    if (float(checked_data[i][9]) < 30000) | (float(checked_data[i][9]) >= 50000):
                        checked_data.remove(checked_data[i])
                for i in range(len(checked_data_1)-1,-1,-1):
                    if (float(checked_data_1[i][2]) < 30000) | (float(checked_data_1[i][2]) >= 50000):
                        checked_data_1.remove(checked_data_1[i])
            if check.average_price == 4:
                for i in range(len(checked_data)-1,-1,-1):
                    if (float(checked_data[i][9]) < 50000) | (float(checked_data[i][9]) >= 100000):
                        checked_data.remove(checked_data[i])
                for i in range(len(checked_data_1)-1,-1,-1):
                    if (float(checked_data_1[i][2]) < 50000) | (float(checked_data_1[i][2]) >= 100000):
                        checked_data_1.remove(checked_data_1[i])
            if check.average_price == 5:
                for i in range(len(checked_data)-1,-1,-1):
                    if (float(checked_data[i][9]) < 100000):
                        checked_data.remove(checked_data[i])
                for i in range(len(checked_data_1)-1,-1,-1):
                    if (float(checked_data_1[i][2]) < 100000):
                        checked_data_1.remove(checked_data_1[i])
            if check.square == 1:
                for i in range(len(checked_data)-1,-1,-1):
                    if (float(checked_data[i][10]) >= 50):
                        checked_data.remove(checked_data[i])
                for i in range(len(checked_data_1)-1,-1,-1):
                    if (float(checked_data_1[i][3]) >= 50):
                        checked_data_1.remove(checked_data_1[i])
            if check.square == 2:
                for i in range(len(checked_data)-1,-1,-1):
                    if (float(checked_data[i][10]) < 50) | (float(checked_data[i][10]) >= 100):
                        checked_data.remove(checked_data[i])
                for i in range(len(checked_data_1)-1,-1,-1):
                    if (float(checked_data_1[i][3]) < 50) | (float(checked_data_1[i][3]) >= 100):
                        checked_data_1.remove(checked_data_1[i])
            if check.square == 3:
                for i in range(len(checked_data)-1,-1,-1):
                    if (float(checked_data[i][10]) < 100) | (float(checked_data[i][10]) >= 150):
                        checked_data.remove(checked_data[i])
                for i in range(len(checked_data_1)-1,-1,-1):
                    if (float(checked_data_1[i][3]) < 100) | (float(checked_data_1[i][3]) >= 150):
                        checked_data_1.remove(checked_data_1[i])
            if check.square == 4:
                for i in range(len(checked_data)-1,-1,-1):
                    if (float(checked_data[i][10]) < 150) | (float(checked_data[i][10]) >= 200):
                        checked_data.remove(checked_data[i])
                for i in range(len(checked_data_1)-1,-1,-1):
                    if (float(checked_data_1[i][3]) < 150) | (float(checked_data_1[i][3]) >= 200):
                        checked_data_1.remove(checked_data_1[i])
            if check.square == 5:
                for i in range(len(checked_data)-1,-1,-1):
                    if (float(checked_data[i][10]) < 200):
                        checked_data.remove(checked_data[i])
                for i in range(len(checked_data_1)-1,-1,-1):
                    if (float(checked_data_1[i][3]) < 200):
                        checked_data_1.remove(checked_data_1[i])
            if check.floor == 1:
                for i in range(len(checked_data)-1,-1,-1):
                    if (int(checked_data[i][15]) > 3):
                        checked_data.remove(checked_data[i])
                for i in range(len(checked_data_1)-1,-1,-1):
                    if (int(checked_data_1[i][8]) > 3):
                        checked_data_1.remove(checked_data_1[i])
            if check.floor == 2:
                for i in range(len(checked_data)-1,-1,-1):
                    if (int(checked_data[i][15]) > 10) | (int(checked_data[i][15]) < 4):
                        checked_data.remove(checked_data[i])
                for i in range(len(checked_data_1)-1,-1,-1):
                    if (int(checked_data_1[i][8]) > 10) | (int(checked_data_1[i][8]) < 4):
                        checked_data_1.remove(checked_data_1[i])
            if check.floor == 3:
                for i in range(len(checked_data)-1,-1,-1):
                    if (int(checked_data[i][15]) > 20) | (int(checked_data[i][15]) < 11):
                        checked_data.remove(checked_data[i])
                for i in range(len(checked_data_1)-1,-1,-1):
                    if (int(checked_data_1[i][8]) > 20) | (int(checked_data_1[i][8]) < 11):
                        checked_data_1.remove(checked_data_1[i])
            if check.floor == 4:
                for i in range(len(checked_data)-1,-1,-1):
                    if (int(checked_data[i][15]) < 21):
                        checked_data.remove(checked_data[i])
                for i in range(len(checked_data_1)-1,-1,-1):
                    if (int(checked_data_1[i][8]) < 21):
                        checked_data_1.remove(checked_data_1[i])

            for i in range(0,len(checked_data_1)):
                checked_finally = Checked(user_id = user_in_db.id, total_price = checked_data_1[i][1], average_price = checked_data_1[i][2], square = checked_data_1[i][3],
                living_room=checked_data_1[i][4], drawing_room=checked_data_1[i][5], kitchen=checked_data_1[i][6],
                bathroom = checked_data_1[i][7], floor=checked_data_1[i][8], building_type = checked_data_1[i][9],
                renovation_con = checked_data_1[i][10], elevator=checked_data_1[i][11], subway=checked_data_1[i][12], house_id = checked_data_1[i][13])
                db.session.add(checked_finally)
                db.session.commit()

    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 5))

    paginate = Checked.query.order_by(Checked.id).filter(Checked.user_id == user_in_db.id).paginate(page, per_page, error_out=False)

    houses_checked = paginate.items

    return render_template('buy.html',title='Buy', data=data, user=user_in_db, houses=houses, form=form, checked=checked_data, checked_1=checked_data_1, paginate=paginate, houses_checked=houses_checked,houses_recent=houses_recent)

@app.route('/predict', methods=['GET','POST'])
def predict():
    form = PredictForm()
    if not session.get("USERNAME") is None:
        username = session.get("USERNAME")
        user_in_db = User.query.filter(User.username == username).first()
        if form.validate_on_submit():
            if form.lng.data == "":
                form.lng.data = 0.0
            if form.lat.data == "":
                form.lat.data = 0.0
            house = House(user_id = user_in_db.id, lng= form.lng.data, lat = form.lat.data, square = form.square.data,
                living_room=form.living_room.data, drawing_room=form.drawing_room.data, kitchen=form.kitchen.data,
                bathroom = form.bathroom.data, floor=form.floor.data, building_type = form.building_type.data,
                renovation_con = form.renovation_con.data, elevator=form.elevator.data, subway=form.subway.data,
                district = form.district.data, status = 0)
            db.session.add(house)
            db.session.commit()
            # call the ML model
            features = [house.lng, house.lat, house.square, house.living_room, house.drawing_room, house.kitchen, house.bathroom,
                house.building_type, house.renovation_con, house.elevator, house.subway, house.district]
            final_features = [np.array(features)]
            prediction = model.predict(final_features)
            output = round(prediction[0], 4)
            house.total_price = output*10000
            house.status = 1
            db.session.commit()
            return redirect(url_for('personal'))
            return redirect(url_for('edit_house', house_id=house.id))

        return render_template('predict.html', title='Predict', user=user_in_db, form=form)
    return render_template('predict.html', title='Predict', form=form)

@app.route('/map')
def map():
    return render_template('map.html', title='Lng and Lat')

@app.route('/delete_house')
def delete_house():
    house_id = request.args.get('house_id')
    house_in_db = House.query.filter(House.id == house_id).first()
    db.session.delete(house_in_db)
    db.session.commit()
    return redirect(url_for('personal'))


@app.route('/edit_house', methods=['GET','POST'])
def edit_house():
    if not session.get("USERNAME") is None:
        username = session.get("USERNAME")
        user_in_db = User.query.filter(User.username == username).first()
    house_id = request.args.get('house_id')
    house_in_db = House.query.filter(House.id == house_id).first()
    form = EditHouseForm()
    path = Config.IMG_DIR
    stored_images = Image.query.filter(Image.house_id == house_in_db.id).all()
    recommendation = Recommendation.query.filter(Recommendation.house_id == house_in_db.id).first()
    if recommendation:
        if form.validate_on_submit():
            house_in_db.total_price = form.price.data
            recommendation.reason = form.reason.data
            if form.img.data:
                nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                filename = form.img.data.filename
                file_path = path+nowTime+filename
                form.img.data.save(file_path)
                stored_path = 'static/img/'+nowTime+filename
                image = Image(filename = filename, filepath=stored_path, house_id=house_in_db.id)
                db.session.add(image)
            db.session.commit()
            return redirect(url_for('details', house_id=house_in_db.id, stored_recomm=recommendation, user=user_in_db, stored_images=stored_images))
        else:
            form.price.data = house_in_db.total_price
            form.reason.data = recommendation.reason
    else:
        if form.validate_on_submit():
            house_in_db.total_price = form.price.data
            recommendation = Recommendation(reason = form.reason.data, house_id = house_in_db.id, user_id = house_in_db.user_id)
            db.session.add(recommendation)
            if form.img.data:
                nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                filename = form.img.data.filename
                file_path = path+nowTime+filename
                form.img.data.save(file_path)
                stored_path = 'static/img/'+nowTime+filename
                image = Image(filename = filename, filepath=stored_path, house_id=house_in_db.id)
                db.session.add(image)
            db.session.commit()
            return redirect(url_for('details', house_id=house_in_db.id, stored_recomm=recommendation, user=user_in_db, stored_images=stored_images))
        else:
            form.price.data = house_in_db.total_price
    return render_template('edit_house.html', title='Edit', form=form, house=house_in_db, user=user_in_db, stored_images=stored_images)

@app.route('/delete_img')
def delete_img():
    img_id = request.args.get('img_id')
    img = Image.query.filter(Image.id == img_id).first()
    house_id = img.house_id
    db.session.delete(img)
    db.session.commit()
    return redirect(url_for('details', house_id=house_id))

@app.route('/visitothers')
def visitothers():
    user_id = request.args.get('user_id')
    user = User.query.filter(User.id == user_id).first()
    #visitor_id = request.args.get('visitor_id')
    return render_template('visitothers.html', user=user, title=user.username)

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
        favorites = Favorite.query.filter(Favorite.user_id == user_in_db.id).all()
        completed = 0
        uploaded = 0
        for h in houses:
            if h.status == 1:
                completed += 1
            if h.status == 2:
                uploaded += 1
        return render_template('personalpage.html', title="Personal Page", user=user_in_db, houses = houses, favorites=favorites,completed=completed,uploaded=uploaded)
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
