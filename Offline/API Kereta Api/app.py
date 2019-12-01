from flask import request, Flask, redirect, jsonify, Response
import requests
import json
from bs4 import BeautifulSoup
import codecs

app = Flask(__name__)
tiketcom = "https://www.tiket.com/kereta-api/cari?d="


@app.route('/')
def test(): 
	return 'test' 

@app.route('/test')
def cek() :
	_url = requests.get('https://www.tiket.com/kereta-api/cari?d=JAKARTA&dt=CITY&a=BANDUNG&at=CITY&date=2019-12-02&adult=1&infant=0')
		
	_textdata = BeautifulSoup(_url.text, 'html.parser')
	
	
	return jsonify(_textdata)
	

@app.route('/kereta')
def getKereta():
		_asal = request.args.get('dept') 
		_tujuan = request.args.get('dest')
		_tanggal = request.args.get('date')
			
		if _asal == '' or _tujuan == '' or _tanggal == '': 
			return(Response('Parameter tidak tepat', 400))
			
		_url = requests.get(tiketcom + _asal + '&dt=CITY&a=' + _tujuan + '&at=CITY&date=' + _tanggal + '&adult=1&infant=0')
		
		_textdata = BeautifulSoup(_url.text, 'html.parser')
		
		_element = _textdata.find('tbody', attrs = {'id' : 'tbody_depart'})
		_traindata = []
		_temp = {}

		for _tr in _element.find_all('tr', attrs = {'class' : 'item-list'}):

			if _tr.find('td', attrs = {'class' : 'td1'}) :

				_td1 = _tr.find('td', attrs = {'class' : 'td1'})
				if _td1.find('div', attrs = {'class' : 'item-title item-title-16'}) :
					_key = "nama kereta" 
					_value = _td1.find('div', attrs = {'class' : 'item-title item-title-16'}).string
				_temp[_key] = _value
				
				if _td1.find('div', attrs = {'class' : 'item-desc'}) :
					_key = "Kelas" 
					_value = _td1.find('span').string
				_temp[_key] = _value
				

			if _tr.find('td', attrs = {'class' : 'td2'}) :
				
				_td2 = _tr.find('td', attrs = {'class' : 'td2'})
				if _td2.find('div', attrs = {'class' : 'item-title'}) :
					_key = "Waktu berangkat" 
					_value = _td2.find('div', attrs = {'class' : 'item-title'}).string
				_temp[_key] = _value
				
				if _td2.find('div', attrs = {'class' : 'item-desc'}) :
					_key = "Stasiun asal" 
					_value = _td2.find('div', attrs = {'class' : 'item-desc'}).string
				_temp[_key] = _value
			

			if _tr.find('td', attrs = {'class' : 'td3'}) :
				
				_td3 = _tr.find('td', attrs = {'class' : 'td3'})
				if _td3.find('div', attrs = {'class' : 'item-title'}) :
					_key = "Waktu tiba" 
					_value = _td3.find('div', attrs = {'class' : 'item-title'}).string
				_temp[_key] = _value
				
				if _td3.find('div', attrs = {'class' : 'item-desc'}) :
					_key = "Stasiun tujuan" 
					_value = _td3.find('div', attrs = {'class' : 'item-desc'}).string
				_temp[_key] = _value
				
			_traindata.append(_temp.copy())
			
		return jsonify(_traindata)
		
if __name__ == '__main__': 
	app.run(threaded = True, port= 3000)
		
		
