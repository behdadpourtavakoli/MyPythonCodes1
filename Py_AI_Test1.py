'''
///*-=============================================================================================-*
/// Dateiname             : Py_AI_Test1.py (Artificial Intelligence Test by Python)
/// Version               : 1.0.0.0
/// Beginn                : 2023-11-07 (1402/08/16)
/// Letzte Aktualisierung : 2023-11-07 (1402/08/16)
/// Autor                 : Ingenieur Behdad Pourtavakoli
/// Warenzeichen          : Behdad Software Developers Group™
/// ----------------------------------------------------------------------------------------------
/// Copyright© 1380-1402,2001-2023 von B.S.D Group™
/// Alle Rechte vorbehalten.
/// ----------------------------------------------------------------------------------------------
///
/// Beschreibung: Überprüfen und lernen Sie die Python-Programmierung auf den Websites 
///               docs.python.org, www.geeksforgeeks.org und www.w3schools.com
///
///-=============================================================================================-*///
'''

import os
import numpy
from scipy import stats

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
/// about_EN() funktion zur Anzeige von Programminformationen, Versionsnummer und Urheberrecht als Deutsch
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/08/16
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
     print("docs.python.org, www.geeksforgeeks.org, www.w3schools.com sind Lehrer...\n")

'''
/// ai_Func_S1()-Funktion zum Ausführen und Testen der nützlichsten Basisfunktionen der künstlichen Intelligenz
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/08/16
/// 
'''
def ai_Func_S1():
    speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
    age = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

    print("Dataset: ", speed, "\n")

    x = numpy.mean(speed)
    print("Mean function: ", x, " //* to find the average speed *")

    x = numpy.median(speed)
    print("Median function: ", x, " //* to find the middle value *")
     
    x = stats.mode(speed)
    print("Mode function: ", x, " //* to find the number that appears the most *")
     
    x = numpy.std(speed)
    print("Std function: ", x, " //* to find the standard deviation *")
     
    x = numpy.var(speed)
    print("Var function: ", x, " //* to find the variance *")

    x = numpy.percentile(age, 75)
    print("Percentile function: ", x, " //* to find the percentiles *")

    x = numpy.percentile(age, 90)
    print("Percentile function: ", x, " //* What is the age that 90% of the people are younger than? *")

    print("\n")

'''
/// ai_Func_S2()-Funktion zur Datenverteilung der Künstlichen Intelligenz
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/08/16
/// 
'''
def ai_Func_S2():
    x = numpy.random.uniform(0.00, 1.00, 100)
    print("Uniform function: //* Create an array containing 250 random floats between 0 and 5 *\n", x)

    #print("\n")
#endregion

#region Standardfunktionen und -verfahren
'''
///*********************************************************************************************************
///* Standardfunktionen und -verfahren                                                                     *
///*********************************************************************************************************
'''
#endregion

#region Hauptprogramm
'''
/// Hauptprogramm, enthält Hauptanweisungen und Aufruffunktionen
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/08/16
/// 
'''

about_DE()
ai_Func_S1()
ai_Func_S2()

print("\nEnde des Programms...", end = "")
#endregion
