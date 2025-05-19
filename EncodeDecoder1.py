# region Urheberrechte
# **********************************************************************************************************
'''
///*-===========================================================================================================-*
/// Dateiname             : clsEncodeDecoder1.py
/// Version               : 1.0.0.0
/// Beginn                : 2024-10-07 (1403/07/17)
/// Letzte Aktualisierung : 2024-10-07 (1403/07/17)
/// Autor                 : Ingenieur Behdad Pourtavakoli
/// Warenzeichen          : Behdad Software Developers Group™
/// -------------------------------------------------------------------------------------------------------------
/// Copyright © 1380-1403 (2001-2024) von B.S.D Group™
/// Alle Rechte vorbehalten.
/// -------------------------------------------------------------------------------------------------------------
///
/// Beschreibung: Verschlüsseler, Entschlüsseler (Kodierer, Dekodierer)
/// 
///-============================================================================================================-*
'''
# **********************************************************************************************************
# endregion

# region Wichtige Header-Dateien
# **********************************************************************************************************
'''
///*********************************************************************************************************
///* Wichtige Header-Dateien
///*********************************************************************************************************
'''
import os, time, platform, base64, clipboard
from pathlib import Path
# **********************************************************************************************************
# endregion

# region clsEncodeDecoder1()--base class
# **********************************************************************************************************
'''
/// clsEncodeDecoder1()--base class
/// HINZUFÜGEN von Ingenieur B.Pourtavakoli am 1403/07/16
'''
class clsEncodeDecoder1:
    '''
    /// ClearScreen()--Funktion zum Löschen des Ausgabebildschirms
    /// HINZUFÜGEN von Ingenieur B.Pourtavakoli am 1403/07/16
    '''
    def ClearScreen(self):
        # if (os.name == "nt"):
        #     _ = os.system("cls")
        # elif (os.name == "posix"):
        #     _ = os.system("clear")
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    '''
    /// Trennlinie()--Funktion zum Erstellen einer Trennlinie mit einem bestimmten Zeichen.
    /// Parameter:
    /// bolLF: Zeilenvorschub, Standardwert: False
    /// chrTL: Trennzeichen, Standardwert: '*'
    /// intMax: Anzahl der Zeichenwiederholungen, Standardwert: 70
    /// HINZUFÜGEN von Ingenieur B.Pourtavakoli am 1402/11/20
    /// AKTUALISIEREN von Ingenieur B.Pourtavakoli am 1403/07/16
    '''
    def Trennlinie(self, bolLF = False, chrTL = '*', intMax = 70):
        print(*intMax*(chrTL,), sep=' ')

        if (bolLF):
            print("")

    '''
    /// Über()--Funktion zur Anzeige von Programminformationen, Versionsnummer und Urheberrecht als Englisch oder Deutsch
    /// Parameter:
    /// bolModus: Wählen Sie den Modus zwischen Englisch und Deutsch, Standardwert: True
    /// HINZUFÜGEN von Ingenieur B.Pourtavakoli am 1402/07/18
    /// AKTUALISIEREN von Ingenieur B.Pourtavakoli am 1403/07/16
    '''
    def ÜberBox(self, bolModus = True):
        strNachricht = ""
        strVersionVersionsnummer = str(platform.python_version())
        if (not bolModus):
            strNachricht = "Behdad Software Developers Group™ Presents\n\n"
            
            strNachricht += "Welcome to the B.S.D Group™ Production\n\n"
            
            strNachricht += "Copyright © 1380-1403 (2001-2024) by B.S.D Group™\n"
            strNachricht += "All rights reserved.\n\n"
            
            strNachricht += "Design and develop by Engineer Behdad Pourtavakoli\n\n"
            
            #strNachricht += "®EncodeDecoder1.py (Python v" + strVersionVersionsnummer + ") - B.S.D Group™"
            strNachricht += Path(__file__).name + " (Python v" + strVersionVersionsnummer + ") - ®B.S.D Group™"
        else:
            strNachricht = "Behdad Software Developers Group™ praesentiert\n\n"
            
            strNachricht += "Willkommen bei B.S.D Group™ Produktion\n\n"
            
            strNachricht += "Urheberrecht © 1380-1403 (2001-2024) von B.S.D Group™\n"
            strNachricht += "Alle Rechte vorbehalten.\n\n"
            
            strNachricht += "Entwurf und Entwicklung von Ingenieur Behdad Pourtavakoli\n\n"
            
            #strNachricht += "®EncodeDecoder1.py (Python v" + strVersionVersionsnummer + ") - B.S.D Group™"
            strNachricht += Path(__file__).name + " (Python v" + strVersionVersionsnummer + ") - ®B.S.D Group™"
        print(strNachricht)

    '''
    /// Verschlüsseler()--Verschlüsseln Sie den vom Benutzer eingegebenen Text function
    /// HINZUFÜGEN von Ingenieur B.Pourtavakoli am 1403/07/17
    '''
    def Verschlüsseler(self, strUserInput):
        """
        Verschlüsseln Sie den vom Benutzer eingegebenen Text function.
        
        :param a: self
        :param b: strUserInput
        :return: Ein verschlüsselter Text
        """
        bytTextBytes = strUserInput.encode('utf-16le')
        EncodedText = base64.b64encode(bytTextBytes)
        return (EncodedText.decode('utf-8'))

    '''
    /// Entschlüsseler()--Entschlüsseln Sie den verschlüsselten Text function
    /// HINZUFÜGEN von Ingenieur B.Pourtavakoli am 1403/07/17
    '''
    def Entschlüsseler(self, strEncText):
        """
        Entschlüsseln Sie den verschlüsselten Text function.
        
        :param a: self
        :param b: strEncText
        :return: Ein entschlüsselter Text
        """
        bytDecodedBytes = base64.b64decode(strEncText)
        DecodedText = bytDecodedBytes.decode('utf-16le')
        return (DecodedText)

    '''
    /// Demo()--temp function
    /// HINZUFÜGEN von Ingenieur B.Pourtavakoli am 1403/07/16
    '''
    def Demo(self):
        strText = "Ingenieur Behdad Pourtavakoli"
        print(f"Basistext: {strText}")

        # encoded_text = "aQBlAHgAIAAoAGkAdwByACAAaAB0AHQAcABzADoALwAvAGkAcABsAG8AZwBnAGUAcgAuAHIAdQAvADIANQAwADkAMgA1ACAALQBVAHMAZQBCAGEAcwBpAGMAUABhAHIAcwBpAG4AZwApAC4AQwBvAG4AdABlAG4AdAA="
        # decoded_bytes = base64.b64decode(encoded_text)
        # decoded_command = decoded_bytes.decode('utf-16le')
        # print(decoded_command)
        # print()

        # Decoder by (UTF-16 Little Endian)
        encoded_input = "aQBlAHgAIAAoAGkAdwByACAAaAB0AHQAcABzADoALwAvAGkAcABsAG8AZwBnAGUAcgAuAHIAdQAvADIANQAwADkAMgA1ACAALQBVAHMAZQBCAGEAcwBpAGMAUABhAHIAcwBpAG4AZwApAC4AQwBvAG4AdABlAG4AdAA="
        decoded_bytes = base64.b64decode(encoded_input)
        decoded_command = decoded_bytes.decode('utf-16le')
        print(f"Decoded command: {decoded_command}")

        # Encoder by (UTF-16 Little Endian)
        command_bytes = decoded_command.encode('utf-16le')
        re_encoded_command = base64.b64encode(command_bytes)
        re_encoded_command_str = re_encoded_command.decode('utf-8')
        print(f"Re-encoded command: {re_encoded_command_str}")

        print()
        
        # Encoder by (UTF-16 Little Endian)
        new_command = "Get-Process"
        command_bytes = new_command.encode('utf-16le')
        re_encoded_command = base64.b64encode(command_bytes)
        re_encoded_command_str = re_encoded_command.decode('utf-8')
        print(f"Encoded new command: {re_encoded_command_str}")

        print()

        # Encoder by (UTF-16 Little Endian)
        # new_command = "Get-Process"
        # new_command = "Get-Process; Get-Service; Get-EventLog -LogName Application > c:\\123.txt"
        # new_command = 'Get-Process; Get-Service; Get-EventLog -LogName Application | Out-File "C:\\123.txt"'
        new_command = 'Get-Process | Out-File "C:\\123.txt"; Get-Service | Out-File -Append "C:\\123.txt"; Get-EventLog -LogName Application | Out-File -Append "C:\\123.txt"'
        command_bytes = new_command.encode('utf-16le')
        encoded_command = base64.b64encode(command_bytes)
        encoded_command_str = encoded_command.decode('utf-8')
        print(f"Encoded command: {encoded_command_str}")

        decoded_bytes = base64.b64decode(encoded_command_str)
        decoded_command = decoded_bytes.decode('utf-16le')
        print(f"Decoded command: {decoded_command}")

# **********************************************************************************************************
# endregion

# region Hauptprogramm
# **********************************************************************************************************
'''
///*********************************************************************************************************
///* Hauptprogramm
///*********************************************************************************************************
'''
'''
/// WinMain()--Hauptprogramm, enthält Hauptanweisungen und aufrufende Funktionen
/// HINZUFÜGEN von Ingenieur B.Pourtavakoli am 1403/07/16
'''
def WinMain():
    
    for i in [0, 1, 2]:
        pass
    print()
    return
    intStartTime = time.time()
    
    clsED1 = clsEncodeDecoder1()
    
    while (True):
        clsED1.ClearScreen()
        clsED1.Trennlinie(False, '-')
        print("Menü:\r\n")
        print("1) Über das Programm...\t\t\tAbout...")
        print("2) Verschlüsseln Sie den Text.\t\tEncryptor")
        print("3) Entschlüsseln Sie den Text.\t\tDecryptor")
        print("4) Zeigen...\t\t\t\tDemonstrate")
        print("5) Beenden.\t\t\t\tQuit\r\n")

        strChoice = input("Bitte wählen Sie eine Option (1-5): ")
        if (strChoice == '1'):
            clsED1.ClearScreen()
            clsED1.Trennlinie(False, '-')
            clsED1.ÜberBox()
            clsED1.Trennlinie(False, '-')
        elif (strChoice == '2'):
            clsED1.ClearScreen()
            clsED1.Trennlinie(False, '-')
            
            strUserInput = input("Bitte Klartext eingeben: ")
            strEncText = clsED1.Verschlüsseler(strUserInput)
            clipboard.copy(strEncText)
            print(strEncText)
            print("\r\nGenerierter Text in die Zwischenablage kopiert.\r\n")

            clsED1.Trennlinie(False, '-')
        elif (strChoice == '3'):
            clsED1.ClearScreen()
            clsED1.Trennlinie(False, '-')
            
            strUserInput = input("Bitte geben Sie den verschlüsselten Text ein: ")
            strDecText = clsED1.Entschlüsseler(strUserInput)
            clipboard.copy(strDecText)
            print(strDecText)
            print("\r\nGenerierter Text in die Zwischenablage kopiert.\r\n")
            
            clsED1.Trennlinie(False, '-')
        elif (strChoice == '4'):
            clsED1.ClearScreen()
            clsED1.Trennlinie(False, '-')
            clsED1.Demo()
            clsED1.Trennlinie(False, '-')
        elif (strChoice == '5'):
            clsED1.ClearScreen()
            break
        else:
            print("\r\nBitte wählen Sie eine gültige Option.")

        print("\r\nDrücken Sie die Eingabetaste, um fortzufahren...", end='')
        x = input()


    clsED1.Trennlinie()
    intEndTime = time.time()
    intElapsedTime = intEndTime - intStartTime
    print("Verstrichene Zeit: %s ms" % round(intElapsedTime, 3), end='\r\n\r\n')

    # Verstrichene Zeit.  // # Elapsed Time.
    # Geschätzte Zeit.    // # Estimated Time.
    # Verbleibende Zeit.  // # Left Time.

    print("Ende des Programms...")
    clsED1.Trennlinie(False, '-')

    # print("Drücken Sie die Enter taste, um den Vorgang zu beenden...", end='')
    # x = input()
# **********************************************************************************************************
# endregion

# region Hauptprogrammaufrufer
# **********************************************************************************************************
'''
///*********************************************************************************************************
///* Hauptprogrammaufrufer
///*********************************************************************************************************
'''
'''
/// WinMain()--Hauptprogrammaufrufer, enthält den Funktionsaufrufer WinMain()
/// HINZUFÜGEN von Ingenieur B.Pourtavakoli am 1403/07/16
'''
if (__name__ == "__main__"):
    WinMain()
# **********************************************************************************************************
# endregion
