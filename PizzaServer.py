from tkinter import *
from socket import *
from datetime import *
from threading import *
import random
import time

def serverNit():
    s = socket()
    s.bind((gethostname(),54321))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        narudzbina = conn.recv(1024).decode()
        print(narudzbina)
        vreme = random.randrange(30, 50)
        vremeStr = str(vreme)
        conn.send(vremeStr.encode())
        Thread(target=vremeNit,args=(conn,vreme,narudzbina)).start()
        conn.close()


def vremeNit(conn,vreme,narudzbina):
    lblNarudzbina = Label(Labelframe1, text=narudzbina)
    lblNarudzbina.pack(anchor=W)
    lblIsporuka = Label(Labelframe1, text=vreme)
    lblIsporuka.pack(anchor=W)
    lblNeisporucene = Label(Labelframe2, text="")
    lblNeisporucene.pack(anchor=W)

    while vreme > 0:
        vreme -= 1
        lblIsporuka.config(text=vreme)
        lblNarudzbina.config(text=narudzbina)
        print(vreme)
        time.sleep(1)

        if vreme < 1:
            lblNeisporucene.config(text=narudzbina)
            lblNarudzbina.destroy()
            lblIsporuka.destroy()


root = Tk()
root.geometry("1100x400")
root.title("Server")
Labelframe1 = LabelFrame(root,text="Neisporucene pice",bd=5)
Labelframe1.pack(fill="both",expand="yes",side=LEFT)

Labelframe2 = LabelFrame(root,text="Isporucene pice",bd=5)
Labelframe2.pack(fill="both",expand="yes",side=RIGHT)

Thread(target=serverNit).start()

root.mainloop()







