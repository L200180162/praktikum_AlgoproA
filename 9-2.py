a = open("L200180162.txt", "w")
a.write("L200180162" "\n")
a.write("05/20/2000" "\n")
a.write("Raihan Mazarul Hidayat" "\n")
a.write("Kudus")

a = open("L200180162.txt", "r")
NIM = a.readline()
Tanggal_lahir = a.readline()
Nama = a.readline()
Kota = a.readline()
print(Nama)
print(Kota, Tanggal_lahir)
print(NIM)
a.close()
