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


@application.route('/fretex')
def fretex():
    return render_template('position_test.html')


@application.route('/pant')
def pant():
    return render_template('pant.html')


@application.route('/recycle', methods=['GET', 'POST'])

def recycle():
        recData = RecycleData.query.all()
        lats = []
        longs = []
        names = []

        for r in recData:
            tmp = lats.append(str(r.lat))

        for r in recData:
            tmp = longs.append(str(r.long))

        for r in recData:
            tmp = names.append(str(r.name))

        return render_template('recycle.html', lats=json.dumps(lats), longs=json.dumps(longs), names=json.dumps(names))


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
