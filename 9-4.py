import shelve
a = open("L200180162.txt", "r")
NIM = a.readline()
Tanggal_lahir = a.readline()
Nama = a.readline()
Kota = a.readline()
a.close()

a = shelve.open("Raihan")
a["b"] = [NIM, Tanggal_lahir, Nama, Kota]
print(a["b"][0])
print(a["b"][1])
print(a["b"][2])
print(a["b"][3])
a.close
