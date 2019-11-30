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
    asal = "GMR"
    tujuan = "GMR" #ini harusnya diisi sama kode stasiun yang ditranslate dari daerah (dinamis)
    tanggal = "05-12-2019" #ini harusnya diisi sama penggabungan tanggal hari tahun di laman home (dinamis)
    # asal = request.form['AsalKota']

    data = requests.get('http://localhost:3000/kereta?dept=' + asal + '&dest=' + tujuan + '&date=' + tanggal).json()
    return render_template("hasil.html", submit = data)

if __name__ == "__main__":
    app.run(debug=True)
