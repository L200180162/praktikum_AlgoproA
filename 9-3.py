import shelve
a = open("L200180162.txt", "r")
NIM = a.readline()
Tanggal_lahir = a.readline()
Nama = a.readline()
Kota = a.readline()
a.close()

a = shelve.open("Raihan")
a["b"] = [NIM, Tanggal_lahir, Nama, Kota]
a.close
