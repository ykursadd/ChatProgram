# -*- coding: cp1254 -*-
# -*- coding: utf-8 -*-
import thread
from MainSohbet import *




#---------BA�LANTI DE���KENLER�N� BA�LATMA-----------#

#Initiate socket and bind port to host PC
PencereBaslik = '81 SUPPORTER- Host'
s = socket(AF_INET, SOCK_STREAM)
HOST = gethostname()
PORT = 8011
conn = ''
s.bind((HOST, PORT))




#------------------ MOUSE OLAYLARI -------------------#

def ClickAction():
    #Sohbet penceresi i�in mesaj yaz�m�
    Metin = IletiFiltrele(MetinKutu.get("0.0",END))
    GirisSen(SohbetLog, Metin)

    #Sohbet penceresinin alt�n gidin
    SohbetLog.yview(END)

    #�nceki mesaj� temizleme
    MetinKutu.delete("0.0",END)
            
    #Benim mesaj�m� t�m kullan�c�lara g�nderimi
    conn.sendall(Metin)
    

	

	

#----------------- KLAVYE OLAYLARI -----------------#

def PressAction(event):
	MetinKutu.config(state=NORMAL)
	ClickAction()
def DisableEntry(event):
	MetinKutu.config(state=DISABLED)

    



#-----------------GRAF�K Y�NET�M�---------------#


#Pencere Olu�turma
base = Tk()
base.title(PencereBaslik)
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)

#Chat penceresi olu�turma
SohbetLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)
SohbetLog.insert(END, u"Ba�lant� Kuruluyor...\n")
SohbetLog.config(state=DISABLED)

#Sohbet penceresine kayd�rma cubugu ekleme
scrollbar = Scrollbar(base, command=SohbetLog.yview, cursor="pirate")
SohbetLog['yscrollcommand'] = scrollbar.set

#mesaj g�nderme butonu olu�turma
SendButton = Button(base, font=30, text=u"G�nder", width="12", height=5,
                    bd=0, bg="#00CCFF", activebackground="#9999FF",
                    command=ClickAction)

#mesaj� girmek i�in kutu olu�turma
MetinKutu = Text(base, bd=0, bg="white",width="29", height="5", font="TimesNewRomantur")
MetinKutu.bind("<Return>", DisableEntry)
MetinKutu.bind("<KeyRelease-Return>", PressAction)

#Ekrandaki t�m bile�enleri yerle�tirme
scrollbar.place(x=376,y=6, height=386)
SohbetLog.place(x=6,y=6, height=386, width=370)
MetinKutu.place(x=6, y=401, height=90, width=265)
SendButton.place(x=278, y=401, height=90)




#----------------BA�LANTI Y�NET�M�--------------#

def GetConnected():
    s.listen(1)
    global conn
    conn, addr = s.accept()
    BaglantiBilgi(SohbetLog, u'Ba�lan�ld�: ' + str(addr) + '\n---------------------------------------------------------------')
    
    while 1:
        try:
            data = conn.recv(1024)
            GirisArkadas(SohbetLog, data)
            if base.focus_get() == None:
                SohbetPencere(PencereBaslik)
                
        except:
            BaglantiBilgi(SohbetLog, u'\n [ Arkada��n �evrimd��� ]\n [ �evrimi�i Olmas� Bekleniyor...] \n  ')
            GetConnected()

    conn.close()
    
thread.start_new_thread(GetConnected,())



base.mainloop()


