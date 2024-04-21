#region Urheberrechte
'''
///*-===========================================================================================================-*
/// Dateiname             : MeineDesktopAnwendung1.py
/// Version               : 1.0.0.0
/// Beginn                : 2024-02-12 (1402/11/23)
/// Letzte Aktualisierung : 2024-02-13 (1402/11/24)
/// Autor                 : Ingenieur Behdad Pourtavakoli
/// Warenzeichen          : Behdad Software Developers Group™
/// -------------------------------------------------------------------------------------------------------------
/// Copyright© 1380-1403,2001-2024 von B.S.D Group™
/// Alle Rechte vorbehalten.
/// -------------------------------------------------------------------------------------------------------------
///
/// Beschreibung: Überprüfen und lernen Sie die Python-Programmierung anhand von PDF-Artikeln und
///               relevanten Websites.
///
///               Desktop-Anwendung (Window-Anwendung)
///               Wahl zwischen TKinter und PyQt, PyQt ist leistungsfähiger als TKinter.
///
///-============================================================================================================-*
'''
#endregion

#region Wichtige Module und Header-Dateien
'''
///*********************************************************************************************************
///* Wichtige Module und Header-Dateien
///*********************************************************************************************************
'''
import time, platform
from tkinter import *
#import tkinter as tk
#endregion

#region Konstanten, Variablen und Deklarationen
'''
///*********************************************************************************************************
///* Konstanten, Variablen und Deklarationen
///*********************************************************************************************************
'''
tkMainForm = Tk()
#endregion

#region Klasse MeineDesktopAnwendung1
'''
///*********************************************************************************************************
///* Klasse MeineDesktopAnwendung1
///* Zu den Klasseneigenschaften gehören Felder und Funktionen:
///* strTitle: Formulartitel, Standardwert: "Python® Meine Desktop-Anwendung v1.0.0.0"
///* # Bauarbeiten im Gange - 1402/11/23
///*********************************************************************************************************
'''
class Basisdialog(object):
    def __init__(self, parent):
        self.data = None

        self.root = Toplevel(parent)
        self.entry = Entry(self.root)
        self.entry.pack()
        self.ok_btn = Button(self.root, text="OK", command=self.cmdOK)
        self.ok_btn.pack()

        self.root.wait_visibility()
        self.root.grab_set()
        self.root.transient(parent)

        self.parent = parent

    def cmdOK(self):
        self.data = self.entry.get()
        self.root.grab_release()
        self.root.destroy()

class MeineDesktopAnwendung1():
    _strTitle = "Python® Meine Desktop-Anwendung v1.0.0.0"
    _strSize1 = "320x200"
    _strSize2 = "640x480"
    _strSize3 = "800x600"
    _strSize4 = "1024x768"
    _strSize5 = "700x440"

    # Bauarbeiten im Gange - 1402/11/23
    def __init__(self, window, strTitle = _strTitle, strSize = _strSize3, bolCenter = True):
        strTemp = strSize.rsplit("x")
        intWidth = int(strTemp[0])
        intHeight = int(strTemp[1])
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        inyPosX = (screen_width / 2) - (intWidth / 2)
        intPosY = (screen_height / 2) - (intHeight / 2)
        if (bolCenter):
            window.geometry("%dx%d+%d+%d" % (intWidth, intHeight, inyPosX, intPosY))
        else:
            window.geometry(strSize)

        window.minsize(320, 200)
        window.resizable(False, False)
        window.iconphoto(False, PhotoImage(file="Images/Python3.png"))
        
        window.title(strTitle)

        strVersionVersionsnummer = str(platform.python_version())
        strNachricht = "Behdad Software Developers Group™ praesentiert\n\n"
        strNachricht += "Willkommen bei B.S.D Group™ Produktion\n\n"
        strNachricht += "Urheberrecht© 1380-1403,2001-2024 von B.S.D Group™\n"
        strNachricht += "Alle Rechte vorbehalten.\n\n"
        strNachricht += "Entwurf und Entwicklung durch Ingenieur Behdad Pourtavakoli\n\n"
        strNachricht += "MeineDesktopAnwendung1.py (Python v" + strVersionVersionsnummer + ") - B.S.D Group™"

        lblTemp = Label(tkMainForm, text = strNachricht)
        lblTemp.pack()
        intH = lblTemp.winfo_vrooty()
        intY = lblTemp.winfo_rooty()
        print(intH, "\t", intY)
        Button(window, text="Popup", command=self.cmdPopup).place(y=intY + intH + 10)
        Button(window, text="Exit", command=self.cmdExit).place(y=20)
        self.window = window
        window.bind("<Key>", self.handle_key)

    def handle_key(self, event):
        k = event.keysym
        print(f"got k: {k}")

    def cmdPopup(self):
        d = Basisdialog(self.window)
        print("opened login window, about to wait")
        self.window.wait_window(d.root)
        print("end wait_window, back in MainWindow code")
        print(f"got data: {d.data}")

    def cmdExit(self):
        self.window.destroy()
#endregion

#region Handschriftliche Funktionen und Prozeduren
'''
///*********************************************************************************************************
///* Handschriftliche Funktionen und Prozeduren
///*********************************************************************************************************
'''

#endregion

#region Standardfunktionen und -verfahren
'''
///*********************************************************************************************************
///* Standardfunktionen und -verfahren
///*********************************************************************************************************
'''

'''
/// WinMain() enthält Hauptanweisungen und aufrufende Funktionen
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/23
/// 
'''
def WinMain():
    intStartTime = time.time()

    # /// Etwas tun - 1402/11/23 (2024/02/12)
    # /// im Aufbau, geht weiter - 1402/11/24 (2024/02/13)
    frmMDA = MeineDesktopAnwendung1(tkMainForm)
    #tkMainForm.master.minsize(800, 600)        
    tkMainForm.mainloop()
    
    intEndTime = time.time()
    intElapsedTime = intEndTime - intStartTime
    print("Elapsed Time: %s ms" % round(intElapsedTime, 3))
#endregion
 
#region Hauptprogramm
'''
///*********************************************************************************************************
///* Hauptprogramm
///*********************************************************************************************************
'''
'''
/// Hauptprogramm, enthält Hauptanweisungen und Aufruffunktionen
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/23
/// 
'''
if (__name__ == "__main__"):
    WinMain()
#endregion
