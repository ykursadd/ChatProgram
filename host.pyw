# -*- coding: cp1254 -*-
# -*- coding: utf-8 -*-
import thread
from MainSohbet import *




#---------BAĞLANTI DEĞİŞKENLERİNİ BAŞLATMA-----------#

#Initiate socket and bind port to host PC
PencereBaslik = '81 SUPPORTER- Host'
s = socket(AF_INET, SOCK_STREAM)
HOST = gethostname()
PORT = 8011
conn = ''
s.bind((HOST, PORT))




#------------------ MOUSE OLAYLARI -------------------#

def ClickAction():
    #Sohbet penceresi için mesaj yazımı
    Metin = IletiFiltrele(MetinKutu.get("0.0",END))
    GirisSen(SohbetLog, Metin)

    #Sohbet penceresinin altın gidin
    SohbetLog.yview(END)

    #Önceki mesajı temizleme
    MetinKutu.delete("0.0",END)
            
    #Benim mesajımı tüm kullanıcılara gönderimi
    conn.sendall(Metin)
    

	

	

#----------------- KLAVYE OLAYLARI -----------------#

def PressAction(event):
	MetinKutu.config(state=NORMAL)
	ClickAction()
def DisableEntry(event):
	MetinKutu.config(state=DISABLED)

    



#-----------------GRAFİK YÖNETİMİ---------------#


#Pencere Oluşturma
base = Tk()
base.title(PencereBaslik)
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)

#Chat penceresi oluşturma
SohbetLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)
SohbetLog.insert(END, u"Bağlantı Kuruluyor...\n")
SohbetLog.config(state=DISABLED)

#Sohbet penceresine kaydırma cubugu ekleme
scrollbar = Scrollbar(base, command=SohbetLog.yview, cursor="pirate")
SohbetLog['yscrollcommand'] = scrollbar.set

#mesaj gönderme butonu oluşturma
SendButton = Button(base, font=30, text=u"Gönder", width="12", height=5,
                    bd=0, bg="#00CCFF", activebackground="#9999FF",
                    command=ClickAction)

#mesajı girmek için kutu oluşturma
MetinKutu = Text(base, bd=0, bg="white",width="29", height="5", font="TimesNewRomantur")
MetinKutu.bind("<Return>", DisableEntry)
MetinKutu.bind("<KeyRelease-Return>", PressAction)

#Ekrandaki tüm bileşenleri yerleştirme
scrollbar.place(x=376,y=6, height=386)
SohbetLog.place(x=6,y=6, height=386, width=370)
MetinKutu.place(x=6, y=401, height=90, width=265)
SendButton.place(x=278, y=401, height=90)




#----------------BAĞLANTI YÖNETİMİ--------------#

def GetConnected():
    s.listen(1)
    global conn
    conn, addr = s.accept()
    BaglantiBilgi(SohbetLog, u'Bağlanıldı: ' + str(addr) + '\n---------------------------------------------------------------')
    
    while 1:
        try:
            data = conn.recv(1024)
            GirisArkadas(SohbetLog, data)
            if base.focus_get() == None:
                SohbetPencere(PencereBaslik)
                
        except:
            BaglantiBilgi(SohbetLog, u'\n [ Arkadaşın Çevrimdışı ]\n [ Çevrimiçi Olması Bekleniyor...] \n  ')
            GetConnected()

    conn.close()
    
thread.start_new_thread(GetConnected,())



base.mainloop()


