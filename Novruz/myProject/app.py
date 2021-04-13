from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask_migrate import Migrate
import os

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database/data.db'
app.config['UPLOAD_PATH']='static/uploads'
db=SQLAlchemy(app)
migrate=Migrate(app,db)

class Aptek(db.Model):
    __tablename__='aptek'
    id=db.Column(db.Integer,primary_key=True)
    aptek=db.Column(db.String(70))
    eczaci=db.Column(db.String(70))
    tel=db.Column(db.String(70))
    a_textarea=db.Column(db.String(250))

class Firma(db.Model):
    __tablename__='firma'
    id=db.Column(db.Integer,primary_key=True)
    shirket=db.Column(db.String(70))
    email=db.Column(db.String(70))
    elaqe=db.Column(db.String(70))
    f_textarea=db.Column(db.String(250))
    operation_FA=db.relationship('Alish',backref='firma')

class Derman(db.Model):
    __tablename__='derman'
    id=db.Column(db.Integer,primary_key=True)
    barkod=db.Column(db.String(70))
    derman_adi=db.Column(db.String(70))
    terkib=db.Column(db.String(70))
    vahid=db.Column(db.String(70))
    ich_sayi=db.Column(db.String(70))
    tarix=db.Column(db.String(70))
    img=db.Column(db.String(120))
    d_textarea=db.Column(db.String(250))
    operation_DA=db.relationship('Alish',backref='derman')


class Hekim(db.Model):
    __tablename__='hekim'
    id=db.Column(db.Integer,primary_key=True)
    hekim_adi=db.Column(db.String(70))
    ixtisas=db.Column(db.String(70))
    telefon=db.Column(db.String(70))
    h_textarea=db.Column(db.String(250))


class Alish(db.Model):
    __tablename__='alish'
    id=db.Column(db.Integer,primary_key=True)
    tarix=db.Column(db.String(70))
    miqdar=db.Column(db.String(70))
    alish_qiymeti=db.Column(db.String(70))
    satish_qiymeti=db.Column(db.String(70))
    qeyd_yeri=db.Column(db.String(250))
    endirim=db.Column(db.String(70))
    barkod=db.Column(db.String(30))
    vahid=db.Column(db.String(10))
    mebleg=db.Column(db.String(70))
    firma_id=db.Column(db.Integer,db.ForeignKey('firma.id'))
    derman_id=db.Column(db.Integer,db.ForeignKey('derman.id'))


@app.route("/")
def base():
    return render_template('base.html')


# Firmalari qeyde alan database:
@app.route("/firmalar", methods=['GET','POST'])
def firma():
    if request.method=='POST':
        firma=request.form['firma_name']
        email=request.form['email']
        elaqe=request.form['elaqe']
        qeyd=request.form['message']
        firmalar=Firma(shirket=firma, email=email, elaqe=elaqe, f_textarea=qeyd)
        db.session.add(firmalar)
        db.session.commit()
        return redirect('/firmalar')
    ButunFirmalar=Firma.query.all()
    return render_template('yFirma.html', firmalar=ButunFirmalar)

# Firmalar siyahisindan silmek ucun:
@app.route('/f_delete/<id>')
def delet_f(id):
    F_Delete=Firma.query.get(id)
    db.session.delete(F_Delete)
    db.session.commit()
    return redirect('/firmalar')


# Aptekleri qeyde alan database:
@app.route("/aptekler", methods=['GET','POST'])
def aptek():
    if request.method=='POST':
        aptek=request.form['aptek_name']
        eczaci=request.form['eczaci_name']
        telefon=request.form['eczaci_tel']
        qeyd=request.form['message']
        aptekler=Aptek(aptek=aptek, eczaci=eczaci, tel=telefon, a_textarea=qeyd)
        db.session.add(aptekler)
        db.session.commit()
        return redirect('/aptekler')
    ButunAptekler=Aptek.query.all()
    return render_template('yAptek.html', aptekler=ButunAptekler)

# Aptekler siyahisindan silmek ucun:
@app.route('/a_delete/<id>')
def delet_a(id):
    A_Delete=Aptek.query.get(id)
    db.session.delete(A_Delete)
    db.session.commit()
    return redirect('/aptekler')

# Hekimleri qeyde alan database:
@app.route("/hekimler", methods=['GET','POST'])
def hekim():
    if request.method=='POST':
        hekim=request.form['hekim_name']
        ixtisas=request.form['hekim_ixtisas']
        tel_elaqe=request.form['tel_nom']
        qeyd=request.form['message']
        hekimler=Hekim(hekim_adi=hekim, ixtisas=ixtisas, telefon=tel_elaqe, h_textarea=qeyd)
        db.session.add(hekimler)
        db.session.commit()
        return redirect('/hekimler')
    ButunHekimler=Hekim.query.all()
    return render_template('yHekim.html', hekimler=ButunHekimler)

# Hekimlerler siyahisindan silmek ucun:
@app.route('/h_delete/<id>')
def delet_h(id):
    H_Delete=Hekim.query.get(id)
    db.session.delete(H_Delete)
    db.session.commit()
    return redirect('/hekimler')



# Dermanlari qeyde alan database:
@app.route("/dermanlar", methods=['GET','POST'])
def derman():
    if request.method=='POST':
        file=request.files['img']
        filename=secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_PATH'],filename))
        barkodu=request.form['barcode']
        adi=request.form['derman_name']
        terkibi=request.form['terkib']
        vahidi=request.form['vahid']
        ichsayi=request.form['ichsayi']
        tarixi=request.form['end_date']
        shekli=filename
        melumat=request.form['message']
        dermanlar=Derman(barkod=barkodu, derman_adi=adi, terkib=terkibi,
        vahid=vahidi, ich_sayi=ichsayi, tarix=tarixi, img=shekli, d_textarea=melumat)
        db.session.add(dermanlar)
        db.session.commit()
        return redirect('/dermanlar')
    ButunDermanlar=Derman.query.all()
    return render_template('yDerman.html', dermanlar=ButunDermanlar)

# Dermanlar siyahisindan silmek ucun:
@app.route('/d_delete/<id>')
def delet_d(id):
    D_Delete=Derman.query.get(id)
    db.session.delete(D_Delete)
    db.session.commit()
    return redirect('/dermanlar')

# Dermanlari yenilemek ucun: AMMA İŞLƏMİR!!!!!!!!!
@app.route('/d_yenile/<id>', methods=['GET','POST'])
def yenile(id):
    dermanYenile=Derman.query.get(id)
    if request.method=='POST':

        # form melumatlari
        terkibi=request.form['terkib']
        tarixi=request.form['end_date']
        melumat=request.form['message']

        # secilmish melumatlari yenile
        dermanYenile.terkib=terkibi
        dermanYenile.end_data=tarixi
        dermanYenile.message=melumat

        return redirect('/dermanlar')
    return render_template('Diger/dYenile.html', derman=dermanYenile)

# Derman Haqqinda
@app.route('/haqqinda/<id>')
def haqqinda(id):
    DermanHaqqinda=Derman.query.get(id)
    return render_template('Diger/dHaqqinda.html', derman=DermanHaqqinda)


# Emeliyyatlar Bolmesi
# Alish emeliyyati
@app.route("/alish", methods=['GET','POST'])
def alish():
    firma=Firma.query.all()
    derman=Derman.query.all()
    if request.method=='POST':
        shirket=request.form['firma']
        tarix=request.form['vaxt']
        barkodu=request.form['barkod']
        derman=request.form['malin_adi']
        vahidi=request.form['vahid']
        alish_miqdari=request.form['miqdar']
        anbarda_qaliq=request.form['qaliq']
        Aqiymeti=request.form['alish']
        Sqiymeti=request.form['satish']
        setir_cemi=request.form['məbleq']
        qeyd=request.form['kicik_qeyd']
        sutun_cemi=request.form['cem_mebleq']
        endirim=request.form['endirim']
        toplam=request.form['son_mebleq']
        emeliyyat=Alish(firma_id=shirket, tarix=tarix, barkod=barkodu, derman_id=derman,
        vahid=vahidi, miqdar=alish_miqdari, alish_qiymeti=Aqiymeti,
        satish_qiymeti=Sqiymeti, qeyd_yeri=qeyd, endirim=endirim, mebleg=toplam)
        db.session.add(emeliyyat)
        db.session.commit()
        return redirect('/alish')
    AlishEmeliyyati=Alish.query.all()
    return render_template('Emeliyyat/alish.html', emeliyyat=AlishEmeliyyati,
    firmalar=firma, dermanlar=derman)

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

# Digerler Bolmesi
# Derman Kataloqu
@app.route("/kataloq")
def katalog():
    ButunDermanlar=Derman.query.all()
    return render_template('Diger/dKatalog.html', dermanlar=ButunDermanlar)




if __name__=='__main__':
    app.run(debug=True)