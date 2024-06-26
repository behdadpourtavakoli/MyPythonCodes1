#region Urheberrechte
'''
///*-===========================================================================================================-*
/// Dateiname             : MyFirstPy2.py
/// Version               : 1.0.0.0
/// Beginn                : 2023-06-02 (1402/03/12)
/// Letzte Aktualisierung : 2024-03-01 (1402/12/11)
/// Autor                 : Ingenieur Behdad Pourtavakoli
/// Warenzeichen          : Behdad Software Developers Group™
/// -------------------------------------------------------------------------------------------------------------
/// Copyright© 1380-1403,2001-2024 von B.S.D Group™
/// Alle Rechte vorbehalten.
/// -------------------------------------------------------------------------------------------------------------
///
/// Beschreibung: Überprüfung und Erlernen der Python-Programmierung auf der w3schools-Website und
///               (https://www.mongard.ir/courses/python-beginner-course/) im PDF-Format
///
/// Nachdem ich mit Chatgpt geplaudert hatte, empfahl es mir, einige wichtige Dinge zu lernen:
///
/// Einige einfache Python-Fragen:
///
/// Your answers are correct! Let me clarify each one:
/// 
///  1) Yes, that's correct. The code snippet swaps the values of x and y. The final output would
///  be:
///       x:10
///       y:5
///  2) A list is a mutable sequence of elements, meaning you can change its elements after creation. 
///     A tuple, on the other hand, is an immutable sequence of elements, meaning you cannot change 
///     its elements after creation.
///  3) The range() function in Python generates a sequence of numbers within a given range, usually 
///     used with the for loop. For example, range(10) generates numbers from 0 to 9.
///  4) A function in Python is defined using the def keyword, followed by the function name, parentheses, 
///     and a colon. The function body is indented and contains the code to be executed when the function 
///     is called.
///  5) A local variable is defined within a function and is only accessible within that function. A 
///     global variable is defined outside any function and is accessible throughout the program, 
///     including within functions.
///
/// Certainly! Here are a few more advanced Python questions for you:
///  1. How do you implement a singleton pattern in Python?
///  2. What is the difference between a generator and a generator expression in Python?
///  3. What is the use of the "nonlocal" keyword in Python?
///  4. How do you create a context manager in Python?
///  5. What are decorators in Python and how do you use them?
///  6. What is the purpose of the "@staticmethod" and "@classmethod" decorators in Python?
///  7. How do you implement a lazy iterator using Python's generator functions?
///  8. How do you implement a depth-first search (DFS) using Python's built-in functions and data structures?
///  9. What is the difference between a list and a tuple in Python?
///  10. How do you create a custom exception class in Python?
/// 
///-============================================================================================================-*
'''
#endregion

#region Wichtige Header-Dateien
'''
///*********************************************************************************************************
///* Wichtige Header-Dateien
///*
///* pip3 freeze > requirements.txt
///*********************************************************************************************************
'''
import os, random, time, hashlib, platform, pythoncom #, subprocess, sys, locale
from tkinter import *
from PIL import Image, ImageTk
#from datetime import datetime
from tqdm import tqdm
from progress.bar import (PixelBar, ShadyBar)
from progress.spinner import (PixelSpinner)

#endregion

#region Konstanten, Variablen und Deklarationen
'''
///*********************************************************************************************************
///* Konstanten, Variablen und Deklarationen
///*********************************************************************************************************
'''
frmAbout1 = Tk()
frmAbout2 = Tk()
#endregion

#region Handschriftliche Funktionen und Prozeduren 1
'''
///*********************************************************************************************************
///* Handschriftliche Funktionen und Prozeduren 1
///*********************************************************************************************************
'''

'''
/// KlarerBildschirm()--Funktion zum Löschen des Konsolenbildschirms unter Windows und/oder Linux
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/07/22
'''
def KlarerBildschirm():
     # For Windows
     if (os.name == "nt"):
          _ = os.system("cls")
          #_ = subprocess.call("cls")
     # For macOS and Linux
     elif (os.name == "posix"):
          _ = os.system("clear")
          #_ = subprocess.call("clear")

'''
/// Über()-Funktion zur Anzeige von Programminformationen, Versionsnummer und Urheberrecht als Englisch oder Deutsch
/// Parameter:
/// bolModus: Wählen Sie den Modus zwischen Englisch und Deutsch, Standardwert: True
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/07/18
/// UPDATE durch Ingenieur B.Pourtavakoli im 1402/11/22
'''
def Über(bolModus = True):
     strNachricht = ""
     strVersionVersionsnummer = str(platform.python_version())
     if (bolModus == True):
          strNachricht = "Behdad Software Developers Group™ Presents\n\n"
          
          strNachricht += "Welcome to the B.S.D Group™ Production\n\n"
          
          strNachricht += "Copyright© 1380-1403,2001-2024 by B.S.D Group™\n"
          strNachricht += "All rights reserved.\n\n"
          
          strNachricht += "Design and develop by Engineer Behdad Pourtavakoli\n\n"
          
          strNachricht += "®MyFirstPy2.py (Python v" + strVersionVersionsnummer + ") - B.S.D Group™\n"
          strNachricht += "www.w3schools.com, www.mongard.ir, coderslegacy.com, www.tutorialspoint.com, Telegram ChatGPT, and more websites are teachers..."
     else:
          strNachricht = "Behdad Software Developers Group™ praesentiert\n\n"
          
          strNachricht += "Willkommen bei B.S.D Group™ Produktion\n\n"
          
          strNachricht += "Urheberrecht© 1380-1403,2001-2024 von B.S.D Group™\n"
          strNachricht += "Alle Rechte vorbehalten.\n\n"
          
          strNachricht += "Entwurf und Entwicklung durch Ingenieur Behdad Pourtavakoli\n\n"
          
          strNachricht += "®MyFirstPy2.py (Pythonv" + strVersionVersionsnummer + ") - B.S.D Group™\n"
          strNachricht += "www.w3schools.com, www.mongard.ir, coderslegacy.com, www.tutorialspoint.com, Telegram ChatGPT, and more websites sind Lehrer..."
     print(strNachricht)

'''
/// Trennlinie()-Funktion zum Erstellen einer Trennlinie mit einem bestimmten Zeichen.
/// Parameter:
/// bolLF: Zeilenvorschub, Standardwert: False
/// chrTL: Trennzeichen, Standardwert: '*'
/// intMax: Anzahl der Zeichenwiederholungen, Standardwert: 70
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/20
/// UPDATE durch Ingenieur B.Pourtavakoli im Jahr 1402/11/22
'''
def Trennlinie(bolLF = False, chrTL = '*', intMax = 70):
     print(*intMax*(chrTL,), sep=' ')
     #print(chrTL * intMax, sep='_')

     if (bolLF):
          print("")

'''
/// DreieckZeichne()-Funktion zum Zeichne eine Dreieck.
/// Parameter:
/// intType: Zeichenmodus, Einzelheiten: 1=Top Left, 2=Top Right, 3=Bottom Left, 4=Bottom Right, Standardwert: 1
/// intLength = Die Tiefe des Dreiecks, Standardwert: 10
/// chrDraw = Charakter zeichnen, Standardwert: '*'
/// chrSpace = Leerer Designraum, Standardwert: ' '
/// chrEndSpace = Leerer Design-Endraum, Standardwert: ' '
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/22
'''
def DreieckZeichne(intType = 1, intLength = 10, chrDraw = '*', chrSpace = ' ', chrEndSpace = ' '):
     for intI in range(intLength, 0, -1):
          for intK in range(0, intI, 1):
               print(chrSpace, end=chrEndSpace)

          for intJ in range(intLength+1, intI, -1):
               print(chrDraw, end=chrEndSpace)

          for intK in range(intI, intLength, 1):
               print(chrDraw, end=chrEndSpace)
          print()
     print()

'''
/// RauteZeichne1()-Funktion zum Zeichne eine Raute.
/// Parameter:
/// intLength = Die Tiefe des Dreiecks, Standardwert: 10
/// chrDraw = Charakter zeichnen, Standardwert: '*'
/// chrSpace = Leerer Designraum, Standardwert: ' '
/// chrEndSpace = Leerer Design-Endraum, Standardwert: ' '
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/22
'''
def RauteZeichne1(intLength = 10, chrDraw = '*', chrSpace = ' ', chrEndSpace = ' '):
     for intI in range(intLength, 0, -1):
          for intK in range(0, intI, 1):
               print(chrSpace, end=chrEndSpace)

          for intJ in range(intLength+1, intI, -1):
               print(chrDraw, end=chrEndSpace)

          for intK in range(intI, intLength, 1):
               print(chrDraw, end=chrEndSpace)
          print()

     for intI in range(0, intLength+1, 1):
          for intK in range(0, intI, 1):
               print(chrSpace, end=chrEndSpace)

          for intJ in range(intLength+1, intI, -1):
               print(chrDraw, end=chrEndSpace)

          for intJ in range(intI, intLength, 1):
               print(chrDraw, end=chrEndSpace)
          print()
     print()

'''
/// RauteZeichne2()-Funktion zum Zeichne eine Raute.
/// Parameter:
/// intLength = Die Tiefe des Dreiecks, Standardwert: 10
/// chrDraw = Charakter zeichnen, Standardwert: '*'
/// chrSpace = Leerer Designraum, Standardwert: ' '
/// chrEndSpace1 = Leerer Design-Endraum, Standardwert: ''
/// chrEndSpace2 = Leerer Design-Endraum, Standardwert: ' '
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/22
'''
def RauteZeichne2(intLength = 11, chrDraw = '*', chrSpace = ' ', chrEndSpace1 = '', chrEndSpace2 = ' '):
     intI = 1
     intJ = 1
     intK = intLength
     while (intI < intLength):
          while (intK > intI):
               print(chrSpace, end=chrEndSpace1)
               intK -= 1

          while (intJ < intI):
               print(chrDraw, end=chrEndSpace2)
               intJ += 1

          intI += 1
          intJ = 1
          intK = intLength
          print()

     intI = intLength
     intJ = 1
     intK = intLength
     while (intI > 1):
          while (intK > intI):
               print(chrSpace, end=chrEndSpace1)
               intK -= 1

          while (intJ < intI):
               print(chrDraw, end=chrEndSpace2)
               intJ += 1

          intI -= 1
          intJ = 1
          intK = intLength
          print()
     print()

'''
/// WirdGeladen()-Funktion um das Warten etwas zu verkürzen.
/// Parameter:
/// intSek = Sekunden zum Warten, Standardwert: 5
/// intWG = Ruhezeit für Schleife pro Sekunde, Standardwert: 0.3
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/22
'''
def WirdGeladen(intSek = 5, intWG = 0.3):
     for intTik in range(0, intSek+1):
          strOutput = "Wird geladen" + "." * intTik
          print(strOutput, end="\r")
          pythoncom.PumpWaitingMessages()
          time.sleep(intWG)

'''
/// WirdGeladen2()-Funktion um das Warten etwas zu verkürzen.
/// Parameter:
/// intMax = Maximale Länge des Fortschrittsbalkens, Standardwert: 100
/// intTyp = Art des Fortschrittsbalkens, Standardwert: 1
/// intSec = maximale Wartezeit in Sekunden, Standardwert: 10 Sekunden
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/12/12
'''
def WirdGeladen2(intMax = 100, intTyp = 1, intSek = 10):

     suffix = '%(percent)d%% [%(elapsed_td)s / %(eta)d / %(eta_td)s]'
     with PixelSpinner('Processing...', suffix=suffix) as bar:
          for i in range(intMax):
               # Etwas tun.
               intSleep = (random.randint(1, intSek)) / 100
               time.sleep(intSleep)
               pythoncom.PumpWaitingMessages()
               bar.next()

     return()

     # classic, classic2, smooth, blocks, bubbles, hollow, solid, circles, squares, checks, filling
     #with alive_bar(150, bar = 'classic2', spinner = 'notes') as bar:
     #with alive_bar(150, bar = 'classic2', spinner = '') as bar:
     #     for i in range(150):
     #          sleep(0.005)
     #          bar()
     
     #with Bar("Processing…") as bar:
     #with Bar("Loading", fill='…', suffix="%(percent).1f%% - %(eta)ds") as bar:
     #with Bar("Loading", fill='*', suffix="%(percent).1f%% - %(eta)ds") as bar:
     #with Bar("Loading", fill='#', suffix="%(percent).1f%% - %(eta)ds") as bar:
     #with MoonSpinner('Processing…') as bar:
          #for intLoop in range(intMax):
          #     # Etwas tun.
          #     intSleep = (random.randint(1, intSek)) / 100
          #     sleep(intSleep)
          #     pythoncom.PumpWaitingMessages()
          #     bar.next()
          
     #intMAX = int(9e6)
     #intMAX = 100
     intSek = 10
     
     for i in tqdm(range(intMAX)):
          # Etwas tun.
          intSleep = (random.randint(1, intSek)) / 150
          time.sleep(intSleep)
          pythoncom.PumpWaitingMessages()
          pass
     
     for i in tqdm(range(intMAX), ncols=62):
          # Etwas tun.
          intSleep = (random.randint(1, intSek)) / 150
          time.sleep(intSleep)
          pythoncom.PumpWaitingMessages()
          pass
          
     for i in tqdm(range(intMAX), ascii=True, desc="Progress:"):
          # Etwas tun.
          intSleep = (random.randint(1, intSek)) / 150
          time.sleep(intSleep)
          pythoncom.PumpWaitingMessages()
          pass

'''
/// AktuelleZeileLöschen()-Funktion zum Löschen der aktuellen Konsolenzeile.
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/22
'''
def AktuelleZeileLöschen():
     intOSSize = os.get_terminal_size()
     for intI in range(1, intOSSize.columns-1):
          print(" ", end='')
     print('\r')
     print("\033[F", end='')

'''
/// ZufälligeDatendemo()-Funktion zur Anzeige von 6 Zufallszahlen.
/// Parameter:
/// intZählen = Anzahl der Iterations-Zufallszahlen, Standardwert: 100
/// intWG = Ruhezeit für Schleife pro Sekunde, Standardwert: 0.01
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/22
'''
def ZufälligeDatendemo(intZählen = 100, intWG = 0.01):
     for intTik in range(0, intZählen+1):
          print(random.random(), '\t', random.uniform(1, 100), '\t', random.expovariate(1 / 100), '\t', random.random(), '\t', 
                random.random(), '\t', random.uniform(1, 100), '\t', random.expovariate(1 / 100), end='\r', flush=True)
          time.sleep(intWG)
     print()
     print()
     AktuelleZeileLöschen()

'''
/// ReviewAgain()-Funktion zum Überprüfen vergangener Python-Lektionen.
/// Überprüfen Sie es noch einmal
/// https://www.w3schools.com/python/ und andere Webseiten
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/20
'''
def ReviewAgain():
     print("Überprüfen Sie es noch einmal", end="\n\n")

     WirdGeladen()
     ZufälligeDatendemo()     

     print("Zeichnen Sie 4 Dreiecke mit verschachtelten Wiederholungsschleifen - zeichnen Sie eine Raute:\n")
     RauteZeichne1()
     RauteZeichne2()
     # in Bau - in 1402/11/22
     DreieckZeichne()

     print()
#endregion

#region Handschriftliche Funktionen und Prozeduren 2
'''
///*********************************************************************************************************
///* Handschriftliche Funktionen und Prozeduren 2
///*********************************************************************************************************
'''

'''
/// variables() Funktion zum Erstellen ...
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/07/18
'''
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

'''
/// TextToHash() Funktion zum Erstellen ...
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/07/18
'''
def TextToHash():
     Msg = "Ingenieur Behdad Pourtavakoli"
     SHA = SHA1Hash(Msg)
     print("Hash is:", SHA)

'''
/// SHA1Hash() Funktion zum Erstellen ...
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/07/18
'''
def SHA1Hash(toHash):
     try:
          messageDigest = hashlib.sha1()
          stringM = str(toHash)
          byteM = bytes(stringM, encoding='utf')
          messageDigest.update(byteM)
          return (messageDigest.hexdigest())
     except TypeError:
          print("String to hash was not compatible")
          
'''
/// SHA1_Hash() Funktion zum Erstellen ...
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/07/18
'''
def SHA1_Hash():
     # initializing string
     str = "B.S.D Group(TM)"
       
     # encoding and printing the sha1 hash value.
     result = hashlib.sha1(str.encode()).hexdigest()
     print("SHA1 Hash:", result)

'''
/// MD5_Hash() Funktion zum Erstellen ...
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/07/18
'''
def MD5_Hash():
     # initializing string
     str = "B.S.D Group(TM)"
       
     # encoding and printing the sha1 hash value.
     result = hashlib.md5(str.encode()).hexdigest()
     print("MD5 Hash : \n", result)

'''
/// id_Func_Test() Funktion zum Erstellen ...
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/07/18
'''
def id_Func_Test():
     numbers = [1, 2, 3, 4, 5]
     new_numbers = numbers

     print('numbers id: {}, new_numbers id: {}'.format(id(numbers), id(new_numbers)),"\n")

'''
/// Slicing() Funktion zum Erstellen ...
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/07/18
'''
def Slicing():
     X = "Behdad Pourtavakoli"
     print(X[2:])

'''
/// StrMethods() Funktion zum Erstellen ...
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/07/18
'''
def StrMethods():
     X = "Behdad.Pourtavakoli.Ingenieur.Software.Developers.Entweckler"
     print(X.split(" . "))

'''
/// Converts() Funktion zum Erstellen ...
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/07/18
'''
def Converts():
     kelid=258
     kelidestan = hex(kelid)
     print("Kelid [" ,kelid, "] hexa converted is:", kelidestan)

     dec = 258
     print("The decimal value of", dec, "is:")
     print(bin(dec), "in binary.")
     print(oct(dec), "in octal.")
     print(hex(dec), "in hexadecimal.")

'''
/// Mongrad1()-Funktion zum Erlernen der Python-Lektion 1 von der Website Mongard.ir
/// 0) Intro, 1) Variable
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/07/21
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
/// Mongrad2()-Funktion zum Erlernen der Python-Lektion 2 von der Website Mongard.ir
/// 2) String
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/07/21
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
/// Mongrad3()-Funktion zum Erlernen der Python-Lektion 3 von der Website Mongard.ir
/// 3) List
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/07/21
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
/// Mongrad4()-Funktion zum Erlernen der Python-Lektion 4 von der Website Mongard.ir
/// 3) While
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/07/26
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

'''
/// ErrorHandling()-Funktion zum Erlernen der Python-Lektionen von dem ChatGPT
/// Sehen Sie sich die Python-Lektionen von Anfang an an:
/// Lektion 1: Einführung in Python -- Kursiert.
/// Lektion 2: Datentypen           -- Kursiert.
/// Lektion 3: Operatoren           -- Kursiert.
/// Lektion 4: Kontrollstrukturen   -- Kursiert.
/// Lektion 5: Fehlerbehandlung     -- Neue Lektion
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/12/13
'''
def ErrorHandling():
     try:
          x = int(input("Enter a number: "))
          print(10 / x)
     except ValueError:
          print("Invalid input. Please enter a valid number.")
     except ZeroDivisionError:
          print("Cannot divide by zero.")
     print()

'''
/// ChatGPT1()-Funktion zum Erlernen der Python-Lektionen von dem ChatGPT
/// Lektion 6: Dateihandhabung (Wortanzahl, Zeichenanzahl, Durchschnittliche Wörter pro Zeile, 
///            Längstes Wort, Kürzestes Wort)
/// 
/// HINZUGEFÜGT von Ingenieur B.Pourtavakoli im Jahr 1402/12/11 und einige Änderungen im Jahr 1402/12/14
'''
def ChatGPT1():
     try:
          strFilename1 = "Text-Editor\\License"
          file1 = open(strFilename1, 'r')
          contents1 = file1.read()
          #print(contents1)

          words = contents1.split()
          word_count = len(words)
          print("Word count:", word_count)

          char_count = len(contents1)
          print("Character count:", char_count)

          print("Average words per line:", word_count / contents1.count(''))
          print("Longest word:", max(words, key=len))
          print("Shortest word:", min(words, key=len))
          
          lines = contents1.split('''
          ''')
          word_counts = [len(line.split()) for line in lines]
          print("Average words per line:", sum(word_counts) / len(word_counts), "\n")
     except FileNotFoundError:
          print("The file", strFilename1, "does not exist.")
     except IsADirectoryError:
          print("It's a directory, not a file.")
     except PermissionError:
          print("The Permission denied.")
     except FileExistsError:
          print("The File Exists Error")
     except NotADirectoryError:
          print("Not a Directory Error")
     except NotImplementedError:
          print("Not Implemented Error")
     except Exception as ex:
          print("An unexpected error occurred:", ex)
     finally:
          file1.close()

     try:
          strFilename2 = "License"
          
          if (os.path.exists(strFilename2)):
               print("The file", strFilename2, "is already exist, The new file is overwritten.")
          #else:
          #     print("The file does not exist.")
          
          file2 = open(strFilename2, 'w')
          file2.write(contents1)
     except FileNotFoundError:
          print("The file", strFilename2, "does not exist.")
     except IsADirectoryError:
          print("It's a directory, not a file.")
     except PermissionError:
          print("The Permission denied.")
     except FileExistsError:
          print("The File Exists Error")
     except NotADirectoryError:
          print("Not a Directory Error")
     except NotImplementedError:
          print("Not Implemented Error")
     except Exception as ex:
          print("An unexpected error occurred:", ex)
     finally:
          file2.close()
          print("The file", strFilename2, "created successfully.")

'''
/// DataTypeRecognizer()-Funktion zur Bereitstellung eines klaren Erkennungsdatentyps
/// Dieser Code ruft jeden Datentyp ab und entfernt alle Nicht-Datentypen wie "<class '...'>"
/// HINZUGEFÜGT von Ingenieur B.Pourtavakoli am 1402/12/25
'''
def DataTypeRecognizer(varDataType):
     return(str(type(varDataType)).replace("<class '", "").replace("'>", ""))

'''
/// W3Schools1()-Funktion zum Erlernen der Python-Lektionen von der Website tqdm.github.io, w3schools.com
/// Fortschrittsbalken von tqdm
/// HINZUGEFÜGT von Ingenieur B.Pourtavakoli im Jahr 1402/12/11 und einige Änderungen im Jahr 1402/12/25
'''
def W3Schools1():
     lstMultiDataType = [36, 23.5, False, "Wow", 99, True]
     myList = ((36, 23.5, False, "Wow", 99, True))
     print("Multi Datatype ", lstMultiDataType, " is ", type(lstMultiDataType), " and length is ", len(lstMultiDataType))
     print("Multi Datatype ", myList, " is ", type(myList), " and length is ", len(myList))
     
     a1 = DataTypeRecognizer(lstMultiDataType)
     a2 = DataTypeRecognizer(myList)
     
     print(a1, a2)

     print()

#endregion

#region Erstellen Sie ein Tkinter-Fenster
'''
///*********************************************************************************************************
///* Erstellen Sie ein Tkinter-Fenster
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
 
     strTitle =  "Behdad Software Developers Group™ Presents\n\n"
     strTitle += "Welcome to the B.S.D Group™ Production\n\n"
     strTitle += "Copyright© 1380-1403,2001-2024 by B.S.D Group™\n"
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
'''
def cmdClose1():
     if (__name__ == '__main__'):
          frmAbout1.destroy()

'''
/// frmAboutBox_DE()-Funktion zum Erstellen eines Fensters mit Python
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/08/16
'''
def frmAboutBox_DE():

     intWidth = 450 # Width
     intHeight = 270 # Height

     screen_width = frmAbout2.winfo_screenwidth()  # Width of the screen
     screen_height = frmAbout2.winfo_screenheight() # Height of the screen

     frmAbout2.title("Über...")
     frmAbout2.resizable(False, False)
     frmAbout2.iconphoto(False, PhotoImage(file="Images/Python3.png"))


     # Calculate Starting X and Y coordinates for Window
     inyPosX = (screen_width / 2) - (intWidth / 2)
     intPosY = (screen_height / 2) - (intHeight / 2)

     frmAbout2.geometry("%dx%d+%d+%d" % (intWidth, intHeight, inyPosX, intPosY))
 
     strTitle = "Behdad Software Developers Group™ praesentiert\n\n"
     strTitle += "Willkommen bei B.S.D Group™ Produktion\n\n"
     strTitle += "Urheberrecht© 1380-1403,2001-2024 von B.S.D Group™\n"
     strTitle += "Entwurf und Entwicklung durch Ingenieur Behdad Pourtavakoli\n\n"
     strTitle += "®MyFirstPy2.py - B.S.D Group™\n"
     strTitle += "www.w3schools.com, www.mongard.ir, coderslegacy.com, www.tutorialspoint.com, Telegram ChatGPT, and more websites sind Lehrer...\n\n"

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
'''
def cmdClose2():
     if (__name__ == '__main__'):
          frmAbout2.destroy()

'''
/// frmTestFenster()-Funktion zum Erstellen eines Fensters mit Python
/// Am Beispiel der Website coderslegacy.com
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/08/16
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
///* Mehrfachverarbeitung
///*********************************************************************************************************
'''

def MultiProcessing1():
     os.system("cmd.exe /c dir c:\\ /ad")
     os.system("cmd.exe /c dir d:\\ /ad")
     os.system("cmd.exe /c dir e:\\ /ad")

#endregion

#region Standardfunktionen und -verfahren
'''
///*********************************************************************************************************
///* Standardfunktionen und -verfahren
///*********************************************************************************************************
'''

'''
/// WinMain() enthält Hauptanweisungen und aufrufende Funktionen
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/26
'''
def WinMain():
     intStartTime = time.time()

     KlarerBildschirm()
     Trennlinie(False, '=')
     Über(False)
     Trennlinie()
     
     #frmAboutBox_EN()
     #frmAboutBox_DE()

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

     #MultiProcessing1()

     ''' /// Überprüfen Sie es noch einmal - 1402/11/20 (2024/02/09) '''
     #ReviewAgain()
     #WirdGeladen2()

     ''' /// Überprüfen Sie es noch einmal - 1402/12/12 (2024/03/02) '''
     #ChatGPT1()
     W3Schools1()
          
     Trennlinie()
     intEndTime = time.time()
     intElapsedTime = intEndTime - intStartTime
     print("Verstrichene Zeit: %s ms" % round(intElapsedTime, 3))

     print("Ende des Programms...")
     Trennlinie(False, '-')

     #print("Drücken Sie die Eingabetaste, um den Vorgang zu beenden...", end='')
     #frmAbout1 = frmAbout2 = None
     #x = input()
     #Trennlinie(False, '-')

#endregion

#region Hauptprogramm
'''
///*********************************************************************************************************
///* Hauptprogramm
///*********************************************************************************************************
'''
'''
/// Hauptprogramm, enthält Hauptanweisungen und Aufruffunktionen
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/07/21
'''
if (__name__ == "__main__"):
    WinMain()

#endregion
