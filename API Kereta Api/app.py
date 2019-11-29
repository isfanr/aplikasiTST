from flask import request, Flask, redirect, jsonify, Response
import requests
import json
from bs4 import BeautifulSoup
import codecs

app = Flask(__name__)
pegi2 = "www.pegipegi.com/kereta-api/search/direct/"


@app.route('/')
def test(): 
	return 'test' 

@app.route('/test')
def cek() :
	_url = requests.get('https://www.pegipegi.com/kereta-api/search/direct/GMR/BD/28-11-2019/1/0/EBK')
		
	_textdata = BeautifulSoup(_url.text, 'html.parser')
	
	
	return jsonify(_textdata)
	
#@app.route('/kereta/<dept>/<dest>/<date>')
@app.route('/kereta')
#def getKereta(dept, dest, date):
def getKereta():
	try:
		"""_asal = dept 
		_tujuan = dest
		_tanggal = date"""
		_asal = request.args.get('dept') 
		_tujuan = request.args.get('dest')
		_tanggal = request.args.get('date')
			
		if _asal == None or _tujuan == None or _tanggal == None: 
			return(Response('Parameter tidak tepat', 400))
			
		_url = requests.get('https://' + pegi2 + _asal + '/' + _tujuan + '/' + _tanggal + '/1/0/EBK')
		
		_textdata = BeautifulSoup(_url.text, 'html.parser')
		
		"""_error = _textdata.find('tr', attrs = {'class' : 'odd'})
		
		if _error:
			return(Response('Kereta tidak ditemukan', 404))"""
			
		
		_element = _textdata.find('tbody', attrs = {'class' : 'searchResultBody detailOrder active'})
		_traindata = []
		_temp = {}
		
		for _tr in _element.find_all('tr'):
			if _tr.find('td', attrs = {'class' : 'column namaKelasKereta'}) :
				if _tr.find('div', attrs = {'class' : 'namaKereta'}) :
					_key = "nama kereta" + str(_num)
					_value = _tr.find('div', attrs = {'class' : 'namaKereta'}).string
				_temp[_key] = _value
				
				if _tr.find('div', attrs = {'class' : 'kelasKereta'}) :
					_key = "Kelas" + str(_num)
					_value = _tr.find('div', attrs = {'class' : 'kelasKereta'}).string
				_temp[_key] = _value
				
			if _tr.find('td', attrs = {'class' : 'column keretaBerangkat'}) :
				if _tr.find('div', attrs = {'class' : 'time'}) :
					_key = "Waktu berankat" + str(_num)
					_value = _tr.find('div', attrs = {'class' : 'time'}).string
				_temp[_key] = _value
				
				if _tr.find('div', attrs = {'class' : 'destiny origresult'}) :
					_key = "Stasiun asal" + str(_num)
					_value = _tr.find('div', attrs = {'class' : 'destiny origresult'}).string
				_temp[_key] = _value
			
			if _tr.find('td', attrs = {'class' : 'column keretaTiba'}) :
				if _tr.find('div', attrs = {'class' : 'time'}) :
					_key = "Waktu tiba" + str(_num)
					_value = _tr.find('div', attrs = {'class' : 'time'}).string
				_temp[_key] = _value
				
				if _tr.find('div', attrs = {'class' : 'destiny desresult'}) :
					_key = "Stasiun Tujuan" + str(_num)
					_value = _tr.find('div', attrs = {'class' : 'destiny desresult'}).string
				_temp[_key] = _value
				
			_traindata.append(_temp.copy())
			for key in _temp: 
				del _temp[key]
			_num += 1
		return jsonify(_traindata)
		
	except Exception as e:
		raise e
		
if __name__ == '__main__': 
	app.run()
			
		
		
		