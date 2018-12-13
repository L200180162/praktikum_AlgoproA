from Tkinter import*

my_app = Tk(className='kalkulator sederhana')

L1 = Label(my_app, text='Angka 1')
L1.grid(row=0, column=0)
E1 = Entry(my_app)
E1.grid(row=0, column=1, columnspan=3)
L2 = Label(my_app, text='Angka 2')
L2.grid(row=1, column=0)
E2 = Entry(my_app)
E2.grid(row=1, column=1, columnspan=3)
L3 = Label(my_app, text='Hasil')
L3.grid(row=3, column=0, columnspan=2)
hasil = StringVar()
L4 = Label(my_app, textvariable=hasil)
L4.grid(row=3, column=2, columnspan=2)

def penjumlahan():
    hasil.set(int(E1.get()) + int(E2.get()))

def pengurangan():
    hasil.set(int(E1.get()) - int(E2.get()))

def perkalian():
    hasil.set(int(E1.get()) * int(E2.get()))

def pembagian():
    hasil.set(int(E1.get()) / int(E2.get()))

B1 = Button(my_app, text='+', command=penjumlahan)
B1.grid(row=2,column=0)
B2 = Button(my_app, text='-', command=pengurangan)
B2.grid(row=2,column=1)
B3 = Button(my_app, text='x', command=perkalian)
B3.grid(row=2,column=2)
B4 = Button(my_app, text=':', command=pembagian)
B4.grid(row=2,column=3)

my_app.mainloop()
