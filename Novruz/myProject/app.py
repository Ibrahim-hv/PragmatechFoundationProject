from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
db=SQLAlchemy(app)




class Aptek(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    aptek=db.Column(db.String(70))
    eczaci=db.Column(db.String(70))
    tel=db.Column(db.String(70))
    textarea=db.Column(db.String(250))





@app.route("/")
def base():
    return render_template('base.html')


# Firmalari qeyde alan database:
@app.route("/firmalar")
def firma():
    return render_template('yFirma.html')


# Aptekleri qeyde alan database:
@app.route("/aptekler", methods=['GET','POST'])
def aptek():
    if request.method=='POST':
        aptek=request.form['aptek_name']
        eczaci=request.form['eczaci_name']
        telefon=request.form['eczaci_tel']
        qeyd=request.form['message']
        aptekler=Aptek(aptek=aptek, eczaci=eczaci, tel=telefon, textarea=qeyd)
        db.session.add(aptekler)
        db.session.commit()
        return redirect('/aptekler')
    ButunAptekler=Aptek.query.all()
    return render_template('yAptek.html', aptekler=ButunAptekler)

# Aptekler siyahisindan silmek ucun:
@app.route('/delete/<id>')
def delet(id):
    ForDelete=Aptek.query.get(id)
    db.session.delete(ForDelete)
    db.session.commit()
    return redirect('/aptekler')

# Hekimleri qeyde alan database:
@app.route("/hekimler")
def hekim():
    return render_template('yHekim.html')


# Dermanlari qeyde alan database:
@app.route("/dermanlar")
def derman():
    return render_template('yDerman.html')


if __name__=='__main__':
    app.run(debug=True)