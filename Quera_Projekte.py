#region Urheberrechte
'''
///*-=============================================================================================-*
/// Dateiname             : Quera_Projekte.py
/// Version               : 1.0.0.0
/// Beginn                : 2024-02-15 (1402/11/26)
/// Letzte Aktualisierung : 2024-04-05 (1403/01/17)
/// Autor                 : Ingenieur Behdad Pourtavakoli
/// Warenzeichen          : Behdad Software Developers Group™
/// ----------------------------------------------------------------------------------------------
/// Copyright© 1380-1403,2001-2024 von B.S.D Group™
/// Alle Rechte vorbehalten.
/// ----------------------------------------------------------------------------------------------
///
/// Beschreibung: Umsetzung von Quera-Website-Projekten in Python - Quera projekts
///               https://quera.org/
///
/// ----------------------------------------------------------------------------------------------
/// Das Wort des Entwicklers: Vergessen Sie nicht den Ingenieur Behdad Pourtavakoli.
///-=============================================================================================-*///
'''
#endregion

#region Wichtige Header-Dateien
'''
///*********************************************************************************************************
///* Wichtige Header-Dateien
///*********************************************************************************************************
'''
import time, math, bisect

#endregion

#region Konstanten, Variablen und Deklarationen
'''
///*********************************************************************************************************
///* Konstanten, Variablen und Deklarationen
///*********************************************************************************************************
'''
#endregion

#region Handschriftliche Funktionen und Prozeduren
'''
///*********************************************************************************************************
///* Handschriftliche Funktionen und Prozeduren
///*********************************************************************************************************
'''

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
/// Avengers() ...
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/26
/// 
'''
def Avengers():
    print("Avengers Problem Solving...\n")
    
    arrStone = ["space", "mind", "reality", "power", "time", "soul"]
    arrColor = ["blue", "yellow", "red", "purple", "green", "orange"]

    print("Enter Avenger Stone name: ", end='')
    strStone = input()
    strStone = strStone.lower()

    intFind = -1
    for intI in range(0, 6):
        if strStone == arrStone[intI]:
            intFind = intI
            break
        
    if (intFind > -1):
        print("The stone ", arrStone[intFind], " color is ", arrColor[intFind], "\n")

    Trennlinie(False, '-')

'''
/// Perfect_Number() ...
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/26
/// 
'''
def Perfect_Number():
    print("Perfect Number Problem Solving...\n")
    
    print("Enter a Number: ", end='')
    strNumber = input()
    intN = int(strNumber)
    intSum = 0

    for intI in range(1, intN):
        if (intN % intI == 0):
            intSum += intI

    if (intSum == intN):
        print("Yes")
    else:
        print("No")
    print()
    
    '''
        // Between 2 and 10000 these numbers are perfect number:
        // 6 is a perfect number
        // 28 is a perfect number
        // 496 is a perfect number
        // 8128 is a perfect number
    '''
    
    Trennlinie(False, '-')
    
'''
/// Solve_Snake() ...
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/26
/// 
'''
def Solve_Snake():
    print("Solve Snake Problem Solving...\n")
    
    print("Enter max of Snake row: ", end='')
    strTemp = input()
    intI = int(strTemp)
    
    print("Enter max of Snake col: ", end='')
    strTemp = input()
    intJ = int(strTemp)
    print()
    
    intSnake = 0
    intSnakeStat = 0
    for intM in range(0, intI):
        if (intM % 2 == 0):
            for intN in range(0, intJ):
                intSnake += 1
                print(intSnake, "\t", end='')
        else:
            intSnakeStat = intSnake
            for intN in range(intSnake + intJ, intSnakeStat, -1):
                intSnake = intN
                print(intSnake, "\t", end='')
            intSnake = intSnakeStat + intJ
        print()
    
    Trennlinie(False, '-')

'''
/// Copy_Problem() ...
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/26
/// 
'''
def Copy_Problem():
    print("Copy Problem Solving...\n")

    print("Enter Virus parameter (Separator is Space = ' '): ", end='')
    strTemp = input()
    
    arrParams = strTemp.split(" ")
    intCount = int(arrParams[0])
    strVirus = arrParams[1]
    
    for intI in range(0, intCount):
        print("copy of ", end='', sep='')
    print(strVirus, end='', sep='')
    
    Trennlinie(False, '-')

'''
/// Multiple() ...
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/27
/// 
'''
def Multiple(intNumber):
    bolResult = 0
    if (intNumber % 5 == 0):
        bolResult = 1
    return(bolResult)


'''
/// Bagher_Problem() ...
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/27
/// 
'''
def Bagher_Problem():
    print("Bagher Problem Solving...\n")

    print("Enter the 3 angles of the triangle (Separator is Space = ' '): ", end='')
    strTemp = input()
    
    arrParams = strTemp.split(" ")
    intAngle1 = int(arrParams[0])
    intAngle2 = int(arrParams[1])
    intAngle3 = int(arrParams[2])
    intSum = intAngle1 + intAngle2 + intAngle3
    
    if (intAngle1 > 0 and intAngle2 > 0 and intAngle3 > 0) and ((Multiple(intAngle1) == 1) and (Multiple(intAngle2) == 1) 
        and (Multiple(intAngle3) == 1)) and (intSum == 180):
        print("YES")
    else:
        print("NO")

    Trennlinie(False, '-')

'''
/// Right_Triangle() ...
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/27
/// 
'''
def Right_Triangle():
    print("Right Triangle Problem Solving...\n")

    print("Enter angles 1 of the triangle: ", end='')
    intAngle1 = int(input())
    
    print("Enter angles 2 of the triangle: ", end='')
    intAngle2 = int(input())
    
    print("Enter angles 3 of the triangle: ", end='')
    intAngle3 = int(input())
    
    intHypotenuse = pow(intAngle1, 2) + pow(intAngle2, 2)
    
    if (intAngle1 <= 0 or intAngle1 > 150) or (intAngle2 <= 0 or intAngle2 > 150) or (intAngle3 <= 0 or intAngle3 > 150):
        print("NO")
    elif (math.sqrt(intHypotenuse) == intAngle3):
        print("YES")
    else:
        print("NO")

    Trennlinie(False, '-')

'''
/// Mehdi_Problem() ...
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/27
/// 
'''
def Mehdi_Problem():
    print("Mehdi Problem Solving...\n")

    print("Enter Mehdi's number: ", end='')
    intNumber = int(input())
    
    if intNumber < 10 or intNumber > 1000000000:
        print("ERROR")
        return()
    
    intSum = 0
    while True:
        while (intNumber >= 10):
            intSum += int(intNumber % 10)
            intNumber /= 10

        intSum += int(intNumber % 10)

        if (intSum < 10):
            break
        else:
            intNumber = intSum
            intSum = 0
    
    print(intSum)

    Trennlinie(False, '-')

'''
/// Print_Number() ...
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/27
/// 
'''
def Print_Number():
    print("Print Number Problem Solving...\n")

    print("Enter the number: ", end='')
    strNumber = input()
    intLen = len(strNumber)
    
    if (intLen <= 0 or intLen > 100):
        print("ERROR")
        return()

    arrNumber = []
    for intI in range(0, intLen):
        arrNumber.append(str(strNumber[intI]))

    for intI in range(0, len(arrNumber)):
        intTemp = int(arrNumber[intI])
        print(str(intTemp), ": ", end='', sep='')
        for intI in range(0, intTemp):
            print(str(intTemp), end='', sep='')
        print()

    Trennlinie(False, '-')

'''
/// Amin_Routing_Problem() ...
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/28
/// 
'''
def Amin_Routing_Problem():
    print("Amin Routing Problem Solving...\n")

    print("Enter the M number: ", end='')
    intM = int(input())

    print("Enter the N number: ", end='')
    intN = int(input())

    if (intM <= 0 or intM > 4) or (intN <= 0 or intN > 4):
        return()

    if (intM == intN):
        print("0")
        return()

    Trennlinie(False, '-')

'''
/// Yellow_Answer() ...
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/28
/// 
'''
def Yellow_Answer():
    print("Yellow Answer Problem Solving...\n")

    print("Enter the Number of Information: ", end='')
    intNumber = int(input())

    if (intNumber < 1 or intNumber > 10):
        return()

    print('W', end='', sep='')
    for intI in range(0, intNumber):
        print('O', end='', sep='')
    print('W!')

    Trennlinie(False, '-')

'''
/// Mr_Khoshghalb() ...
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/28
/// 
'''
def Mr_Khoshghalb():
    print("Mr. Khoshghalb Problem Solving...\n")

    print("Enter the number of Repetitions: ", end='')
    intNumber = int(input())

    if (intNumber < 1 or intNumber > 100):
        return()

    for intI in range(0, intNumber):
        print("man khoshghlab hastam")

    Trennlinie(False, '-')

'''
/// Factorial_Problem() ...
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/28
/// 
'''
def Factorial_Problem():
    print("Factorial Problem Solving...\n")

    print("Enter the Number: ", end='')
    intNumber = int(input())

    if (intNumber < 1 or intNumber > 10):
        return()

    intFactorial = 1
    for i in range(1, intNumber+1):
        intFactorial *= i
    
    print("The Factorial Result is ", intFactorial, sep='')

    Trennlinie(False, '-')

'''
/// Power_Problem() ...
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/28
/// 
'''
def Power_Problem():
    print("Power of two Problem Solving...\n")

    print("Enter the Number: ", end='')
    intNumber = int(input())

    if (intNumber < 1 or intNumber > 10000000000):
        return()

    intTemp = int(math.sqrt(intNumber))
    intXTemp = int(math.pow(2, intTemp))
    
    print("The Result is ", intXTemp, sep='')

    Trennlinie(False, '-')

'''
/// Reverse_Numbers() ...
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/28
/// 
'''
def Reverse_Numbers():
    print("Reverse Numbers Problem Solving...\n")

    print("Enter the Numbers (To end type 0 number): ", end='')
    arrNumber = []
    while (True):
        intNumber = int(input())
        if (intNumber == 0):
            break
        else:
            arrNumber.append(intNumber)

    print("\nThe Result is: ")
    arrNumberX = arrNumber[::-1]

    for intI in range(0, len(arrNumberX)):
        print(arrNumberX[intI])

    Trennlinie(False, '-')

'''
/// Binäre Sortierfunktionen4() ...
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/28
/// 
'''
def Insert_Sort4(arrTemp):
    if (len(arrTemp) <= 1):
        return(arrTemp)
    intPivot = arrTemp[len(arrTemp) // 2]
    intLeft = [x for x in arrTemp if x < intPivot]
    intMiddle = [x for x in arrTemp if x == intPivot]
    intRight = [x for x in arrTemp if x > intPivot]
    return(Insert_Sort4(intLeft) + intMiddle + Insert_Sort4(intRight))

'''
/// Binäre Sortierfunktionen3() ...
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/28
/// 
'''
def Binary_Search3(arrTemp, intLow, intHigh):
    pivot = arrTemp[intHigh]
    intI = intLow - 1
    for intJ in range(intLow, intHigh):
        if (arrTemp[intJ] <= pivot):
            intI += 1
            (arrTemp[intI], arrTemp[intJ]) = (arrTemp[intJ], arrTemp[intI])

    (arrTemp[intI + 1], arrTemp[intHigh]) = (arrTemp[intHigh], arrTemp[intI + 1])
    return(intI + 1)
 
def Insert_Sort3(arrTemp, intLow, intHigh):
    if (intLow < intHigh):
        intPI = Binary_Search3(arrTemp, intLow, intHigh)
        Insert_Sort3(arrTemp, intLow, intPI - 1)
        Insert_Sort3(arrTemp, intPI + 1, intHigh)

'''
/// Binäre Sortierfunktionen2() ...
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/28
/// 
'''
def Binary_Search2(arrTemp, intVal, intStart, intEnd):
    if (intStart == intEnd):
        if (arrTemp[intStart] > intVal):
            return(intStart)
        else:
            return(intStart+1)
 
    if (intStart > intEnd):
        return(intStart)
 
    intMid = int((intStart+intEnd)/2)
    if (arrTemp[intMid] < intVal):
        return(Binary_Search2(arrTemp, intVal, intMid+1, intEnd))
    elif (arrTemp[intMid] > intVal):
        return(Binary_Search2(arrTemp, intVal, intStart, intMid-1))
    else:
        return(intMid)

def Insert_Sort2(arrTemp):
    for intI in range(1, len(arrTemp)):
        intValue = arrTemp[intI]
        intJ = Binary_Search2(arrTemp, intValue, 0, intI-1)
        arrTemp = arrTemp[:intJ] + [intValue] + arrTemp[intJ:intI] + arrTemp[intI+1:]
    return(arrTemp)

'''
/// Binäre Sortierfunktionen() ...
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/28
/// 
'''
def Binary_Search(arrTemp, intVal, intStart, intEnd):
    bscIndex = bisect.bisect_left(arrTemp[intStart:intEnd+1], intVal)
    return(intStart + bscIndex)
 
def Insert_Sort(arrTemp):
    for intI in range(1, len(arrTemp)):
        intVal = arrTemp[intI]
        intJ = Binary_Search(arrTemp, intVal, 0, intI-1)
        arrTemp = arrTemp[:intJ] + [intVal] + arrTemp[intJ:intI] + arrTemp[intI+1:]
    return(arrTemp)

'''
/// Fast_Sort() ...
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/28
/// 
'''
def Fast_Sort():
    print("Fast Sort Problem Solving...\n")

    print("Enter the numbers for sort (Separator is Space = ' ', to exit press Enter): ", end='')
    strTemp = input()
    arrParams = strTemp.split(" ")
    print("Sorted array: ", sep='', end='')
    arrParams = Insert_Sort4(arrParams)
    for intI in range(0, len(arrParams)):
        print(arrParams[intI], ' ', end='', sep='')
    print()

    Trennlinie(False, '-')

'''
/// Decode() ...
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/12/11
/// 
'''
def Decode():
    print("Decode the names of Bad-Men Problem Solving...\n")

    header1 = b'\x89PNG\r\n\x1a\n'      # PNG header
    header2 = b'\xff\xd8\xff'           # JPEG header
    header3 = b'\x42\x4d'               # BMP header
    header4 = b'\x49\x49\x2a\x00'       # TIFF header
    header5 = b'\x47\x49\x46\x38'       # GIF header
    header6 = b'\x50\x4b\x03\x04'       # ZIP header
    header7 = b'\x7fELF'                # ELF header
    header8 = b'\x25\x50\x44\x46'       # PDF header
    header9 = b'\x49\x44\x33'           # MP3 header
    header10 = b'\xff\xfb'              # MPEG header
    header11 = b'\x00\x00\x01\x00'      # PDDF header
    header12 = b'\x00\x01\x00\x00'      # ICO header

    print("ïICO".encode('utf-8'))
    return


    str_original = input('Please enter string data: ')
    bytes_encoded = str_original.encode()
    str_decoded = bytes_encoded.decode()
    print('Encoded bytes =', bytes_encoded)
    print('Decoded String =', str_decoded)
    print('str_original equals str_decoded =', str_original == str_decoded)
    return

    #print(header1.decode('UTF-8', 'strict'))
    #print(header2.decode('UTF-8', 'strict'))
    print(header3.decode('UTF-8', 'strict'))
    print(header4.decode('UTF-8', 'strict'))
    print(header5.decode('UTF-8', 'strict'))
    print(header6.decode('UTF-8', 'strict'))
    print(header7.decode('UTF-8', 'strict'))
    print(header8.decode('UTF-8', 'strict'))
    print(header9.decode('UTF-8', 'strict'))
    print(header10.decode('UTF-8', 'strict'))
    print(header11.decode('UTF-8', 'strict'))
    print(header12.decode('UTF-8', 'strict'))
    return

    str = "Ingenieur Behdad Pourtavakoli"
    #str = "ICO"
    string_utf = str.encode('UTF-8')
    print('The encoded version is:', string_utf)
    string_utf = str.encode('UTF-16')
    print('The encoded version is:', string_utf)

    bytes_string = b'ELF'                # ELF header
    normal_string = bytes_string.decode('UTF-8', 'strict')
    print(normal_string)
    return

    str_encoded = str.encode('utf_8', 'strict')
    print("The encoded string is: ", str_encoded)
    
    str_decoded = str_encoded.decode('utf_8', 'strict')
    print("The decoded string is: ", str_decoded)
    return

    bytes_string = b'\x89PNG\r\x1a'
    normal_string = bytes_string.decode('UTF-8', 'strict')
    print(normal_string)

    normal_string = bytes_string.decode('UTF-8', 'strict')
    print(normal_string)

    Trennlinie(False, '-')

'''
/// Salib_Problem() ...
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1403/01/17
'''
def Salib_Problem():
    print("Lösung des Subtraktionsproblems von Salim...\n")

    print("Enter the number (Two-Digits): ", end='')
    intNumber = int(input())

    intFirstNum = int(intNumber / 10)
    intSecondNum = int(intNumber % 10)

    intResult = -1
    if (intFirstNum > intSecondNum):
        intResult = intFirstNum - intSecondNum
    else:
        intResult = intSecondNum - intFirstNum
        
    print("Result: ", intResult)

    Trennlinie(False, '-')

'''
/// Words_Check() ...
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1403/01/17
'''
def Words_Check():
    print("Wörter überprüfen von Salim...\n")

    

    Trennlinie(False, '-')

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
/// 
'''
def WinMain():
    intStartTime = time.time()

    #Avengers()
    #Perfect_Number()
    #Solve_Snake()
    #Copy_Problem()
    #Bagher_Problem()
    #Right_Triangle()
    #Mehdi_Problem()
    #Print_Number()
    #Amin_Routing_Problem()
    #Yellow_Answer()
    #Mr_Khoshghalb()
    #Factorial_Problem()
    #Power_Problem()
    #Reverse_Numbers()
    #Fast_Sort()
    
    #Decode()
    
    #Salib_Problem()
    Words_Check()
    
    intEndTime = time.time()
    intElapsedTime = intEndTime - intStartTime
    print("Elapsed Time: %s ms" % round(intElapsedTime, 3))
    
    print("Press Enter key to exit...", end='')
    input()
#endregion
 
#region Hauptprogramm
'''
///*********************************************************************************************************
///* Hauptprogramm
///*********************************************************************************************************
'''
'''
/// Hauptprogramm, enthält Hauptanweisungen und Aufruffunktionen
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/11/26
/// 
'''
if (__name__ == "__main__"):
    WinMain()
#endregion
