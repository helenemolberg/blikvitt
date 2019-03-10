from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

import config

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URI

db = SQLAlchemy(application)
migrate = Migrate(application, db)

'''Know we can use flask command, can write flask db --help'''
manager = Manager(application)
manager.add_command('db', MigrateCommand)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


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


@application.route('/login')
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


''''@application.route('/add_pant', methods=['GET', 'POST'])
def add_pant():
    with database_connection.cursor() as cursor:
        if request.method == 'POST':
            pant = request.form['pant']
            print(pant)
            cursor.execute("""
                insert into pant (value)
                values (%s)
            """, (pant,))
        database_connection.commit()
        cursor.execute('select * from pant')
        pant = cursor.fetchall()
    return render_template('add_pant.html', pant=pant)
'''

if __name__ == '__main__':
    manager.run()
