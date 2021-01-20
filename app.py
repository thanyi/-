from flask import Flask,render_template,request
import sqlite3
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/score')
def score():
    score = []
    num =[]
    conn = sqlite3.connect("./豆瓣电影.db")
    c = conn.cursor()
    sql = "select score,count(score) from movies group by score"
    data = c.execute(sql)
    for item in data:
        score.append(item[0])
        num.append(item[1])
    c.close()
    conn.close()
    return render_template("score.html",score = score,num = num)

@app.route('/movie')
def movie():
    datalist = []
    conn = sqlite3.connect("./豆瓣电影.db")
    c = conn.cursor()
    sql ="select * from movies"
    data = c.execute(sql)
    for item in data:
        datalist.append(item)
    c.close()
    conn.close()
    return render_template("movie.html",movies = datalist)

@app.route('/team')
def team():
    return render_template("team.html")

@app.route('/word')
def word():
    return render_template("word.html")


if __name__ == '__main__':
    app.run()
