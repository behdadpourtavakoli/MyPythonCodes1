# region Urheberrechte
# **********************************************************************************************************
'''
///*-===========================================================================================================-*
/// Dateiname             : EncryptedMessenger.py
/// Version               : 1.0.0.0
/// Beginn                : 2024-09-29 (1403/07/08)
/// Letzte Aktualisierung : 2024-10-04 (1403/07/13)
/// Autor                 : Ingenieur Behdad Pourtavakoli
/// Warenzeichen          : Behdad Software Developers Group™
/// -------------------------------------------------------------------------------------------------------------
/// Copyright © 1380-1403 (2001-2024) von B.S.D Group™
/// Alle Rechte vorbehalten.
/// -------------------------------------------------------------------------------------------------------------
///
/// Beschreibung: Verschlüsselter Messenger
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
import os, time, base64, random, string, platform
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from pathlib import Path
# **********************************************************************************************************
# endregion

# region clsEncryptedMessenger()--base class
# **********************************************************************************************************
'''
/// clsEncryptedMessenger()--base class
/// HINZUFÜGEN von Ingenieur B.Pourtavakoli am 1403/07/08
'''
class clsEncryptedMessenger:
    '''
    /// ClearScreen()--Funktion zum Löschen des Ausgabebildschirms
    /// HINZUFÜGEN von Ingenieur B.Pourtavakoli am 1403/07/08
    '''
    def ClearScreen(self):
        if (os.name == "nt"):
            _ = os.system("cls")
        elif (os.name == "posix"):
            _ = os.system("clear")

    '''
    /// Trennlinie()--Funktion zum Erstellen einer Trennlinie mit einem bestimmten Zeichen.
    /// Parameter:
    /// bolLF: Zeilenvorschub, Standardwert: False
    /// chrTL: Trennzeichen, Standardwert: '*'
    /// intMax: Anzahl der Zeichenwiederholungen, Standardwert: 70
    /// HINZUFÜGEN von Ingenieur B.Pourtavakoli am 1402/11/20
    /// AKTUALISIEREN von Ingenieur B.Pourtavakoli am 1403/07/08
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
    /// AKTUALISIEREN von Ingenieur B.Pourtavakoli am 1403/07/08
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
            
            #strNachricht += "®MyPython2.py (Python v" + strVersionVersionsnummer + ") - B.S.D Group™\n"
            strNachricht += Path(__file__).name + " (Python v" + strVersionVersionsnummer + ") - ®B.S.D Group™\n"
        else:
            strNachricht = "Behdad Software Developers Group™ praesentiert\n\n"
            
            strNachricht += "Willkommen bei B.S.D Group™ Produktion\n\n"
            
            strNachricht += "Urheberrecht © 1380-1403 (2001-2024) von B.S.D Group™\n"
            strNachricht += "Alle Rechte vorbehalten.\n\n"
            
            strNachricht += "Entwurf und Entwicklung von Ingenieur Behdad Pourtavakoli\n\n"
            
            #strNachricht += "®MyPython2.py (Pythonv" + strVersionVersionsnummer + ") - B.S.D Group™\n"
            strNachricht += Path(__file__).name + " (Python v" + strVersionVersionsnummer + ") - ®B.S.D Group™\n"
        print(strNachricht)

    '''
    /// # AES Encryptor Level 5: Generate a 32-byte key for AES-256
    /// # At this level, random and unique keys are generated for each cryptographic session. This greatly increases security.
    /// HINZUFÜGEN von Ingenieur B.Pourtavakoli am 1403/07/08
    '''
    def Generate_Key(self):
        return (os.urandom(32))

    '''
    /// # Level 5: Encryption using random keys (more security)
    /// HINZUFÜGEN von Ingenieur B.Pourtavakoli am 1403/07/08
    '''
    def AES_Encrypt_L5(self, plain_text, key):
        cipher = AES.new(key, AES.MODE_CBC)
        iv = cipher.iv
        encrypted_bytes = cipher.encrypt(pad(plain_text.encode('utf-8'), AES.block_size))
        return (base64.b64encode(iv + encrypted_bytes).decode('utf-8'))

    '''
    /// # AES Decryptor Level 5: Simple example
    /// HINZUFÜGEN von Ingenieur B.Pourtavakoli am 1403/07/08
    '''
    def AES_Decrypt_L5(self, encrypted_text, key):
        encrypted_data = base64.b64decode(encrypted_text)
        iv = encrypted_data[:16]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_bytes = unpad(cipher.decrypt(encrypted_data[16:]), AES.block_size)
        return decrypted_bytes.decode('utf-8')

    '''
    /// # AES Decryptor Level 5: Simple example
    /// HINZUFÜGEN von Ingenieur B.Pourtavakoli am 1403/07/08
    '''
    def Encrypted_Formated(self, encrypted_text, block_size=5):
        formatted_text = ' '.join([encrypted_text[i:i+block_size] for i in range(0, len(encrypted_text), block_size)])
        return (formatted_text)
    
    '''
    /// # AES Decryptor Level 5: Simple example
    /// HINZUFÜGEN von Ingenieur B.Pourtavakoli am 1403/07/08
    '''
    def Add_Random_Data(self, text, length=10):
        random_data = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        return (text + random_data)
    
    '''
    /// # AES Decryptor Level 5: Simple example
    /// HINZUFÜGEN von Ingenieur B.Pourtavakoli am 1403/07/08
    '''
    def Remove_Random_Data(self, decrypted_text, random_data_length=10):
        return (decrypted_text[:-random_data_length])

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
/// HINZUFÜGEN von Ingenieur B.Pourtavakoli am 1403/07/08
'''
def WinMain():
    intStartTime = time.time()
    
    clsEM = clsEncryptedMessenger()
    clsEM.ClearScreen()
    clsEM.Trennlinie(False, '-')
    clsEM.ÜberBox()
    clsEM.Trennlinie(False, '-')


    while (1):
        print("")
    strText = "Behdad Pourtavakoli"
    # print(f"Klartext: {strText}")

    strText_PlusRndData = clsEM.Add_Random_Data(strText)
    print(f"Klartext + zufällige Daten: {strText_PlusRndData}")

    strKey = clsEM.Generate_Key()
    encEncrypted = clsEM.AES_Encrypt_L5(strText_PlusRndData, strKey)
    print(f"Verschlüsselter Text nach Level 5: {encEncrypted} - Länge: {len(encEncrypted)}")
    # print(f"Verschlüsselter Text nach Level 5 + Format: {clsEM.Encrypted_Formated(encEncrypted)} - Länge: {len(encEncrypted)}")

    clsEM.Trennlinie()
    intEndTime = time.time()
    intElapsedTime = intEndTime - intStartTime
    print("Verstrichene Zeit: %s ms" % round(intElapsedTime, 3), end='\r\n\r\n')

    # Verstrichene Zeit.  // # Elapsed Time.
    # Geschätzte Zeit.    // # Estimated Time.
    # Verbleibende Zeit.  // # Left Time.

    print("Ende des Programms...")
    clsEM.Trennlinie(False, '-')

    print("Drücken Sie die Enter taste, um den Vorgang zu beenden...", end='')
    x = input()
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
/// HINZUFÜGEN von Ingenieur B.Pourtavakoli am 1403/07/08
'''
if (__name__ == "__main__"):
    WinMain()
# **********************************************************************************************************
# endregion
