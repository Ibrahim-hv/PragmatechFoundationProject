from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database/data.db'
db=SQLAlchemy(app)

class Aptek(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    sn=db.Column(db.Integer)
    aptek=db.Column(db.String(70))
    eczaci=db.Column(db.String(70))
    tel=db.Column(db.String(70))
    img=db.Column(db.String(120))
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


# Emeliyyatlar Bolmesi
# Alish emeliyyati
@app.route("/alish")
def alish():
    return render_template('Emeliyyat/alish.html')

# Satish emeliyyati
@app.route("/satish")
def satish():
    return render_template('Emeliyyat/satish.html')

# Alishdan GeriQaytarma emeliyyati
@app.route("/alishdan")
def alishdan_geri():
    return render_template('Emeliyyat/gAlishdan.html')

# Satishdan GeriQaytarma emeliyyati
@app.route("/satishdan")
def satishdan_geri():
    return render_template('Emeliyyat/gSatishdan.html')

# Kassa Medaxil emeliyyati
@app.route("/medaxil")
def kassa_medaxil():
    return render_template('Emeliyyat/kMedaxil.html')

# Kassa Mexaric emeliyyati
@app.route("/mexaric")
def kassa_mexaric():
    return render_template('Emeliyyat/kMexaric.html')

# Hekim Qeydi emeliyyati
@app.route("/hekimqeydi")
def hekim_qeydi():
    return render_template('Emeliyyat/hekimQeydi.html')


# Senedler Bölməsi
# Alish Senedleri
@app.route("/alishSenedleri")
def alish_Senedleri():
    return render_template('Senedler/alishSenedleri.html')

# Satish Senedleri
@app.route("/satishSenedleri")
def satish_Senedleri():
    return render_template('Senedler/satishSenedleri.html')

# Alishdan Geri Qaytarma Sənədləri
@app.route("/htamamlanmish")
def h_tamamlanmish():
    return render_template('Senedler/HQtamSened.html')

# Satishdan Geri Qaytarma Sənədləri
@app.route("/hyarimqalmish")
def h_yarimqalmish():
    return render_template('Senedler/HQyarimSened.html')

# Kassa Medaxil Senedleri
@app.route("/medaxilS")
def medaxilS():
    return render_template('Senedler/medaxilSened.html')

# Kassa Mexaric Senedleri
@app.route("/mexaricS")
def mexaricS():
    return render_template('Senedler/mexaricSened.html')

# Hekim Qeydi Tam Sənədlər
@app.route("/gSAlishdan")
def gSAlishdan():
    return render_template('Senedler/geriAlishSened.html')

# Həkim Qeydi Yarım Sənədlər
@app.route("/gSSatishdan")
def gSSatishdan():
    return render_template('Senedler/geriSatishSened.html')

# Bütün Sənədlər
@app.route("/ButunSenedler")
def ButunSenedler():
    return render_template('Senedler/butunSened.html')


# Hesabat Bölməsi
# Anbar Qalığı
@app.route("/anbarqaliqi")
def anbar_qaliqi():
    return render_template('Hesabatlar/anbarqaliq.html')

# Borc Firmalar
@app.route("/firmaborcu")
def firma_borcu():
    return render_template('Hesabatlar/borcFirmalar.html')

# Borc Apteklər
@app.route("/aptekborcu")
def aptek_borcu():
    return render_template('Hesabatlar/borcAptekler.html')

# Borc Həkimlər
@app.route("/hekimborcu")
def hekim_borcu():
    return render_template('Hesabatlar/borcHekimler.html')

# Alışdan geri qaytarma hesabatı
@app.route("/alishdanhesabat")
def alishdan_hesabat():
    return render_template('Hesabatlar/geriAlishHes.html')

# Satışdan geri qaytarma hesabatı
@app.route("/satishdanhesabat")
def satishdan_hesabat():
    return render_template('Hesabatlar/geriSatishHes.html')

# Firmalar üzrə hesabat
@app.route("/firmalarU")
def firmalar_U():
    return render_template('Hesabatlar/firmalarUzre.html')

# Apteklər üzrə hesabat
@app.route("/apteklerU")
def aptekler_U():
    return render_template('Hesabatlar/apteklerUzre.html')

# Həkimlər üzrə hesabat
@app.route("/hekimlerU")
def hekimler_U():
    return render_template('Hesabatlar/hekimlerUzre.html')

# Dərmanlar üzrə hesabat
@app.route("/dermanlarU")
def dermanlar_U():
    return render_template('Hesabatlar/dermanlarUzre.html')

# Balans
@app.route("/balans")
def balans():
    return render_template('Hesabatlar/balans.html')



if __name__=='__main__':
    app.run(debug=True)