from houseapp import app
from flask import render_template,url_for
from houseapp.forms import CommentForm

@app.route('/')
@app.route('/details')
def details():
    form = CommentForm()
    return render_template('details.html', form=form)

@app.route('/buy')
def buy():
    return render_template('buy.html')