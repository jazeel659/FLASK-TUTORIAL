from flask import Flask, render_template
import sqlite3
app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/gold')
def list():
    conn = get_db_connection()
    GOLD = conn.execute('SELECT * FROM GOLD').fetchall()
    conn.close()
    return render_template('index.html', GOLD=GOLD)


@app.route('/laxmi-price')
def laxmi():
    price = {}
    conn = get_db_connection()
    laxmi = conn.execute(
        """SELECT price FROM GOLD WHERE name='laxmi'""").fetchone()
    conn.close()
    price["price"] = laxmi["price"]
    return price


@app.route('/<brand>/gold')
def details(brand):
    details = {}
    conn = get_db_connection()
    detail = conn.execute(
        'SELECT * FROM GOLD WHERE name=?', (brand,)).fetchall()
    conn.close()
    details["name"] = detail[0][1]
    details["price"] = detail[0][2]
    details["purity"] = detail[0][1]
    details["Email"] = detail[0][3]
    details["image_url"] = detail[0][4]
    return details


@app.route('/')
def main():
    return render_template('main.html')
