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
    return str(gethostbyname(getfqdn())) #Python yorumlay�c�s�n�n y�r�t�ld��� makinenin hostname'ini string olarak d�nd�r�r,tam etkili alan ad� i�in getfqdn() kullan�lm��t�r.
    
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
            SohbetLog.insert(END, u"Arkada�: " + Metin)
            SohbetLog.tag_add(u"Arkada�", SatirNo, SatirNo+0.8)
            SohbetLog.tag_config(u"Arkada�", foreground="#04B404", font=("TimesNewRomantur", 12, "bold"))
            SohbetLog.config(state=DISABLED)
            SohbetLog.yview(END)
            
