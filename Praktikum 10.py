###KEGIATAN 1
###nama berkas: p_tcpser.py
###TCP server untuk client p_tcpcli.py
##import socket
##s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##s.bind(("",50004))
##s.listen(5)
##print "server penjawab otomatis sudah siap"
##data =''
##kamus = {'Nama': 'Raihan Mazarul H', 'NIM': 'L200180162', 'angkatan': '26', 'keluar': 'siap!!'}
##while data.lower() != 'q':
##    komm, addr = s.accept()
##    while data.lower() != 'q':
##        data = komm.recv(1024)
##        if data.lower() == 'q':
##            s.close()
##            break
##        print 'perintah: ',data
##        if kamus.has_key(data):
##            komm.send(kamus[data])
##        else:
##            komm.send('Maaf, perintah tidak dimengerti')

###KEGIATAN 1
###nama berkas: p_tcpcli.py
###client TCP untuk server p_tcpser.py
##import socket
##
##hostname = 'localhost'
##pesan = ''
##s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##s.connect((hostname, 50004))
##print "mesin penjawab otomatis sudah siap"
##while pesan.lower() != 'q':
##    pesan = raw_input('perintah: ')
##    s.send(pesan)
##    if pesan.lower() != 'q':
##        response = s.recv(1024)
##        print 'jawab: ', response
##s.close()

###KEGIATAN 2
####nama berkas: p_tcpser.py
####TCP server untuk client p_tcpcli.py
##import socket
##import platform
##
##s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##s.bind(("",50004))
##s.listen(5)
##print "server penjawab otomatis sudah siap"
##data =''
##kamus = {'machine': platform.machine(), 'release': platform.release(), 'system': platform.system(), 'version': platform.version(), 'node':platform.node()}
##while data.lower() != 'quit':
##    komm, addr = s.accept()
##    while data.lower() != 'quit':
##        data = komm.recv(1024)
##        if data.lower() == 'quit':
##            s.close()
##            break
##        print 'command: ',data
##        if kamus.has_key(data):
##            komm.send(kamus[data])
##        else:
##            komm.send('unknown command')

###KEGIATAN 2
####nama berkas: p_tcpcli.py
####client TCP untuk server p_tcpser.py
##import socket
##import platform
##
##hostname = 'localhost'
##pesan = ''
##s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##s.connect((hostname, 50004))
##print "Program komunikasi tentang diri anda"
##while pesan.lower() != 'quit':
##    pesan = raw_input('perintah: ')
##    s.send(pesan)
##    if pesan.lower() != 'quit':
##        response = s.recv(1024)
##        print 'jawab: ', response
##    else:
##        print "siap!!"
##s.close()

###KEGIATAN 3
####nama berkas: p_tcpser.py
####TCP server untuk client p_tcpcli.py
##import socket
##import platform
##s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
##s.bind(("", 50002))
##s.listen(5)
##print "server penjawab otomatis sudah siap"
##data= ''
##angkaHitung = 0
### komm, addr = s.accept()
### data = komm.recv(1024)
##
### kamus = {'parameter1=' : platform.machine(),
###          'hitung' : 
###          'quit' : ' Siapp !!!' }
##
##
##def hitung(a):
##    return a*a
##
##
##while data.lower() != 'quit' :
##    komm, addr = s.accept()
##    data = komm.recv(1024)
##    print 'Command: ', data
##    if data[0:11].lower() == 'parameter1=':
##            angkaHitung = int(data[11:])
##            if angkaHitung != 0:
##                komm.send("Parameter di catat")
##    else:
##        komm.send('unknown command')
##    data = komm.recv(1024)
##    if data.lower() == 'hitung':
##        hasil = hitung(angkaHitung)
##        hasil = str(hasil)
##        komm.send("Hasil persegi dari sisi "+str(angkaHitung)+" adalah "+hasil)
##    else:
##        komm.send('unknown command')
##    if data.lower() == 'keluar':
##        s.close()
##        break

###KEGIATAN 3
####nama berkas: p_tcpcli.py
####client TCP untuk server p_tcpser.py
##import socket
##
##hostname = 'localhost'
##client = ''
##s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##s.connect((hostname, 50002))
##print "Menghitung Luas Bangun Persegi "
##while client.lower() != 'keluar' :
##    client = raw_input( 'Pesan: ')
##    s.send(client)
##    if client.lower() != 'keluar' :
##        response = s.recv(1024)
##        print "Respon: " , response
##    else :
##        print 'Respon: -'
##s.close()
