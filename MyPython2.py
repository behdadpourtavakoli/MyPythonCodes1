'''
///*-=============================================================================================-*
/// Dateiname             : MyFirstPy2.py
/// Version               : 1.0.0.0
/// Beginn                : 2023-06-02 (1402/03/12)
/// Letzte Aktualisierung : 2023-11-06 (1402/08/15)
/// Autor                 : Ingenieur Behdad Pourtavakoli
/// Warenzeichen          : Behdad Software Developers Group™
/// ----------------------------------------------------------------------------------------------
/// Copyright© 1380-1402,2001-2023 von B.S.D Group™
/// Alle Rechte vorbehalten.
/// ----------------------------------------------------------------------------------------------
///
/// Beschreibung: Überprüfung und Erlernen der Python-Programmierung auf der w3schools-Website und
///               (https://www.mongard.ir/courses/python-beginner-course/) im PDF-Format
///
///-=============================================================================================-*///
'''

import os, time, sys, locale
from tkinter import *
from PIL import Image, ImageTk

# Python 3 code to demonstrate the SHA1
import hashlib

#region Konstanten, Variablen und Deklarationen
'''
///*********************************************************************************************************
///* Konstanten, Variablen und Deklarationen                                                               *
///*********************************************************************************************************
'''

#endregion

#region Handschriftliche Funktionen und Prozeduren
'''
/// *********************************************************************************************************
/// * Handschriftliche Funktionen und Prozeduren                                                            *
/// *********************************************************************************************************
'''

'''
/// about_EN() funktion zur Anzeige von Programminformationen, Versionsnummer und Urheberrecht als Englisch
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/07/18
/// 
'''
def about_EN():
     os.system('cls')
     print("Behdad Software Developers Group™ Presents\n")
     
     print("Welcome to the B.S.D Group™ Production\n")
     
     print("Copyright© 1380-1402,2001-2023 by B.S.D Group™")
     print("All rights reserved.\n")
     
     print("Design and develop by Engineer Behdad Pourtavakoli\n")
     
     print("®MyFirstPy2.py - B.S.D Group™")
     print("www.mongard.ir, coderslegacy.com, www.tutorialspoint.com are teachers...\n")

'''
/// about_EN() funktion zur Anzeige von Programminformationen, Versionsnummer und Urheberrecht als Deutsch
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/07/18
/// 
'''
def about_DE():
     os.system('cls')
     print("Behdad Software Developers Group™ praesentiert\n")
     
     print("Willkommen bei B.S.D Group™ Produktion\n")
     
     print("Urheberrecht© 1380-1402,2001-2023 von B.S.D Group™")
     print("Alle Rechte vorbehalten.\n")
     
     print("Entwurf und Entwicklung durch Ingenieur Behdad Pourtavakoli\n")
     
     print("®MyFirstPy2.py - B.S.D Group™")
     print("www.mongard.ir, coderslegacy.com, www.tutorialspoint.com sind Lehrer...\n")

def variables():
     x = "Hello World"
     print("X [" , x, "] Class type is: ", type(x))
     x = 20
     print("X [" , x, "] Class type is: ", type(x))
     x = 20.5
     print("X [" , x, "] Class type is: ", type(x))
     x = 1j
     print("X [" , x, "] Class type is: ", type(x))
     x = ["apple", "banana", "cherry"]
     print("X [" , x, "] Class type is: ", type(x))
     x = ("apple", "banana", "cherry")
     print("X [" , x, "] Class type is: ", type(x))
     x = range(6)
     print("X [" , x, "] Class type is: ", type(x))
     x = {"name" : "John", "age" : 36}
     print("X [" , x, "] Class type is: ", type(x))
     x = {"apple", "banana", "cherry"}
     print("X [" , x, "] Class type is: ", type(x))
     x = frozenset({"apple", "banana", "cherry"})
     print("X [" , x, "] Class type is: ", type(x))
     x = True
     print("X [" , x, "] Class type is: ", type(x))
     x = b"Hello"
     x = bytearray(5)
     print("X [" , x, "] Class type is: ", type(x))
     x = memoryview(bytes(5))
     print("X [" , x, "] Class type is: ", type(x))
     x = None
     print("X [" , x, "] Class type is: ", type(x))

def TextToHash():
     Msg = "Ingenieur Behdad Pourtavakoli"
     SHA = SHA1Hash(Msg)
     print("Hash is:", SHA)

def SHA1Hash(toHash):
     try:
          messageDigest = hashlib.sha1()
          stringM = str(toHash)
          byteM = bytes(stringM, encoding='utf')
          messageDigest.update(byteM)
          return (messageDigest.hexdigest())
     except TypeError:
          print("String to hash was not compatible")
          
def SHA1_Hash():
     # initializing string
     str = "B.S.D Group(TM)"
       
     # encoding and printing the sha1 hash value.
     result = hashlib.sha1(str.encode()).hexdigest()
     print("SHA1 Hash:", result)

def MD5_Hash():
     # initializing string
     str = "B.S.D Group(TM)"
       
     # encoding and printing the sha1 hash value.
     result = hashlib.md5(str.encode()).hexdigest()
     print("MD5 Hash : \n", result)


def id_Func_Test():
     numbers = [1, 2, 3, 4, 5]
     new_numbers = numbers

     print('numbers id: {}, new_numbers id: {}'.format(id(numbers), id(new_numbers)),"\n")

def Slicing():
     X = "Behdad Pourtavakoli"
     print(X[2:])

def StrMethods():
     X = "Behdad.Pourtavakoli.Ingenieur.Software.Developers.Entweckler"
     print(X.split(" . "))

def Converts():
     kelid=258
     kelidestan = hex(kelid)
     print("Kelid [" ,kelid, "] hexa converted is:", kelidestan)

     dec = 258
     print("The decimal value of", dec, "is:")
     print(bin(dec), "in binary.")
     print(oct(dec), "in octal.")
     print(hex(dec), "in hexadecimal.")
#endregion

#region Standardfunktionen und -verfahren
'''
///*********************************************************************************************************
///* Standardfunktionen und -verfahren                                                                     *
///*********************************************************************************************************
'''

'''
/// Mongrad1()-Funktion zum Erlernen der Python-Lektion 1 von der Website Mongrad.ir
/// 0) Intro, 1) Variable
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/07/21
/// 
'''
def Mongrad1():
     #print("print('wow')\n")

     name = "Das ist Ingenieur Behdad \'Pourtavakoli"
     print(name, "\n")

     var1 = 8 ** 5
     print(var1, "\n")

     var1 = round(12.5)
     print(var1)

'''
/// Mongrad2()-Funktion zum Erlernen der Python-Lektion 2 von der Website Mongrad.ir
/// 2) String
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/07/21
/// 
'''
def Mongrad2():
     name = 'Hallo, ich heisse Behdad Pourtavakoli.'\
            ' Ich bin Computersoftwareentwickler.'\
            ' Ich bin Computer Ingenieur.'
     print(name, " - Länge: ", len(name), "\n")

     name = ('Hallo, ich heisse Behdad Pourtavakoli.'
            ' Ich bin Computersoftwareentwickler.'
            ' Ich bin Computer Ingenieur.')
     print(name, " - Länge: ", len(name), "\n")

'''
/// Mongrad3()-Funktion zum Erlernen der Python-Lektion 3 von der Website Mongrad.ir
/// 3) List
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/07/21
/// 
'''
def Mongrad3():
     names = ["Behdad", "Software", "Developers", "Groups™", "B.S.D", "Ingeniuer"]
     names2 = ["Copyright", "Entwickler", "Engineer"]

     print("names: ", names + names2)
     print("Typ von names: ", type(names))
     print("Länge von names: ", len(names))

     names[:] = []
     print("names: ", names)

'''
/// Mongrad4()-Funktion zum Erlernen der Python-Lektion 4 von der Website Mongrad.ir
/// 3) While
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/07/26
/// 
'''
def Mongrad4():
     print("while:")

     a, b = 0, 1
     while (a < 10):
          if (a < 9):
               print(a, end=",")
          else:
               print(a)

          #a, b = b, a+b
          a = a + 1
#endregion

#region Erstellen Sie ein Tkinter-Fenster
'''
///*********************************************************************************************************
///* Erstellen Sie ein Tkinter-Fenster                                                                     *
///*********************************************************************************************************
'''

class Hello(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.make_widgets()

    def make_widgets(self):
        widget = Button(self, text="OK", command=self.destroy)
        widget.pack(side=LEFT)
        #widget.configure(state=DISABLED, background="cadetblue")
        #widget.configure(state=NORMAL, background="red")
        widget.focus_set()

'''
/// frmAboutBox_EN()-Funktion zum Erstellen eines Fensters mit Python
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/08/16
/// 
'''
def frmAboutBox_EN():

     #for f in os.listdir("."):
     #     print(f)
     #
     ##print(__name__)
     ##print ("File1 __name__ = %s" %__name__)  

     ##if __name__ == "__main__":
     ##     print ("File1 is being run directly")
     ##else:
     ##     print ("File1 is being imported")
     ##return

     frmAbout1.title("About...")
     frmAbout1.resizable(False, False)
     #frmAbout1.iconbitmap("Images/bulb.ico")
     frmAbout1.iconphoto(False, PhotoImage(file="Images/Python3.png"))

     intWidth = 450 # Width
     intHeight = 270 # Height

     screen_width = frmAbout1.winfo_screenwidth()  # Width of the screen
     screen_height = frmAbout1.winfo_screenheight() # Height of the screen

     # Calculate Starting X and Y coordinates for Window
     inyPosX = (screen_width / 2) - (intWidth / 2)
     intPosY = (screen_height / 2) - (intHeight / 2)

     frmAbout1.geometry("%dx%d+%d+%d" % (intWidth, intHeight, inyPosX, intPosY))
 
     strTitle = "Behdad Software Developers Group™ Presents\n\n"
     strTitle += "Welcome to the B.S.D Group™ Production\n\n"
     strTitle += "Copyright© 1380-1402,2001-2023 by B.S.D Group™\n"
     strTitle += "All rights reserved.\n\n"
     strTitle += "Design and develop by Engineer Behdad Pourtavakoli\n\n"
     strTitle += "®MyFirstPy2.py - B.S.D Group™\n"
     strTitle += "www.mongard.ir, coderslegacy.com, www.tutorialspoint.com are teachers...\n\n"

     lblTitle1 = Label(frmAbout1, text = strTitle).pack(pady = 15)

     cmdButton1 = Button(frmAbout1, text = "Close", command = cmdClose1, cursor="hand2", height=1, width=10)
     cmdButton1.focus_set()
     cmdButton1.pack()

     frmFrame1 = Frame(frmAbout1)
     frmFrame1.place(x=10, y=10)

     # Load and display an image 
     imageX = Image.open("Images/Python3.png")
     img_resized = imageX.resize((50, 50)) # new width & height
     imageX = ImageTk.PhotoImage(img_resized)

     # Create a label to display the image
     image_label = Label(frmFrame1, image=imageX).pack()

     #if (__name__ == "__main__"):
     #     Hello().mainloop()

     frmAbout1.mainloop()

'''
/// cmdClose1()-Funktion zum Schließen des frmAboutBox_EN-Fensters
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/08/16
/// 
'''
def cmdClose1():
     if (__name__ == '__main__'):
          frmAbout1.destroy()

'''
/// frmAboutBox_DE()-Funktion zum Erstellen eines Fensters mit Python
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/08/16
/// 
'''
def frmAboutBox_DE():

     frmAbout2.title("Über...")
     frmAbout2.resizable(False, False)
     frmAbout2.iconphoto(False, PhotoImage(file="Images/Python3.png"))

     intWidth = 450 # Width
     intHeight = 270 # Height

     screen_width = frmAbout2.winfo_screenwidth()  # Width of the screen
     screen_height = frmAbout2.winfo_screenheight() # Height of the screen

     # Calculate Starting X and Y coordinates for Window
     inyPosX = (screen_width / 2) - (intWidth / 2)
     intPosY = (screen_height / 2) - (intHeight / 2)

     frmAbout2.geometry("%dx%d+%d+%d" % (intWidth, intHeight, inyPosX, intPosY))
 
     strTitle = "Behdad Software Developers Group™ praesentiert\n\n"
     strTitle += "Willkommen bei B.S.D Group™ Produktion\n\n"
     strTitle += "Urheberrecht© 1380-1402,2001-2023 von B.S.D Group™\n"
     strTitle += "Entwurf und Entwicklung durch Ingenieur Behdad Pourtavakoli\n\n"
     strTitle += "®MyFirstPy2.py - B.S.D Group™\n"
     strTitle += "www.mongard.ir, coderslegacy.com, www.tutorialspoint.com sind Lehrer...\n\n"

     lblTitle1 = Label(frmAbout2, text = strTitle).pack(pady = 15)

     cmdButton1 = Button(frmAbout2, text = "Close", command = cmdClose2, cursor="hand2", height=1, width=10)
     cmdButton1.focus_set()
     cmdButton1.pack()

     frmFrame1 = Frame(frmAbout2)
     frmFrame1.place(x=10, y=10)

     # Load and display an image 
     imageX = Image.open("Images/Python3.png")
     img_resized = imageX.resize((50, 50)) # new width & height
     imageX = ImageTk.PhotoImage(img_resized)

     # Create a label to display the image
     image_label = Label(frmFrame1, image=imageX).pack()

     frmAbout2.mainloop()

'''
/// cmdClose2()-Funktion zum Schließen des frmAboutBox_DE-Fensters
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/08/16
/// 
'''
def cmdClose2():
     if (__name__ == '__main__'):
          frmAbout2.destroy()

'''
/// frmTestFenster()-Funktion zum Erstellen eines Fensters mit Python
/// Am Beispiel der Website coderslegacy.com
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/08/16
/// 
'''
def frmTestFenster():
     root = Tk()
     root.geometry("200x150")
     frame = Frame(root)
     frame.pack()
     
     leftframe = Frame(root)
     leftframe.pack(side=LEFT)
     
     rightframe = Frame(root)
     rightframe.pack(side=RIGHT)
     
     label = Label(frame, text = "Hello world")
     label.pack()
     
     button1 = Button(leftframe, text = "Button1", cursor="hand1")
     button1.pack(padx = 3, pady = 3)
     button2 = Button(rightframe, text = "Button2", cursor="hand2")
     button2.pack(padx = 3, pady = 3)
     button3 = Button(leftframe, text = "Button3", cursor="hand1")
     button3.pack(padx = 3, pady = 3)
     
     root.title("Test")
     root.geometry("920x500")
     frame = Frame(root)
     frame.pack(expand=True, fill=BOTH)

     cursors = """
     X_cursor
     arrow
     based_arrow_down
     based_arrow_up
     boat
     bogosity
     bottom_left_corner
     bottom_right_corner
     bottom_side
     bottom_tee
     box_spiral
     center_ptr
     circle
     clock
     coffee_mug
     cross
     cross_reverse
     crosshair
     diamond_cross
     dot
     dotbox
     double_arrow
     draft_large
     draft_small
     draped_box
     exchange
     fleur
     gobbler
     gumby
     hand1
     hand2
     heart
     icon
     iron_cross
     left_ptr
     left_side
     left_tee
     leftbutton
     ll_angle
     lr_angle
     man
     middlebutton
     mouse
     pencil
     pirate
     plus
     question_arrow
     right_ptr
     right_side
     right_tee
     rightbutton
     rtl_logo
     sailboat
     sb_down_arrow
     sb_h_double_arrow
     sb_left_arrow
     sb_right_arrow
     sb_up_arrow
     sb_v_double_arrow
     shuttle
     sizing
     spider
     spraycan
     star
     target
     tcross
     top_left_arrow
     top_left_corner
     top_right_corner
     top_side
     top_tee
     trek
     ul_angle
     umbrella
     ur_angle
     watch
     xterm""".split()

     i = 0
     j = 0
     for cur in cursors:
          if (i == 10):
               i = 0
               j += 1
          Button(frame, text=cur, height=2, width=15, cursor=cur).grid(row=i, column=j)
          i += 1

     root.mainloop()

#endregion

#region Mehrfachverarbeitung
'''
///*********************************************************************************************************
///* Mehrfachverarbeitung                                                                                  *
///*********************************************************************************************************
'''

def MultiProcessing1():
     os.system("cmd.exe /c dir c:\ /ad")
     os.system("cmd.exe /c dir d:\ /ad")
     os.system("cmd.exe /c dir e:\ /ad")

#endregion

#region Hauptprogramm
'''
/// Hauptprogramm, enthält Hauptanweisungen und Aufruffunktionen
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/07/21
/// 
'''

#frmAbout1 = Tk()
#about_EN()
#frmAboutBox_EN()

frmAbout2 = Tk()
about_DE()
frmAboutBox_DE()

#variables()

#TextToHash()
#SHA1_Hash()
#MD5_Hash()

#id_Func_Test()

#Slicing()
#StrMethods()
#Converts()

#Mongrad1()
#Mongrad2()
#Mongrad3()
#Mongrad4()

#frmTestFenster()

MultiProcessing1()

print("\nEnde des Programms...", end = "")
#endregion
