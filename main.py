from flask import Flask, render_template
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

@app.route("/hasil")
def hasil():
    #API kereta api
    data = requests.get('http://localhost:3000/....').json() #itu harusnya endpoint yang lu harapkan
    return render_template("hasil.html", submit = data)

if __name__ == "__main__":
    app.run(debug=True)