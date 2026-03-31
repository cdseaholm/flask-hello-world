from flask import Flask
import psycopg2
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from --Carl Seaholm-- in 3308'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://postgres3308_user:4mW94qBdAWY5TnzZHKaY3cdA0cV8uEkD@dpg-d761n7ea2pns73fmf080-a/postgres3308")
    conn.close()
    return 'Database Connection Successsful'

@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgresql://postgres3308_user:4mW94qBdAWY5TnzZHKaY3cdA0cV8uEkD@dpg-d761n7ea2pns73fmf080-a/postgres3308")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball (
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"
