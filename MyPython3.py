#region Klassenbeispiel

###class Dog:
### 
###    # class attribute
###    attr1 = "mammal"
### 
###    # Instance attribute
###    def __init__(self, name):
###        self.name = name
### 
#### Driver code
#### Object instantiation
###Rodger = Dog("Rodger")
###Tommy = Dog("Tommy")
###
###print(Rodger.name)
###exit(0)
###
#### Accessing class attributes
###print("Rodger is a {}".format(Rodger.__class__.attr1))
###print("Tommy is also a {}".format(Tommy.__class__.attr1))
### 
#### Accessing instance attributes
###print("My name is {}".format(Rodger.name))
###print("My name is {}".format(Tommy.name))
###
###exit(0)

#endregion

#region Urheberrechte
'''
///*-=============================================================================================-*
/// Dateiname             : MyFirstPy3.py
/// Version               : 1.0.0.0
/// Beginn                : 2024-02-11 (1402/11/22)
/// Letzte Aktualisierung : 2024-02-11 (1402/11/22)
/// Autor                 : Ingenieur Behdad Pourtavakoli
/// Warenzeichen          : Behdad Software Developers Group™
/// ----------------------------------------------------------------------------------------------
/// Copyright© 1380-1402,2001-2024 von B.S.D Group™
/// Alle Rechte vorbehalten.
/// ----------------------------------------------------------------------------------------------
///
/// Beschreibung: Überprüfung und Erlernen der Python-Programmierung auf der w3schools-Website und
///               (https://www.mongard.ir/courses/python-beginner-course/) im PDF-Format
///
///-=============================================================================================-*///
'''
#endregion

#region Wichtige Header-Dateien
'''
///*********************************************************************************************************
///* Wichtige Header-Dateien                                                                               *
///*********************************************************************************************************
'''
import os, random, time, platform, win32gui

#endregion

#region Konstanten, Variablen und Deklarationen
'''
///*********************************************************************************************************
///* Konstanten, Variablen und Deklarationen                                                               *
///*********************************************************************************************************
'''

#endregion

#region Handschriftliche Funktionen und Prozeduren 1
'''
///*********************************************************************************************************
///* Handschriftliche Funktionen und Prozeduren 1                                                          *
///*********************************************************************************************************
'''

'''
/// KlarerBildschirm()--Funktion zum Löschen des Konsolenbildschirms unter Windows und/oder Linux
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/07/22
'''
def KlarerBildschirm():
     # For Windows
     if (os.name == 'nt'):
          _ = os.system('cls')
          #_ = subprocess.call('cls')
     # For macOS and Linux
     elif (os.name == 'posix'):
          _ = os.system('clear')
          #_ = subprocess.call('clear')

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
          
          strNachricht += "Copyright© 1380-1402,2001-2024 by B.S.D Group™\n"
          strNachricht += "All rights reserved.\n\n"
          
          strNachricht += "Design and develop by Engineer Behdad Pourtavakoli\n\n"
          
          strNachricht += "®MyFirstPy2.py (Python v" + strVersionVersionsnummer + ") - B.S.D Group™\n"
          strNachricht += "www.w3schools.com, www.mongard.ir, coderslegacy.com, www.tutorialspoint.com are teachers..."
     else:
          strNachricht = "Behdad Software Developers Group™ praesentiert\n\n"
          
          strNachricht += "Willkommen bei B.S.D Group™ Produktion\n\n"
          
          strNachricht += "Urheberrecht© 1380-1402,2001-2024 von B.S.D Group™\n"
          strNachricht += "Alle Rechte vorbehalten.\n\n"
          
          strNachricht += "Entwurf und Entwicklung durch Ingenieur Behdad Pourtavakoli\n\n"
          
          strNachricht += "®MyFirstPy2.py (Python v" + strVersionVersionsnummer + ") - B.S.D Group™\n"
          strNachricht += "www.w3schools.com, www.mongard.ir, coderslegacy.com, www.tutorialspoint.com sind Lehrer..."
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
/// 
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
/// 
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
/// 
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
/// 
'''
def WirdGeladen(intSek = 5, intWG = 0.3):
     for intTik in range(0, intSek+1):
          strOutput = "Wird geladen" + "." * intTik
          print(strOutput, end="\r")
          time.sleep(intWG)

'''
/// AktuelleZeileLöschen()-Funktion zum Löschen der aktuellen Konsolenzeile.
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/22
/// 
'''
def AktuelleZeileLöschen():
     intOSSize = os.get_terminal_size()
     for intI in range(0, intOSSize.columns-1):
          print(" ", end='')
     print('\r')
     print("\033[F", end='')

'''
/// ZufälligeDatendemo()-Funktion zur Anzeige von 6 Zufallszahlen.
/// Parameter:
/// intZählen = Anzahl der Iterations-Zufallszahlen, Standardwert: 100
/// intWG = Ruhezeit für Schleife pro Sekunde, Standardwert: 0.01
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/22
/// 
'''
def ZufälligeDatendemo(intZählen = 100, intWG = 0.01):
     for intTik in range(0, intZählen+1):
          print(random.random(), '\t', random.uniform(1, 100), '\t', random.expovariate(1 / 100), '\t', random.random(), '\t', 
                random.random(), '\t', random.uniform(1, 100), '\t', random.expovariate(1 / 100), end='\r', flush=True)
          time.sleep(intWG)
     AktuelleZeileLöschen()

'''
/// ReviewAgain()-Funktion zum Überprüfen vergangener Python-Lektionen.
/// Überprüfen Sie es noch einmal
/// https://www.w3schools.com/python/ und andere Webseiten
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/20
/// 
'''
def ReviewAgain():
     print("Überprüfen Sie es noch einmal", end="\n\n")

     intStartTime = time.time()

     WirdGeladen()
     ZufälligeDatendemo()     

     print("Zeichnen Sie 4 Dreiecke mit verschachtelten Wiederholungsschleifen - zeichnen Sie eine Raute:\n")
     RauteZeichne1()
     RauteZeichne2()
     # in Bau - in 1402/11/22
     DreieckZeichne()

     intEndTime = time.time()
     intElapsedTime = intEndTime - intStartTime
     print("Elapsed Time: %s ms" % round(intElapsedTime, 3))

     print()
#endregion

#region Standardfunktionen und -verfahren
'''
///*********************************************************************************************************
///* Standardfunktionen und -verfahren                                                                     *
///*********************************************************************************************************
'''

'''
/// main() enthält Hauptanweisungen und aufrufende Funktionen
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/23
/// 
'''
def main():
     os.system("mode con cols=168 lines=48")
     #keyboard.press('f11')
     KlarerBildschirm()

     #WirdGeladen()
     #intOSSize = os.get_terminal_size()
     #print("Bildschirmaufloesung: ", intOSSize)
     #print("Bildschirmbreite: ", intOSSize.columns)
     #print("Bildschirmhoehe: ", intOSSize.lines)
     #x = str(random.random()) + '\t' + str(random.uniform(1, 100)) + '\t' + str(random.expovariate(1 / 100)) + '\t' + str(random.random())
     #x +=  '\t' + str(random.random()) + '\t' + str(random.uniform(1, 100)) + '\t' + str(random.expovariate(1 / 100))
     #print(x)
     #print(len(x))
     #x1 = random.random()
     #x2 = random.uniform(1, 100)
     #x3 = random.expovariate(1 / 100)
     #print(x1, "\t", len(str(x1)))
     #print(x2, "\t", len(str(x2)))
     #print(x3, "\t", len(str(x3)))
     #print("Drücken Sie zum Beenden die ENTER-Taste...", end='')
     #input()
     #return

     Trennlinie(False, '=')
     Über(False)
     Trennlinie()

     ''' /// Überprüfen Sie es noch einmal - 1402/11/20 (2024/02/09) '''
     
     ReviewAgain()
     #print(convert_size(logsize))

     Trennlinie()
     print("Ende des Programms...")
     Trennlinie(False, '-')
     print("Drücken Sie zum Beenden die ENTER-Taste...", end='')
     input()
     #key = getch()
#endregion
 
#region Hauptprogramm
'''
/// Hauptprogramm, enthält Hauptanweisungen und Aufruffunktionen
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/07/21
/// UPDATE durch Ingenieur B.Pourtavakoli im 1402/11/23
/// 
'''
if (__name__ == "__main__"):
    main()
#endregion
