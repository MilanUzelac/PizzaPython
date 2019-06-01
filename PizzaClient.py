from tkinter import *
from threading import *
from datetime import *
from socket import *
from tkinter import messagebox
import re

s = socket()
s.connect((gethostname(),54321))

root = Tk()
root.title("Client")
root.geometry("300x600")
lblNarucite = Label(root,text="Narucite picu",font=("Verdana"))
lblNarucite.pack()

lblVelicina = Label(root,text="Velicina:")
lblVelicina.pack(anchor=W)

varVelicina=IntVar(value=1)
rb25 = Radiobutton(root,text="25cm",variable=varVelicina,value=1)
rb25.pack(anchor=W)

rb32 = Radiobutton(root,text="32cm",variable=varVelicina,value=2)
rb32.pack(anchor=W)

rb50 = Radiobutton(root,text="50cm",variable=varVelicina,value=3)
rb50.pack(anchor=W)

lblVrsta = Label(root,text="Vrsta:")
lblVrsta.pack(anchor=W)

varVrsta=IntVar(value=1)
margarita = Radiobutton(root,text="Margarita",variable=varVrsta,value=1)
margarita.pack(anchor=W)

quattro = Radiobutton(root,text="Quattro Stagione",variable=varVrsta,value=2)
quattro.pack(anchor=W)

funghi = Radiobutton(root,text="Funghi",variable=varVrsta,value=3)
funghi.pack(anchor=W)

vegetariana = Radiobutton(root,text="Vegeteriana",variable=varVrsta,value=4)
vegetariana.pack(anchor=W)

lblDodaci = Label(root,text="Dodaci")
lblDodaci.pack(anchor=W)

varKecap=IntVar()
cbKecap = Checkbutton(root,text="Kecap",variable=varKecap)
cbKecap.pack(anchor=W)

varMajonez=IntVar()
cbMajonez = Checkbutton(root,text="Majonez",variable = varMajonez)
cbMajonez.pack(anchor=W)

varOrigano=IntVar()
cbOrigano = Checkbutton(root,text="Origano",variable = varOrigano)
cbOrigano.pack(anchor=W)

lblNacinPlacanja = Label(text="Nacin placanja: ")
lblNacinPlacanja.pack(anchor=W)


varNacin = IntVar(value=1)
rbGotovinom = Radiobutton(root,text="Gotovinom",variable=varNacin,value=1)
rbGotovinom.pack(anchor=W)

rbKarticom = Radiobutton(root,text="Karticom",variable=varNacin,value=2)
rbKarticom.pack(anchor=W)

lblAdresa = Label(root,text="Adresa:")
lblAdresa.pack(anchor=W)

varAdresa=StringVar()
txtAdresa = Entry(root,textvariable=varAdresa,width=300)
txtAdresa.pack(anchor=W)

lblTelefon = Label(root,text="Telefon:")
lblTelefon.pack(anchor=W)

varTelefon = StringVar()
txtTelefon = Entry(root,textvariable = varTelefon,width=300)
txtTelefon.pack()

lblNapomena = Label(root,text="Napomena:")
lblNapomena.pack(anchor=W)

varNapomena = StringVar()
txtNapomena = Entry(root,textvariable = varNapomena,width=300)
txtNapomena.pack(anchor=W)


def naruci():
    odgovor = ""
    flag = False
    velicina = ""
    vrsta = ""
    b=""
    nacinPlacanja=""
    if varVelicina.get()==1:
        velicina = "25cm"
    elif varVelicina.get()==2:
        velicina = "32cm"
    elif varVelicina.get()==3:
        velicina = "50cm"
    if varVrsta.get()==1:
        vrsta="Margarita"
    elif varVrsta.get()==2:
        vrsta="Quattro Stagione"
    elif varVrsta.get()==3:
        vrsta="Funghi"
    elif varVrsta.get()==4:
        vrsta = "Vegeteriana"
    if varKecap.get():
        b = "sa kecapom,"
    c=""
    if varMajonez.get():
        c = "sa majonezom,"
    d=""
    if varOrigano.get():
        d = "sa origanom,"

    izbor =c+b+d
    if varNacin.get()==1:
        nacinPlacanja = "placanje gotovinom"
    if varNacin.get()==2:
        nacinPlacanja="placanje karticom"


    print(varTelefon.get())
    regex = "\w{3}-\w{4}-\w{3}"

    if not re.search(regex,varTelefon.get()):
        txtTelefon.configure(bg="red")
        txtTelefon.update()
        messagebox._show("Greska pri unosu!","Broj telefona mora biti u formatu 000-0000-000")
        flag = False
    else:
        flag=True

    if varAdresa.get()=="" or varTelefon.get()=="":
        messagebox._show("Greska!","Polja za unos adrese i broja telefona moraju biti popunjena!")
        flag=False


    if flag==True:
        porudzbina = "Pica: " + velicina + ", " + vrsta + ", " + izbor + nacinPlacanja + ", " + varAdresa.get() + ", " + varTelefon.get() + ", " + varNapomena.get()
        messagebox.showinfo("Narudžba", "Naručili ste: " + velicina +", " + vrsta + ", " +izbor + nacinPlacanja + ", " + varAdresa.get() + ", " + varTelefon.get() + ", " + varNapomena.get())
        print(porudzbina)
        s.send(porudzbina.encode())
        odgovor = s.recv(1024).decode()
        lblVreme.config(text=odgovor + "minuta")


btnNaruci = Button(root,text="Naruci",width=300,command = naruci)
btnNaruci.pack()

lblVremeDoIsporuke = Label(root,text="Vreme do isporuke:")
lblVremeDoIsporuke.pack(anchor = W)

lblVreme = Label(root,text="")
lblVreme.pack(anchor =W)

root.mainloop()