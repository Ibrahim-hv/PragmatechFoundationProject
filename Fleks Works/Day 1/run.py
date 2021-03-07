from flask import Flask,render_template

app=Flask(__name__)
title='Sen fikirlesh burada neler ola bilerdi))'
@app.route("/")
def index():
    return render_template('index.html', data=title)

data=[
    {
        'id':1,
        'title':'Blogerlik ish deyil!',
        'content':"""
        What is Lorem Ipsum?
        Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry',
        """,
        'img':'../static/img/1.jpeg'

    },
    {
        'id':2,
        'title':'Reklamdan da boyuk ish var?',
        'content':"""It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters""",
        'img':'../static/img/2.jpeg'
    },
    {
        'id':3,
        'title':'Qubada yagan qar...',
        'content':"""
        It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters""",
        'img':'../static/img/3.jpg'
    }
]
@app.route("/about")
def about():
    return render_template('about.html', data=data)

if __name__=='__main__':
    app.run(debug=True)

