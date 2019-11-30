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
    if asal == 'Kota Bandung':
        asal = 'BD'
    elif asal == 'Kab. Bandung':
        asal = 'CCL'
    elif asal == 'Kab. Bandung Barat':
        asal = 'PDL'
    elif asal == 'Kota Sukabumi':
        asal = 'SI'
    elif asal == 'Kab. Sukabumi':
        asal = 'CBD'
    else:
        asal = 'XXX' #kereta tidak terdaftar
    
    tujuan = request.args.get('dest')
    if tujuan == 'Kota Bandung':
        tujuan = 'BD'
    elif tujuan == 'Kab. Bandung':
        tujuan = 'CCL'
    elif tujuan == 'Kab. Bandung Barat':
        tujuan = 'PDL'
    elif tujuan == 'Kota Sukabumi':
        tujuan = 'SI'
    elif tujuan == 'Kab. Sukabumi':
        tujuan = 'CBD'
    else:
        tujuan = 'XXX' #kereta tidak terdaftar

    tgl = request.args.get('Tanggal')
    bln = request.args.get('Bulan')
    thn = request.args.get('Tahun')
    data = requests.get('http://localhost:3000/kereta?dept=' + asal + '&dest=' + tujuan + '&date=' + tgl + '-' + bln + '-' + thn).json()
    return render_template("hasil.html", submit = data)

if __name__ == "__main__":
    app.run(debug=True)