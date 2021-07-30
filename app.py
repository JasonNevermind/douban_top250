from flask import Flask,render_template,request
import datetime
import sqlite3


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!你好世界！"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/movie")
def movie():
    datalist=[]
    con = sqlite3.connect("movie250.db")
    c=con.cursor()
    sql='''
        select * from movie250
    '''
    data = c.execute(sql)
    #不能直接断开数据库，data因为游标的关闭而缺失数据，先保存
    for i in data:
        datalist.append(i)
    con.commit()
    con.close()
    return render_template("movie.html",list=datalist)

@app.route("/score")
def score():
    num=[]
    score=[]
    con = sqlite3.connect("movie250.db")
    c=con.cursor()
    sql='''
        select rating,count(rating) from movie250 group by rating
    '''
    data = c.execute(sql)
    #不能直接断开数据库，data因为游标的关闭而缺失数据，先保存
    for i in data:
        score.append(i[0])
        num.append(i[1])
    con.commit()
    con.close()
    return render_template("score.html",score=score,num=num)

@app.route("/word")
def word():
    return render_template("word.html")

@app.route("/team")
def team():
    return render_template("team.html")

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5000)


