# -*- coding: cp1254 -*-
# -*- coding: utf-8 -*-

from Tkinter import *
from socket import *
import win32gui
   
def SohbetPencere(baslik):
    ID = win32gui.FindWindow(None, baslik)
    win32gui.FlashWindow(ID,True)

def SohbetPencere2(baslik):
    ID2 = win32gui.FindWindow(None, baslik)
    win32gui.FlashWindow(ID2,True)  
    

def IcIP():
    return str(gethostbyname(getfqdn())) #Python yorumlayıcısının yürütüldüğü makinenin hostname'ini string olarak döndürür,tam etkili alan adı için getfqdn() kullanılmıştır.
    
def IletiFiltrele(Metin):
    """
    Filter out all useless white lines at the end of a string,
    returns a new, beautifully filtered string.
    """
    
    FiltreSonu = u''
    for i in range(len(Metin)-1,-1,-1):
        if Metin[i]!=u'\n':
            FiltreSonu = Metin[0:i+1]
            break
    for i in range(0,len(FiltreSonu), 1):
            if FiltreSonu[i] != u"\n":
                    return FiltreSonu[i:]+u'\n'
    return ''
	
def BaglantiBilgi(SohbetLog, Metin):
    if Metin != '':
        SohbetLog.config(state=NORMAL)
        if SohbetLog.index('end') != None:
            SohbetLog.insert(END, Metin+'\n')
            SohbetLog.config(state=DISABLED)
            SohbetLog.yview(END)

def GirisSen(SohbetLog, Metin):
    if Metin != '':
        SohbetLog.config(state=NORMAL)
        if SohbetLog.index('end') != None:
            SatirNo = float(SohbetLog.index('end'))-1.0
            SohbetLog.insert(END, "Sen: " + Metin)
            SohbetLog.tag_add("Sen", SatirNo, SatirNo+0.4)
            SohbetLog.tag_config("Sen", foreground="#FF8000", font=("TimesNewRomantur", 12, "bold"))
            SohbetLog.config(state=DISABLED)
            SohbetLog.yview(END)


def GirisArkadas(SohbetLog, Metin):
    if Metin != '':
        SohbetLog.config(state=NORMAL)
        if SohbetLog.index('end') != None:
            try:
                SatirNo = float(SohbetLog.index('end'))-1.0
            except:
                pass
            SohbetLog.insert(END, u"Arkadaş: " + Metin)
            SohbetLog.tag_add(u"Arkadaş", SatirNo, SatirNo+0.8)
            SohbetLog.tag_config(u"Arkadaş", foreground="#04B404", font=("TimesNewRomantur", 12, "bold"))
            SohbetLog.config(state=DISABLED)
            SohbetLog.yview(END)
            
