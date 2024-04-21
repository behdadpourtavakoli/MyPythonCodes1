#region Urheberrechte
'''
///*-=============================================================================================-*
/// Dateiname             : Py_ExitConfirm5.py
/// Version               : 1.0.0.0
/// Beginn                : 2024-02-12 (1402/11/23)
/// Letzte Aktualisierung : 2024-02-12 (1402/11/23)
/// Autor                 : Ingenieur Behdad Pourtavakoli
/// Warenzeichen          : Behdad Software Developers Group™
/// ----------------------------------------------------------------------------------------------
/// Copyright© 1380-1403,2001-2024 von B.S.D Group™
/// Alle Rechte vorbehalten.
/// ----------------------------------------------------------------------------------------------
///
/// Beschreibung: Überprüfen und lernen Sie die Python-Programmierung auf den Websites 
///               (https://www.freecodecamp.org/news/python-exit-how-to-use-an-exit-function-in-
///               python-to-stop-a-program /)
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
import sys
#endregion

#region Standardfunktionen und -verfahren
'''
///*********************************************************************************************************
///* Standardfunktionen und -verfahren                                                                     *
///*********************************************************************************************************
'''

'''
/// main(), enthält Hauptanweisungen und Aufruffunktionen
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/23
/// 
'''
def main():
    try:
        print("Welcome to the program!")
        
        # Check for termination condition
        user_input = input("Do you want to exit the program? (y/n): ")
        if user_input.lower() == "y":
            exit_program()
        
        # Continue with other operations
        
    except Exception as e:
        print(f"An error occurred: {e}")
        exit_program()

def exit_program():
    print("Exiting the program...")
    sys.exit(0)
#endregion

    
#region Hauptprogramm
'''
/// Hauptprogramm, enthält Hauptanweisungen und Aufruffunktionen
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/23
/// 
'''
if (__name__ == "__main__"):
    main()
#endregion
