from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

import config

'''Database connection'''
application = Flask(__name__)
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
        return '<User %r>' % self.username


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
def hello_world():
    return render_template('frontpage.html')


@application.route('/fretex')
def fretex():
    return render_template('fretex.html')


@application.route('/pant')
def pant():
    return render_template('pant.html')


@application.route('/recycle')
def recycle():
    return render_template('recycle.html')


@application.route('/login', methods=('get', 'post'))
def login():
    return render_template('userLogin.html')


@application.route('/registeruser', methods=('get', 'post'))
def registeruser():
    if request.method == 'POST':
        form = request.form
        if User.query.filter_by(username=request.form['email']).count() > 0:
            return render_template('registerUser.html', message=f'{form["email"]} already exists')
        user = User(username=form['email'], email=form['email'])
        db.session.add(user)
        db.session.commit()
        return render_template('registerUser.html', message=f'{user.username} created')
    else:
        return render_template('registerUser.html', message='Please fill in this form to create an account.')


if __name__ == '__main__':
    manager.run()


'''to create a new table use db.create_all()'''