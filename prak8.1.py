a = {'NIM':'L200180162','Nama':'Raihan Mazarul Hidayat','Alamat':'Kudus','Panggilan':'Raihan','PT':'UMS','Fak':'FKI','Prodi':'Informatika','K':'Keluar'}

print ("Pilihan yang tersedia:")
print ("N menampilkan Nama")
print ("n menampilkan NIM")
print ("l menampilkan Alamat")
print ("p menampikan Panggilan")
print ("t menampilkan PT")
print ("f menampilkan Fakultas")
print ("i menampilkan Prodi")
print ("K menampilkan Keluar")

def Nama():
    "menampilkan data diri masing-masing 1 setiap data"
    print ('Nama:' + a['Nama'])

def NIM():
    "menampilkan data diri masing-masing 1 setiap data"
    print ('NIM:' + a['NIM'])

def Alamat():
    "menampilkan data diri masing-masing 1 setiap data"
    print ('Alamat:' + a['Alamat'])

def Panggilan():
    "menampilkan data diri masing-masing 1 setiap data"
    print ('Panggilan:' + a['Panggilan'])

def PT():
    "menampilkan data diri masing-masing 1 setiap data"
    print ('PT:' + a['PT'])
 
def Fak():
    "menampilkan data diri masing-masing 1 setiap data"
    print ('Fak:' + a['Fak'])

def Prodi():
    "menampilkan data diri masing-masing 1 setiap data"
    print ('Prodi:' + a['Prodi'])

def K():
    "menampilakn data diri masing-masing 1 setiap data"
    print ('K:' + a['K'])

repeat = True

repeat = True

while repeat :
    x = input("Pilihan saudara :")
    if x == "N" :
        Nama()
    elif x == "n" :
        NIM()
    elif x == "l" :
        Alamat()
    elif x == "p" :
        Panggilan()
    elif x == "t" :
        PT()
    elif x == "f" :
        FAK()
    elif x == "i" :
        Prodi()
    elif x == "k" :
        print ("Terima Kasih.")
        repeat = False
        
                      
        
