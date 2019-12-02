APLIKASI LAYANAN KERETA API JAWA BARAT

Yudhistira Qasthari Putra - 18217003 
Muhammad Isfan Rahadi - 18217019

---------------------------------------------------------------------------

URL API Kereta Api: http://api-kereta-api.herokuapp.com/

URL API Tempat: https://wiki-region-api.herokuapp.com/

URL Aplikasi: http://layanankereta.herokuapp.com/

--------------------------------------

Endpoint API Kereta Api : 
'/kereta' 
Menggunakan query masukan yaitu : 
  dept = kota asal (Uppercase)
  dest = kota tujuan (Uppercase)
  date = tanggal (yyyy-mm-dd) 

contoh : /kereta?dept=BANDUNG&dest=CIREBON&date=2019-12-06
 
Endpoint API Tempat: 
'/id/city/<idprovinsi>' 
id provinsi merupakan integer

contoh : '/id/city/32'

----------------------------------------------------------

Note: 

Deploy berhasil dilakukan namun data web yang dicrawl (tiket.com) diprotect oleh Cloudflare.
Sehingga apabila dilakukan crawl pada web app yang sudah dideploy terjadi internal server error.
Apabila dilakukan crawl secara offline melalui localhost maka dapat dilakukan.

---------------------------------------------------

Disediakan file offline yang dapat dijalankan melalui localhost pada folder "Offline." (Worked 100%)

End point API Kereta Api: http://localhost:3000/

End point API Tempat: http://localhost:4000/

End point Aplikasi: http://localhost:5000/

How to run:

1. Run app.py dari aplikasiTST/Offline/API Kereta Api/

2. Run main.py dari aplikasiTST/Offline/API Tempat/

3. Run main.py dari aplikasiTST/Offline/

4. Masuk ke end point Aplikasi

------------------------------------------------------

Instruction

Apabila tidak muncul jadwal maka tidak ada kereta yang tersedia pada rute tersebut.
Diharapkan memilih tanggal dalam kurun waktu 1-2 minggu terdekat dari hari ini agar terdapat jadwal kereta yang sudah ada.
