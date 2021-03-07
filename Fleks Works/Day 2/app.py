from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
    surname=db.Column(db.String(50))
    email=db.Column(db.String(50))
    detail=db.Column(db.String(250))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new',methods=['GET','POST'])
def new():
    if request.method=='POST':
        ad=request.form['user_name']
        soyad=request.form['user_surname']
        email=request.form['user_email']
        detal=request.form['user_detail']
        user=User(name=ad,surname=soyad,email=email,detail=detal)
        db.session.add(user)
        db.session.commit()
        return redirect('/users')
    return render_template('new.html')

@app.route('/delete/<id>')
def delete(id):
    userForDelete=User.query.get(id)
    db.session.delete(userForDelete)
    db.session.commit()
    return redirect('/users')
# melumati deyisdir
@app.route('/update/<id>',methods=['GET','POST'])
def update(id):
    userForUpdate=User.query.get(id)
    if request.method=='POST':
        # form melumatlarini al
        ad=request.form['user_name']
        soyad=request.form['user_surname']
        email=request.form['user_email']
        detal=request.form['user_detail']
        # form melumatlarina esasen secilmis obyektin datalarini deyis
        userForUpdate.name=ad
        userForUpdate.surname=soyad
        userForUpdate.email=email
        userForUpdate.detail=detal
        db.session.commit()
        return redirect('/users')
    return  render_template('update.html',user=userForUpdate)

# istifade detallarini gor
@app.route('/detail/<id>')
def detail(id):
    userForShow=User.query.get(id)
    return render_template('detail.html',user=userForShow)

@app.route('/users')
def users():
    allUsers=User.query.all()
    return render_template('users.html',users=allUsers)

if __name__=='__main__':
    app.run(debug=True)

