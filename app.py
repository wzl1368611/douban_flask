from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/temp')
def temp():
    return render_template('temp.html')


@app.route('/index')
def home():
    # return render_template('index.html')
    return index()


@app.route('/movie')
def movie():
    datalist = []
    conn = sqlite3.connect("movie.db")
    cursor = conn.cursor()
    sql = "select * from movie250 "
    data = cursor.execute(sql)
    for item in data:
        datalist.append(item)
    conn.commit()
    cursor.close()
    conn.close()

    return render_template('movie.html', movies=datalist)


@app.route('/score')
def score():
    score = []
    num = []
    conn = sqlite3.connect("movie.db")
    cursor = conn.cursor()
    sql = "select  score,count(score) from movie250 group by score "
    data = cursor.execute(sql)
    for item in data:
        score.append(str(item[0]))
        num.append(item[1])
    conn.commit()
    cursor.close()
    conn.close()

    return render_template('score.html', score=score, num=num)


@app.route('/team')
def team():
    return render_template('team.html')


@app.route('/word')
def word():
    return render_template('word.html')


if __name__ == '__main__':
    app.run()
