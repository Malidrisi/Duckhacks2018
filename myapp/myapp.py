from flask import Flask, render_template
import sqlite3 as sql 


app = Flask(__name__)

def db_connect():
    """db connection"""
    con = sql.connect("duckhacks2018.db")
    cur = con.cursor()
    return con, cur
    
@app.route('/')
def index():
    """home page, get user info for January"""
    con,cur = db_connect()
    query = " select C.category_name, E.expected_value, A.actual, A.comment from Actual_Spendings as A join Category as C on A.category_id = C.category_id  join Expected_Spendings as E on A.category_id = E.category_id and A.user_id = E.user_id where A.month = 1 and A.user_id = 2"
    cur.execute(query)
    rows = cur.fetchall()
    data = [{'category_name': category_name, 'expected_value': expected_value, 'actual': actual, 'comment':comment} for category_name, expected_value, actual, comment in rows]
    con.close()
    return render_template('index.html', data=data)

@app.route('/feb/')
def feb():
    """get user info for feb and redirect to that page"""
    con,cur = db_connect()
    query = " select C.category_name, E.expected_value, A.actual, A.comment from Actual_Spendings as A join Category as C on A.category_id = C.category_id  join Expected_Spendings as E on A.category_id = E.category_id and A.user_id = E.user_id where A.month = 2 and A.user_id = 2"
    cur.execute(query)
    rows = cur.fetchall()
    print(rows)
    data = [{'category_name': category_name, 'expected_value': expected_value, 'actual': actual, 'comment':comment} for category_name, expected_value, actual, comment in rows]
    con.close()
    return render_template('feb.html', data=data)

@app.route('/mar/')
def mar():
    """get user info for feb and redirect to that page"""
    return render_template('mar.html')

@app.route('/apr/')
def apr():
    """get user info for feb and redirect to that page"""
    return render_template('apr.html')

if __name__ == "__main__":
    app.run(debug=True)