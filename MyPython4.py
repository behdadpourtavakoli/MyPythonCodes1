# region Copyright
# **********************************************************************************************************
'''
///*-=============================================================================================-*
/// File name      : MyPython4.py
/// Version        : 1.0.0.0
/// Start          : 2024-09-07 (1403/06/17)
/// Last update    : 2024-09-07 (1403/06/17)
/// Autor          : Engineer Behdad Pourtavakoli
/// Trademark      : Behdad Software Developers Group™
/// ----------------------------------------------------------------------------------------------
/// Copyright © 1380-1403 (2001-2024) by B.S.D Group™
/// All rights reserved.
/// ----------------------------------------------------------------------------------------------
///
/// Description: Review and revise the Python learning
///
/// ----------------------------------------------------------------------------------------------
/// The developer's word: Do not forget the engineer Behdad Pourtavakoli.
///-=============================================================================================-*
'''
# **********************************************************************************************************
# endregion

# region Important header files
'''
///*********************************************************************************************************
///* Important header files
///*********************************************************************************************************
'''
from tqdm import tqdm
from tqdm.notebook import tqdm
import time, os, pytesseract#, pytesseract
from PIL import Image
from pathlib import Path
from alive_progress import alive_bar
from alive_progress.styles import showtime
from alive_progress.styles import showtime
# endregion

# region constants, variables and declarations
# **********************************************************************************************************
'''
///*********************************************************************************************************
///* constants, variables and declarations
///*********************************************************************************************************
'''

x = "Behdad"
a = 258
b = 3.14
c = 0x001230
d = 1j
e = ["apple", "banana", "cherry"]
f = ("apple", "banana", "cherry")
g = range(6)
h = {"name" : "John", "age" : 36}
i = {"apple", "banana", "cherry"}
j = frozenset({"apple", "banana", "cherry"})
k = True
l = b"Hello"
m = bytearray(5)
n = memoryview(bytes(5))
o = 1024 * 1024 * 1024 * 1204 * 1024 * 1204
p = None
# **********************************************************************************************************
# endregion

# region Handwritten functions and procedures
# **********************************************************************************************************
'''
///*********************************************************************************************************
///* Handwritten functions and procedures
///*********************************************************************************************************
'''

'''
/// Divider() function to create a separator line with a given character.
/// Parameters:
/// bolLF: line feed, default: False
/// chrTL: separator, default: '*'
/// intMax: number of character repetitions, default: 70
/// ADD by engineer B.Pourtavakoli on 1402/11/20
/// UPDATE by engineer B.Pourtavakoli on 1402/11/22
'''
def Divider(bolLF = False, chrTL = '*', intMax = 70):
     print(*intMax*(chrTL,), sep=' ')
     #print(chrTL * intMax, sep='_')

     if (bolLF):
          print("")
# **********************************************************************************************************
# endregion

# region Standard functions and procedures
# **********************************************************************************************************
'''
///*********************************************************************************************************
///* Standard functions and procedures
///*********************************************************************************************************
'''

def changer():
    global x
    x = "Hilda"
    #print(x)

def DataType():
    print(f"x Value: {x} - Type: {type(x)}")
    print(f"a Value: {a} - Type: {type(a)}")
    print(f"b Value: {b} - Type: {type(b)}")
    print(f"c Value: {c} - Type: {type(c)}")
    print(f"d Value: {d} - Type: {type(d)}")
    print(f"e Value: {e} - Type: {type(e)}")
    print(f"f Value: {f} - Type: {type(f)}")
    print(f"g Value: {g} - Type: {type(g)}")
    print("h Value: {h} - Type: {type(h)}")
    print("i Value: {i} - Type: {type(i)}")
    print("j Value: {j} - Type: {type(j)}")
    print("k Value: {k} - Type: {type(k)}")
    print("l Value: {l} - Type: {type(l)}")
    print(f"m Value: {m} - Type: {type(m)}")
    print(f"n Value: {n} - Type: {type(n)}")
    print(f"o Value: {o} - Type: {type(o)}")
    print(f"p Value: {p} - Type: {type(p)}")

###testing  A= ["2,4,6,12,24,35,125,135","4,12,35,125"]
###testing  A=["1,2,3,4","1,4,5,7"]
def FindIntersection(stArr):
    #print(stArr)
    st = ''
    for intI in stArr[0].split(','):
        for intJ in stArr[2].split(','):
            if (i==j):
                st = st + intJ + ','
                break
                            
    stArr = st[0:-1]
    # code goes here
    return stArr

def Prints_Test():
    print(x, a, b)
    print(x, a, sep='-')
    print(x, a, end=' ')
    print()
    print("Loading...", flush=True)
    print(x, a, b, sep=", ")
    print("Processing", end="...")
    print("Done!")

    for intI in range(10):
        print(intI + 1, end=" ", flush=True)
        time.sleep(0.2)
    print("")

    print("Done!")
    print()

def LoadingBar():
    for intI in tqdm(range(150)): #, force=True):
        time.sleep(0.01)
    print()
    return

    with alive_bar(120000) as bar:
        bar(60000, skipped=True)
        for i in range(60000, 120000):
            # process item
            bar()
    print()
    
    for total in 500, 700, 400, 0:
        with alive_bar(total) as bar:
            for _ in range(500):
                time.sleep(.001)
                bar()
    print()

    with alive_bar(120000) as bar:
        bar(60000, skipped=True)
        for i in range(60000, 120000):
            bar()
    print()

    #showtime()

def Ensure_Trailing_Backslash(path):
    path = str(path)
    if (not path.endswith(os.sep)):
        return path + os.sep
    return path

# License Plate Recognition - lpr
def LPR():
    current_directory = os.getcwd()
    #current_directory = Path().cwd()
    
    #current_directory = os.path.abspath(__file__).resolve()
    #current_directory = Path(__file__).resolve()
    
    #current_directory = os.path.dirname(os.path.abspath(__file__))
    current_directory = os.path.dirname(Path(__file__).resolve())
    #print(current_directory)

    strFilename = Ensure_Trailing_Backslash(current_directory) + 'Plate2.jpg'
    print(strFilename)
    
    if (not os.path.exists(strFilename)):
        print("Directory not found.")
    
    ##pyinstaller --onefile --add-binary "C:\Program Files\Tesseract-OCR\tesseract.exe;./tesseract" myscript.py
    #pytesseract.pytesseract.tesseract_cmd = os.path.join(os.getcwd(), 'tesseract', 'tesseract.exe')
    pytesseract.pytesseract.tesseract_cmd = os.path.join(os.getcwd(), 'tesseract', 'tesseract.exe')

    #image = cv2.imread(strFilename)
    #text = pytesseract.image_to_string(image)
    #print("License Plate:", text)

    image = Image.open(strFilename)
    text = pytesseract.image_to_string(image)
    print("Detected text:", text)

lst = list()

def Python_TelChat_1(arg: list = lst):
    arg.append(0)
    return arg

'''
/// WinMain() contains main statements and calling functions
/// ADD by engineer B.Pourtavakoli on 1402/11/26
'''
def WinMain():
    intStartTime = time.time()

    print("Wow, Welcome")
    
    intEndTime = time.time()
    intElapsedTime = intEndTime - intStartTime
    print("Elapsed Time: %s ms" % round(intElapsedTime, 3))
    
    Divider()
    #changer()
    #print(x)
    #DataType()
    #Prints_Test()

    LoadingBar()
    
    #LPR()
    print(lst)
    print(Python_TelChat_1())
    print(Python_TelChat_1())
    print(Python_TelChat_1())
    print(Python_TelChat_1())
    print(Python_TelChat_1())
    print(lst)

    # keep this function call here
    #print(FindIntersection(str(input())[2:-2].split('\"')))

    Divider()
    
    #print("Press Enter key to exit...", end='')
    #input()
# **********************************************************************************************************
# endregion
 
# region Main program
# **********************************************************************************************************
'''
///*********************************************************************************************************
///* Main program
///*********************************************************************************************************
'''
'''
/// Main program, contains main statements and calling functions
/// ADD by engineer B.Pourtavakoli on 1402/11/26
'''
if (__name__ == "__main__"):
    WinMain()
# **********************************************************************************************************
# endregion
