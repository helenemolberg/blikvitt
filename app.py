from flask import Flask, render_template, request, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask import json
from flask import Response
# from flask import request


import os
import config

'''Boolean for login-function'''
isLoggedIn = False

'''Database connection'''
application = Flask(__name__)
application.secret_key = os.urandom(12)
application.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URI

'''Using SQLAlchemy and Migrate'''
db = SQLAlchemy(application)
migrate = Migrate(application, db)

'''Know we can use flask command, can write flask db --help'''
manager = Manager(application)
manager.add_command('db', MigrateCommand)

'''Creating tables for the database'''


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stationname = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    comment = db.Column(db.String(200), nullable=True)


class PantFeedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pant_stationname = db.Column(db.String(50), nullable=False)
    pant_status = db.Column(db.String(50), nullable=False)
    pant_comment = db.Column(db.String(200), nullable=True)


class RecycleFeedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recycle_stationname = db.Column(db.String(50), nullable=False)
    recycle_status = db.Column(db.String(50), nullable=False)
    comment = db.Column(db.String(200), nullable=True)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80))

    def __repr__(self):
        return '<User %r>' % self.email


class RecycleData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    lat = db.Column(db.DECIMAL, nullable=False)
    long = db.Column(db.DECIMAL, nullable=False)
    comment = db.Column(db.String(80))


class FretexData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    lat = db.Column(db.DECIMAL, nullable=False)
    long = db.Column(db.DECIMAL, nullable=False)
    comment = db.Column(db.String(80))


class PantData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    postalcode = db.Column(db.Integer, nullable=False)
    lat = db.Column(db.DECIMAL, nullable=False)
    long = db.Column(db.DECIMAL, nullable=False)
    comment = db.Column(db.String(80))





'''Rendering html'''


@application.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('frontpage.html')
    else:
        return render_template('frontpage.html')


@application.route('/fretex', methods=('get', 'post'))
def fretex():
    if request.method == 'POST':
        form = request.form
        feedback = Feedback(stationname=form['station_name'], status=form['status'], comment=form['comment'])
        db.session.add(feedback)
        db.session.commit()

    feedback = Feedback.query.all()
    station_names = []
    statuses = []
    feedback_comments = []
    fretexData = FretexData.query.all()
    flats = []
    flongs = []
    fnames = []
    fcomments = []

    for r in feedback:
        tmp = station_names.append(str(r.stationname))
    for r in feedback:
        tmp = statuses.append(str(r.status))
    for r in feedback:
        tmp = feedback_comments.append(str(r.comment))
    for r in fretexData:
        tmp = flats.append(str(r.lat))
    for r in fretexData:
        tmp = flongs.append(str(r.long))
    for r in fretexData:
        tmp = fnames.append(str(r.name))
    for r in fretexData:
        tmp = fcomments.append(str(r.comment))
    return render_template('position_test.html', station_names=json.dumps(station_names),
                           statuses=json.dumps(statuses), feedback_comments=json.dumps(feedback_comments),
                           flats=json.dumps(flats), flongs=json.dumps(flongs),
                           fnames=json.dumps(fnames), fcomments=json.dumps(fcomments))


@application.route('/pant', methods=('get', 'post'))
def pant():
    if request.method == 'POST':
        form = request.form
        pant_feedback = PantFeedback(pant_stationname=form['pant_station_name'], pant_status=form['pant_status'],
                                     pant_comment=form['pant_comment'])
        db.session.add(pant_feedback)
        db.session.commit()

    pantData = PantData.query.all()
    plats = []
    plongs = []
    pnames = []
    pcomments = []
    pant_feedback = PantFeedback.query.all()
    pant_station_names = []
    pant_statuses = []
    pant_feedback_comments = []

    for r in pant_feedback:
        tmp = pant_station_names.append(str(r.pant_stationname))
    for r in pant_feedback:
        tmp = pant_statuses.append(str(r.pant_status))
    for r in pant_feedback:
        tmp = pant_feedback_comments.append(str(r.pant_comment))

    for p in pantData:
        tmp = plats.append(str(p.lat))

    for p in pantData:
        tmp = plongs.append(str(p.long))

    for p in pantData:
        tmp = pnames.append(str(p.name))

    for p in pantData:
        tmp = pcomments.append(str(p.comment))

    return render_template('pant.html', pant_station_names=json.dumps(pant_station_names),
                           pant_statuses=json.dumps(pant_statuses),
                           pant_feedback_comments=json.dumps(pant_feedback_comments),
                           plats=json.dumps(plats), plongs=json.dumps(plongs), pnames=json.dumps(pnames),
                           comments=json.dumps(pcomments))


@application.route('/recycle', methods=['GET', 'POST'])
def recycle():
    if request.method == 'POST':
        form = request.form
        recycle_feedback = PantFeedback(recycle_stationname=form['recycle_station_name'], recycle_status=form['recycle_status'],
                                        recycle_comment=form['recycle_comment'])
        db.session.add(recycle_feedback)
        db.session.commit()

    recData = RecycleData.query.all()
    lats = []
    longs = []
    names = []
    recycle_feedback = RecycleFeedback.query.all()
    recycle_station_names = []
    recycle_statuses = []
    recycle_feedback_comments = []

    for r in recycle_feedback:
        tmp = recycle_station_names.append(str(r.recycle_stationname))
    for r in recycle_feedback:
        tmp = recycle_statuses.append(str(r.recycle_status))
    for r in recycle_feedback:
        tmp = recycle_feedback_comments.append(str(r.recycle_comment))


    for r in recData:
        tmp = lats.append(str(r.lat))

    for r in recData:
        tmp = longs.append(str(r.long))

    for r in recData:
        tmp = names.append(str(r.name))

    return render_template('recycle.html', recycle_station_names=json.dumps(recycle_station_names),
                           recycle_statuses=json.dumps(recycle_statuses),
                           recycle_feedback_comments=json.dumps(recycle_feedback_comments),
                           lats=json.dumps(lats), longs=json.dumps(longs), names=json.dumps(names))


@application.route('/login', methods=('get', 'post'))
def login():
    if request.method == 'POST':
        form = request.form
        if User.query.filter_by(email=request.form['email']).count() > 0:
            if User.query.filter_by(password=request.form['password']).count() > 0:
                session['logged_in'] = True
                return render_template('frontpage.html', isLoggedIn=True, message=f'du er logget inn')
            else:
                return render_template('userLogin.html', message=f'Feil passord')
        else:
            return render_template('userLogin.html', message=f'Feil email')
    else:
        return render_template('userLogin.html', message='')


@application.route('/logout')
def logout():
    session['logged_in'] = False
    return home()


@application.route('/registeruser', methods=('get', 'post'))
def registeruser():
    if request.method == 'POST':
        form = request.form
        if User.query.filter_by(email=request.form['email']).count() > 0:
            return render_template('registerUser.html', message=f'{form["email"]} finnes allerede')
        user = User(email=form['email'], password=form['password'])
        db.session.add(user)
        db.session.commit()
        return render_template('registerUser.html', message=f'{user.email} er opprettet')
    else:
        return render_template('registerUser.html', message='Fyll inn nødvendig informasjon for å registrere bruker.')


if __name__ == '__main__':
    manager.run()

'''to create a new table use db.create_all()'''
