from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    #API tempat
    data = requests.get('http://localhost:4000/id/city/32').json() #hanya jawa barat
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
    elif asal == 'Kab. Cirebon':
        asal = 'CIREBON'
    elif asal == 'Kota Bogor':
        asal = 'BOGOR'
    elif asal == 'Kab. Bogor':
        asal = 'BOGOR'
    elif asal == 'Kab. Cianjur':
        asal = 'CIANJUR'
    elif asal == 'Kab. Garut':
        asal = 'GARUT'
    elif asal == 'Kab. Tasikmalaya':
        asal = 'TASIKMALAYA'
    elif asal == 'Kota Tasikmalaya':
        asal = 'TASIKMALAYA'
    elif asal == 'Kab. Ciamis':
        asal = 'CIAMIS'
    elif asal == 'Kab. Indramayu':
        asal = 'INDRAMAYU'
    elif asal == 'Kab. Subang':
        asal = 'SUBANG'
    elif asal == 'Kab. Purwakarta':
        asal = 'PURWAKARTA'
    elif asal == 'Kab. Karawang':
        asal = 'KARAWANG'
    elif asal == 'Kota Cirebon':
        asal = 'CIREBON'
    elif asal == 'Kota Bekasi':
        asal = 'BEKASI'
    elif asal == 'Kab. Bekasi':
        asal = 'BEKASI'
    elif asal == 'Kota Cimahi':
        asal = 'CMI'
    elif asal == 'Kota Banjar':
        asal = 'BANJAR'
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
    elif tujuan == 'Kota Cirebon':
        tujuan = 'CIREBON'
    elif tujuan == 'Kab. Cirebon':
        tujuan = 'CIREBON'
    elif tujuan == 'Kota Bogor':
        tujuan = 'BOGOR'
    elif tujuan == 'Kab. Bogor':
        tujuan = 'BOGOR'
    elif tujuan == 'Kab. Cianjur':
        tujuan = 'CIANJUR'
    elif tujuan == 'Kab. Garut':
        tujuan = 'GARUT'
    elif tujuan == 'Kab. Tasikmalaya':
        tujuan = 'TASIKMALAYA'
    elif tujuan == 'Kota Tasikmalaya':
        tujuan = 'TASIKMALAYA'
    elif tujuan == 'Kab. Ciamis':
        tujuan = 'CIAMIS'
    elif tujuan == 'Kab. Indramayu':
        tujuan = 'INDRAMAYU'
    elif tujuan == 'Kab. Subang':
        tujuan = 'SUBANG'
    elif tujuan == 'Kab. Purwakarta':
        tujuan = 'PURWAKARTA'
    elif tujuan == 'Kab. Karawang':
        tujuan = 'KARAWANG'
    elif tujuan == 'Kota Cirebon':
        tujuan = 'CIREBON'
    elif tujuan == 'Kota Bekasi':
        tujuan = 'BEKASI'
    elif tujuan == 'Kab. Bekasi':
        tujuan = 'BEKASI'
    elif tujuan == 'Kota Cimahi':
        tujuan = 'CMI'
    elif tujuan == 'Kota Banjar':
        tujuan = 'BANJAR'
    else:
        tujuan = 'XXX' #kereta tidak terdaftar

    tgl = request.args.get('Tanggal')
    bln = request.args.get('Bulan')
    thn = request.args.get('Tahun')
    data = requests.get('http://localhost:3000/kereta?dept=' + asal + '&dest=' + tujuan + '&date=' + thn + '-' + bln + '-' + tgl).json()
    return render_template("hasil.html", submit = data)

if __name__ == "__main__":
    app.run(debug=True)
