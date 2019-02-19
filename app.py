import psycopg2

from flask import Flask, render_template, request

import config

application = Flask(__name__)
database_connection = psycopg2.connect(config.DATABASE_URI)


@application.route('/')
def hello_world():
    return render_template('frontpage.html')


@application.route('/add_pant', methods=['GET', 'POST'])
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


if __name__ == '__main__':
    application.run()
