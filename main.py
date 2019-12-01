from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    #API tempat
    data = requests.get('https://wiki-region-api.herokuapp.com/id/city/32').json() #hanya jawa barat
    return render_template("home.html", kota = data)
    
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/hasil", methods=['GET'])
def hasil():
    #API kereta api
    
    asal = request.args.get('dept')
    if asal == "Kota Bandung":
        asal = "BANDUNG"
    elif asal == 'Kab. Bandung':
        asal = 'BANDUNG'
    elif asal == 'Kab. Bandung Barat':
        asal = 'BANDUNG'
    elif asal == 'Kota Sukabumi':
        asal = 'SUKABUMI'
    elif asal == 'Kab. Sukabumi':
        asal = 'SUKABUMI'
    elif asal == 'Kota Cirebon':
        asal = 'CIREBON'
    else:
        asal = 'XXX' #kereta tidak terdaftar
    
    tujuan = request.args.get('dest')
    if tujuan == 'Kota Bandung':
        tujuan = 'BANDUNG'
    elif tujuan == 'Kab. Bandung':
        tujuan = 'BANDUNG'
    elif tujuan == 'Kab. Bandung Barat':
        tujuan = 'BANDUNG'
    elif tujuan == 'Kota Sukabumi':
        tujuan = 'SUKABUMI'
    elif tujuan == 'Kab. Sukabumi':
        tujuan = 'SUKABUMI'
    elif asal == "Kota Cirebon":
        asal = "CIREBON"
    else:
        tujuan = 'XXX' #kereta tidak terdaftar

    tgl = request.args.get('Tanggal')
    bln = request.args.get('Bulan')
    thn = request.args.get('Tahun')
    data = requests.get('http://localhost:8080/kereta?dept=' + asal + '&dest=' + tujuan + '&date=' + thn + '-' + bln + '-' + tgl).json()
    return render_template("hasil.html", submit = data)

if __name__ == "__main__":
    app.run(debug=True)
