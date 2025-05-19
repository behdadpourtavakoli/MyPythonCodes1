# region Copyright
# **********************************************************************************************************
'''
///*-=============================================================================================-*
/// File name             : CodeYad1.py
/// Version               : 1.0.0.0
/// Start                 : 2024-09-20 (1403/06/30)
/// Last update           : 2024-11-25 (1403/09/05)
/// Autor                 : Engineer Behdad Pourtavakoli
/// Trademark             : Behdad Software Developers Group™
/// ----------------------------------------------------------------------------------------------
/// Copyright © 1380-1403 (2001-2024) by B.S.D Group™
/// All rights reserved.
/// ----------------------------------------------------------------------------------------------
///
/// Description: Review and revise the Python learning by CodeYad based on Video
///
/// ----------------------------------------------------------------------------------------------
/// The developer's word: Do not forget the engineer Behdad Pourtavakoli.
///-=============================================================================================-*
'''
# **********************************************************************************************************
# endregion

# region Important header files
# **********************************************************************************************************
'''
///*********************************************************************************************************
///* Important header files
///*********************************************************************************************************
'''
import os, base64, lorem, sys, math, hashlib, psutil, pprint, platform, random, datetime, pytz, jdatetime, json, re, cowsay
import asyncio, time, pathlib
from tkinter import *
from datetime import datetime, timedelta
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


import numpy as np


# **********************************************************************************************************
# endregion

# region Constants and Variables
# **********************************************************************************************************
'''
///*********************************************************************************************************
///* Constants and Variables
///*********************************************************************************************************
'''

NEWLINE = "\n"

# **********************************************************************************************************
# endregion

# region Handwritten functions and procedures
# **********************************************************************************************************
'''
///*********************************************************************************************************
///* Handwritten functions and procedures
///*********************************************************************************************************
'''

def Button_Click():
    print("Download in progress...")

# region Other classes declaration
# **********************************************************************************************************

'''
/// Other classes declaration
/// ADDED by engineer B.Pourtavakoli on 1403/06/30
'''

def function_test():
    pass

def def1():
    print(str.__module__)

class clsClassTest1:
    def function1():
        print(str.__module__)

class clsClassTest2:
    def function2():
        print(str.__module__)

'''
/// # AES Encryptor Level 1: Simple example
/// # a simple string is used for encryption. The encryption key must also be a 16, 24, or 32-byte 
///   string (for AES-128, AES-192, or AES-256).
/// ADDED by engineer B.Pourtavakoli on 1403/07/07
'''
def AES_Encrypt_L1(plain_text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    encrypted_bytes = cipher.encrypt(pad(plain_text.encode('utf-8'), AES.block_size))
    return (base64.b64encode(cipher.iv + encrypted_bytes).decode('utf-8'))

'''
/// # AES Decryptor Level 1: Simple example
/// ADDED by engineer B.Pourtavakoli on 1403/07/07
'''
def AES_Decrypt_L1(encrypted_text, key):
    encrypted_data = base64.b64decode(encrypted_text)
    # IV is the first 16 bytes
    iv = encrypted_data[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_bytes = unpad(cipher.decrypt(encrypted_data[16:]), AES.block_size)
    return (decrypted_bytes.decode('utf-8'))

'''
/// # AES Encryptor Level 2: Encryption with key management and IV
/// # This level explains how to manage key and IV for added security. The use of Initialization 
///   Vector (IV) is very important to ensure the randomness of the encryption output.
/// ADDED by engineer B.Pourtavakoli on 1403/07/07
'''
def AES_Encrypt_L2(plain_text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    encrypted_bytes = cipher.encrypt(pad(plain_text.encode('utf-8'), AES.block_size))
    return (base64.b64encode(iv + encrypted_bytes).decode('utf-8'))

'''
/// # AES Decryptor Level 2: Simple example
/// ADDED by engineer B.Pourtavakoli on 1403/07/07
'''
def AES_Decrypt_L2(encrypted_text, key):
    encrypted_data = base64.b64decode(encrypted_text)
    # IV is the first 16 bytes
    iv = encrypted_data[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_bytes = unpad(cipher.decrypt(encrypted_data[16:]), AES.block_size)
    return (decrypted_bytes.decode('utf-8'))

'''
/// # AES Encryptor Level 3: encryption and key storage and IV
/// # In this example, the encryption key is stored securely and the IV is also sent along with 
///   the ciphertext. This method is suitable for storing sensitive data.
/// ADDED by engineer B.Pourtavakoli on 1403/07/07
'''
def AES_Encrypt_L3(plain_text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    encrypted_bytes = cipher.encrypt(pad(plain_text.encode('utf-8'), AES.block_size))
    return (base64.b64encode(iv + encrypted_bytes).decode('utf-8'))

'''
/// # Save_Encrypted_Data for Level 3: Store encrypted data and key
/// ADDED by engineer B.Pourtavakoli on 1403/07/07
'''
def Save_Encrypted_Data(encrypted_data, key):
    with open('encrypted_data.txt', 'w') as f:
        f.write(encrypted_data)
    with open('encryption_key.txt', 'wb') as f:
        f.write(key)

'''
/// # AES Decryptor Level 3: Simple example
/// ADDED by engineer B.Pourtavakoli on 1403/07/07
'''
def AES_Decrypt_L3(encrypted_text, key):
    encrypted_data = base64.b64decode(encrypted_text)
    # IV is the first 16 bytes
    iv = encrypted_data[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_bytes = unpad(cipher.decrypt(encrypted_data[16:]), AES.block_size)
    return (decrypted_bytes.decode('utf-8'))

'''
/// # AES Encryptor Level 4: encryption and decryption
/// # At this level, in addition to encryption, the decryption function is also implemented so 
///   that we can return the encrypted text back to the original state. This example will help 
///   you get a better understanding of the encryption and decryption process.
/// ADDED by engineer B.Pourtavakoli on 1403/07/07
'''
def AES_Encrypt_L4(plain_text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    encrypted_bytes = cipher.encrypt(pad(plain_text.encode('utf-8'), AES.block_size))
    return (base64.b64encode(iv + encrypted_bytes).decode('utf-8'))

'''
/// # AES Decryptor Level 4: Simple example
/// ADDED by engineer B.Pourtavakoli on 1403/07/07
'''
def AES_Decrypt_L4(encrypted_text, key):
    encrypted_data = base64.b64decode(encrypted_text)
    # IV is the first 16 bytes
    iv = encrypted_data[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_bytes = unpad(cipher.decrypt(encrypted_data[16:]), AES.block_size)
    return (decrypted_bytes.decode('utf-8'))
    
'''
/// # AES Encryptor Level 5: Generate a 32-byte key for AES-256
/// # At this level, random and unique keys are generated for each cryptographic session. This greatly increases security.
/// ADDED by engineer B.Pourtavakoli on 1403/07/07
'''
def Generate_Key():
    return (os.urandom(32))

'''
/// # Level 5: Encryption using random keys (more security)
/// ADDED by engineer B.Pourtavakoli on 1403/07/07
'''
def AES_Encrypt_L5(plain_text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    encrypted_bytes = cipher.encrypt(pad(plain_text.encode('utf-8'), AES.block_size))
    return (base64.b64encode(iv + encrypted_bytes).decode('utf-8'))

'''
/// # AES Decryptor Level 5: Simple example
/// ADDED by engineer B.Pourtavakoli on 1403/07/07
'''
def AES_Decrypt_L5(encrypted_text, key):
    encrypted_data = base64.b64decode(encrypted_text)
    # IV is the first 16 bytes
    iv = encrypted_data[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_bytes = unpad(cipher.decrypt(encrypted_data[16:]), AES.block_size)
    return (decrypted_bytes.decode('utf-8'))

def Encrypted_Formated(encrypted_text, block_size=5):
    formatted_text = ' '.join([encrypted_text[i:i+block_size] for i in range(0, len(encrypted_text), block_size)])
    formatted_text = encrypted_text
    return (formatted_text)


def logistic_map(x, r):
    return (r * x * (1 - x))

def chaotic_key_generator(length, x0=0.5, r=3.9):
    key = []
    x = x0
    for i in range(length):
        x = logistic_map(x, r)
        key.append(int(x > 0.5))
    return (key)

def xor_encrypt_decrypt(data, key):
    return (''.join([chr(ord(c) ^ k) for c, k in zip(data, key)]))

def Hash_MD5(strInput, bolLower = False):
    md5_hash = hashlib.md5(strInput.encode())
    strOutput = md5_hash.hexdigest().upper()
    if (bolLower == True):
        strOutput = strOutput.lower()
    return (strOutput)

def Hash_SHA1(strInput, bolLower = False):
    sha1_hash = hashlib.sha1(strInput.encode())
    strOutput = sha1_hash.hexdigest().upper()
    if (bolLower == True):
        strOutput = strOutput.lower()
    return (strOutput)

# **********************************************************************************************************
# endregion

# region CodeYad1()--base class
# **********************************************************************************************************
'''
/// CodeYad1()--base class
/// ADDED by engineer B.Pourtavakoli on 1403/07/06
'''
class CodeYad1:
    '''
    /// ClearScreen()--function to clear output screen
    /// ADDED by engineer B.Pourtavakoli on 1403/06/31
    '''
    def ClearScreen(self):
        # For Windows
        if (os.name == "nt"):
            _ = os.system("cls")
            #_ = subprocess.call("cls")

        # For macOS and Linux
        elif (os.name == "posix"):
            _ = os.system("clear")
            #_ = subprocess.call("clear")

    '''
    /// PyClassCaller()--function to test some Python methods
    /// ADDED by engineer B.Pourtavakoli on 1403/07/06
    '''
    def PyClassCaller(self):
        print("__name__: ", __name__)
        ## print("__builtins__: ", __builtins__)
        ## print("__cached__: ", __cached__)
        print("__doc__: ", __doc__)
        print("__file__: ", __file__)
        print("__import__: ", __import__)
        print("__package__: ", __package__)
        ## print("__loader__: ", __loader__)
        ## print("__spec__: ", __spec__)

        # print("__annotations__: ", __annotations__)
        # print("__dict__: ", __dict__)
        # print("__path__: ", os.__path__)

        print(str.__module__)
        def1()
        clsClassTest1.function1()
        clsClassTest2.function2()

    '''
    /// CodeYad1(self)--function to review the Python language by CodeYad.com
    /// Contains CodeYad lessons by video: 1 to 13
    /// ADDED by engineer B.Pourtavakoli on 1403/07/06
    '''
    def CodeYad1(self):
        a = 12
        b = 5
        c = a / b
        print(f"Value: {c} - Type: {type(c).__name__}")
        c = a // b
        print(f"Value: {c} - Type: {type(c).__name__}")
        c = a % b
        print(f"Value: {c} - Type: {type(c).__name__}")

        a = 2.4
        b = 5
        c = a * b
        print(f"Value: {c} - Type: {type(c).__name__}")
        
        s = "Mein name ist \"Behdad\""
        S = 'Mein name ist \'Behdad\''
        print(s)
        print(S)

        txt = f"The price is {20 * 59} dollars"
        print(txt)

    '''
    /// CodeYad2(self)--function to review the Python language by CodeYad.com
    /// Contains CodeYad lessons by video: 14
    /// ADDED by engineer B.Pourtavakoli on 1403/07/06
    '''
    def CodeYad2(self):
        strTemp = "Behdad Pourtavakoli"
        print(f"len(): {len(strTemp)}")
        print(f"count(): {strTemp.count("a")}")

        print(f"capitalize(): {strTemp.capitalize()}")
        print(f"casefold(): {strTemp.casefold()}")
        print(f"encode(): {strTemp.encode()}")
        print(f"expandtabs(): {strTemp.expandtabs()}")
        print(f"format(): {strTemp.format()}")

        print(f"lstrip(): {strTemp.lstrip()}")
        print(f"rsplit(): {strTemp.rsplit()}")
        print(f"rstrip(): {strTemp.rstrip()}")
        print(f"split(): {strTemp.split()}")
        print(f"splitlines(): {strTemp.splitlines()}")
        print(f"swapcase(): {strTemp.swapcase()}")

        print(f"strip(): {strTemp.strip()}")
        print(f"title(): {strTemp.title()}")
        print(f"lower(): {strTemp.lower()}")
        print(f"upper(): {strTemp.upper()}")

        #print(strTemp.center())
        #print(strTemp.endswith())
        #print(strTemp.find())
        #print(strTemp.format_map())
        #print(strTemp.index())
        #print(strTemp.join())
        #print(strTemp.ljust())
        #print(strTemp.maketrans())
        #print(strTemp.partition())
        #print(strTemp.replace())
        #print(strTemp.rfind())
        #print(strTemp.rindex())
        #print(strTemp.rjust())
        #print(strTemp.rpartition())
        #print(strTemp.startswith())
        #print(strTemp.translate())
        #print(strTemp.zfill())

        ##print(f"{strTemp.isalnum()}")
        ##print(f"{strTemp.isalpha()}")
        ##print(f"{strTemp.isascii()}")
        ##print(f"{strTemp.isdecimal()}")
        ##print(f"{strTemp.isdigit()}")
        ##print(f"{strTemp.isidentifier()}")
        ##print(f"{strTemp.islower()}")
        ##print(f"{strTemp.isnumeric()}")
        ##print(f"{strTemp.isprintable()}")
        ##print(f"{strTemp.isspace()}")
        ##print(f"{strTemp.istitle()}")
        ##print(f"{strTemp.isupper()}")

    '''
    /// CodeYad3(self)--function to review the Python language by CodeYad.com
    /// Contains CodeYad lessons by video: 15
    /// ADDED by engineer B.Pourtavakoli on 1403/07/06
    '''
    def CodeYad3(self):
        strInput = input("Enter a number (between 1 .. 9): ")
        intInput = intOutput = int(strInput)
        #intOutput = (((((((intInput * 2) + 8) + intInput) - 2) / 3) - intInput) * 4)
        intOutput *= 2
        intOutput += 8
        intOutput += intInput
        intOutput -= 2
        intOutput /= 3
        intOutput -= intInput
        intOutput *= 4
        intOutput = int(intOutput)
        print(f"Your answer is {intOutput}")

    '''
    /// CodeYad4(self)--function to review the Python language by CodeYad.com
    /// Contains CodeYad lessons by video: 16 to 24
    /// ADDED by engineer B.Pourtavakoli on 1403/07/06
    '''
    def CodeYad4(self):
        lstListTest = []
        lstListTest.append("Wow")
        lstListTest.append("007")
        lstListTest.append("MI6")
        lstListTest.append("IMF")
        lstListTest.append("CIA")
        lstListTest.append("NSA")
        lstListTest.append("KGB")
        lstListTest.append("Spy")
        print(f"1) List: {lstListTest} - List count: {len(lstListTest)}")

        lstListTest.insert(0, "Behdad")
        print(f"2) List: {lstListTest} - List count: {len(lstListTest)}")

        intIndex = len(lstListTest) - 1
        lstListTest.remove(lstListTest[intIndex])
        lstListTest.pop()
        print(f"3) List: {lstListTest} - List count: {len(lstListTest)}")

        del(lstListTest[0])
        print(f"4) List: {lstListTest} - List count: {len(lstListTest)}")

        lstListTest.insert(len(lstListTest), "Behdad")
        print(f"5) List: {lstListTest} - List count: {len(lstListTest)}")

        lstNewList = ["000", "002", "008", "007"]
        # lstListTest.extend(lstNewList)
        # print(f"6) List: {lstListTest} - List count: {len(lstListTest)}")

        lstNewList.extend(lstListTest)
        lstListTest = lstNewList
        print(f"7-1) List: {lstListTest} - List count: {len(lstListTest)}")

        lstListTest = list.copy(lstNewList)
        print(f"7-2) List: {lstListTest} - List count: {len(lstListTest)}")

        print(type(lstListTest))
        print(type(lstListTest).__base__)
        print(type(lstListTest))
        print(type(lstListTest).__contains__)
        print(type(lstListTest).__init__)
        print(type(lstListTest).__name__)
        # print(f"Type 1: {type(lstListTest)} - Type 2: {type(lstListTest).__name__}")

    '''
    /// CodeYad5(self)--function to review the Python language by CodeYad.com
    /// Contains CodeYad lessons by video: 24
    /// ADDED by engineer B.Pourtavakoli on 1403/07/06
    '''
    def CodeYad5(self):

        fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
        print(fruits[2:5])
        
        tplTuple = ('Behdad')
        print(f"1) Tuple: {tplTuple} - Tuple count: {len(tplTuple)} - Tuple type: {type(tplTuple)}")

        tplTuple = tuple(tplTuple)
        print(f"2) Tuple: {tplTuple} - Tuple count: {len(tplTuple)} - Tuple type: {type(tplTuple)}")

        tplTuple = ('Behdad',)
        print(*tplTuple)
        print(tplTuple[0])
        print(f"3) Tuple: {tplTuple} - Tuple count: {len(tplTuple)} - Tuple type: {type(tplTuple)}")
        
        tplTuple = ('Behdad', 'Hilda', 'Hila')
        print(f"4) Tuple: {tplTuple}")
        
        lstTuple = list(tplTuple)
        lstTuple[0], lstTuple[1] = lstTuple[1], lstTuple[0]
        lstTuple.append('Hiva')
        tplTuple = tuple(lstTuple)
        print(f"5) Fix Tuple: {tplTuple}")
        
        try:
            print(f"6) Tuple count: {tplTuple.count('H')} - Tuple index: {tplTuple.index('H')}")
        except ValueError:
            print(f"'Hiva' is not in tuple")

    '''
    /// CodeYad6(self)--function to review the Python language by CodeYad.com
    /// Contains CodeYad lessons by video: 25 .. 27
    /// ADDED by engineer B.Pourtavakoli on 1403/07/06
    '''
    def CodeYad6(self):
        setSetList = {'Blueberry', 'Kiwi', 'Apple', 'Banana', 'Kiwi', 'Tomato', 'Kiwi'}
        print(setSetList)
        
        setSetList2 = {'Strawberry', 'Carrot', 'Onion'}
        setSetList.update(setSetList2)
        print(setSetList)
        
        lstList = {'Good', 'Normal', 'Wow'}
        setSetList.update(lstList)
        print(setSetList)
        
    '''
    /// CodeYad7(self)--function to review the Python language by CodeYad.com
    /// Contains CodeYad lessons by video: 28..32
    /// ADDED by engineer B.Pourtavakoli on 1403/07/12
    '''
    def CodeYad7(self):
        
        lstList = [1]
        tupTuple = (2)
        dicDictionary = {3}
        
        dicDict = { "Name": "Behdad", "Family": "Pourtavakoli", "Age": "43", "Job": "Developer" }
        print(f"Dictionary: {dicDict} - Type: {type(dicDict)} - Length: {len(dicDict)}")
        print(f"Dictionary Items 1: {dicDict["Name"]} {dicDict["Family"]}")
        print(f"Dictionary Items 2: {dicDict.get("Age")} {dicDict.get("Job")}")
        print(f"Dictionary Keys: {dicDict.keys()}")
        print(f"Dictionary Keys: {dicDict.values()}")
        print(f"Dictionary Keys: {dicDict.items()}")
        
        bolResult = "Name" in dicDict
        print(f"Result: {bolResult}")

        dicDict["Age"] = 40
        print(f"Dictionary: {dicDict}")

        dicDict.update({"age": 43})
        print(f"Dictionary: {dicDict}")
        
        dicDict.pop("age")
        print(f"Dictionary: {dicDict}")
        
        dicDict.popitem()
        print(f"Dictionary: {dicDict}")

        del(dicDict["Age"])
        print(f"Dictionary: {dicDict}")
        
        dicNastedDict = { "Dict1": { "Name": "", "Family": "", "Age": "", "Job": "" },
                          "Dict2": { "Name": "", "Family": "", "Age": "", "Job": "" },
                          "Dict3": { "Name": "", "Family": "", "Age": "", "Job": "" },
                          "Dict4": { "Name": "", "Family": "", "Age": "", "Job": "" } }
        # print(f"Dictionary: {dicNastedDict} - Type: {type(dicNastedDict)} - Length: {len(dicNastedDict)}")
        print(f"Dictionary: {dicNastedDict.items()}")

        dicDict1 = { "Name": "", "Family": "", "Age": "", "Job": "" }
        dicDict2 = { "Name": "", "Family": "", "Age": "", "Job": "" }
        dicDict3 = { "Name": "", "Family": "", "Age": "", "Job": "" }
        dicDict4 = { "Name": "", "Family": "", "Age": "", "Job": "" }
        dicNastedDict = { "Dict1": dicDict1,
                          "Dict2": dicDict2,
                          "Dict3": dicDict3,
                          "Dict4": dicDict4 }
        # print(f"Dictionary: {dicNastedDict} - Type: {type(dicNastedDict)} - Length: {len(dicNastedDict)}")
        print(f"Dictionary: {dicNastedDict.items()}")

    '''
    /// has_sufficient_memory(self)--function to ...
    /// ADDED by engineer B.Pourtavakoli on 1403/08/08
    '''
    def has_sufficient_memory():
        memory_info = psutil.virtual_memory()
        available_memory_gb = memory_info.available / (1024 ** 3)
        print(f"Available memory: {available_memory_gb:.2f} GB")
        
        # Check the minimum memory required, 2 GB by default
        return (available_memory_gb > 2)

    '''
    /// CodeYad8(self)--function to review the Python language by CodeYad.com
    /// Contains: Try and test big data bumber (8000 digits) :D) :)) :-D :D XD
    /// ADDED by engineer B.Pourtavakoli on 1403/07/15
    '''
    def CodeYad8(self):
        '''
        مثالی از کامنت نویسی برای توابع.
        
        این تابع دو عدد را ضرب می‌کند.
        
        :param a: عدد اول
        :param b: عدد دوم
        :return: حاصل ضرب دو عدد
        '''
        dblDouble = 12345678901234567890123456789012345678901234567890123456789012345678901234567890
        dblDouble *= dblDouble
        print(f"Value: {dblDouble}\r\nType: {type(dblDouble)}-Length: {len(str(dblDouble))}")
        input("Press the Enter key to continue...")
        # input("Drücken Sie die Eingabetaste, um fortzufahren ...")
        
        print(f"the limit (4300 digits) for integer string")
        dblDouble = 10 ** 4299
        print(f"Value: {dblDouble}\r\nType: {type(dblDouble)}-Length: {len(str(dblDouble))}\r\n")
        input("Press the Enter key to continue...")
        
        # For example, increasing the limit to 10,000 digits
        sys.set_int_max_str_digits(8001)

        # A number with 5001 digits
        dblDouble = 10 ** 8000
        # Convert to a string and count its length
        print(f"Value: {dblDouble}\r\nType: {type(dblDouble)}-Length: {len(str(dblDouble))}\r\n")
        input("Press the Enter key to continue...")

        n = 2000
        dblDouble = math.factorial(n)
        print(f"Value: {dblDouble}\r\nType: {type(dblDouble)}-Length: {len(str(dblDouble))}\r\n")
        input("Press the Enter key to continue...")

    '''
    /// CodeYad9(self)--function to review the Python language by CodeYad.com
    /// Contains: 
    /// ADDED by engineer B.Pourtavakoli on 1403/07/15
    '''
    def CodeYad9(self):
        plain_text = "Hello, Chaos Theory!"

        key_length = len(plain_text)
        key = chaotic_key_generator(key_length)

        encrypted = xor_encrypt_decrypt(plain_text, key)
        print(f"Encrypted text: {encrypted}")

        decrypted = xor_encrypt_decrypt(encrypted, key)
        print(f"Decrypted text: {decrypted}")

    '''
    /// CodeYad10(self)--function to review the Python language by CodeYad.com
    /// Contains CodeYad lessons by video: 32..45 - 46..50
    /// ADDED by engineer B.Pourtavakoli on 1403/07/15-1403/07/20
    '''
    def CodeYad10(self):
        # while
        # for { continue, break }
        
        names = ["Behdad", "Hilda", "Hila", "Hiva", "Engineer", "Teacher", "Student", "Kid"]
        b = []
        
        for name in names:
            if (name[0] == "H"):
                # print(name)
                b.append(name)
        print(b)
        
        return
        
        a = ["Behdad", "Hilda", "Hila", "Hiva"]
        b = ["Engineer", "Teacher", "Student", "Kid"]
        
        for i in a:
            for j in b:
                print((i, j), end='\t')
            print()
                
        for i in range(1, 10, 2):
            print(i, end=', ')
        print()
        for i in range(2, 11, 2):
            print(i, end=', ')
        print()
        
        for i in range(1, 8):
            for j in range(1, 8):
                print((i * j), end='\t')
            print()
        print()


    '''
    /// CodeYad11(self)--function to review the Python language by CodeYad.com
    /// Contains CodeYad lessons by video: 51
    /// ADDED by engineer B.Pourtavakoli on 1403/07/20
    '''
    def CodeYad11(self):
        name = input("Enter the name: ").lower().strip().replace(' ', '')
        
        for i in name:
            print(i, end='\t')
        print()
        
        print(f"Length:  {len(name)}")
        
        b = []
        for i in name:
            if (i not in b):
                print(f"your name has {name.count(i)} {i}")
                b.append(i)
        
        pass
    
    '''
    /// CodeYad12(self)--function to review the Python language by CodeYad.com
    /// Contains CodeYad lessons by video: 52
    /// Introduce: pynative.com website look like quera.ir
    /// ADDED by engineer B.Pourtavakoli on 1403/07/20
    '''
    def CodeYad12(self):
        # displays first 10 natural numbers
        n = 0
        while (n <= 10):
            print(n, end='\t')
            n += 1
        print()

        # displays top 5 triangle
        for i in range(1, 7):
            for j in range(1, i):
                print(j, end='\t')
            print()

    '''
    /// Fibonacci(self, n)--function to review the Python language by CodeYad.com
    /// Fibonacci sequence
    /// ADDED by engineer B.Pourtavakoli on 1403/07/21
    '''
    def Fibonacci(self, n, memo={}, bolPrnFlag = False):
        '''
        Fibonacci sequence function(self, n, memo={}, bolPrnFlag = False)

        :param n: An integer representing the position in the Fibonacci sequence.
        :param memo: A dictionary used to store previously computed Fibonacci numbers (used for memoization).
        :param bolPrnFlag: A boolean flag to control whether to print each step of the computation or not.
        :return: The Fibonacci number corresponding to the input n.
        '''
        #############################################################################################################
        # Old version of Fibonacci sequence function
        #############################################################################################################
        # if (n <= 1):
        #     return (n)
        # return (self.Fibonacci(n-1) + self.Fibonacci(n - 2))
        
        # memo = [0] * (n + 1)
        # memo[0], memo[1] = 0, 1        
        # for i in range(2, n + 1):
        #     memo[i] = memo[i-1] + memo[i-2]
        # return (memo[n])
        
        if (bolPrnFlag):
            print(f"Fibonacci({n}) called")
        if (n in memo):
            if (bolPrnFlag):
                print(f"Fibonacci({n}) from memory: {memo[n]}")
            return (memo[n])
        
        if (n <= 1):
            return (n)
        
        memo[n] = self.Fibonacci(n-1, memo) + self.Fibonacci(n-2, memo)
        if (bolPrnFlag):
            print(f"Fibonacci({n}) Calculated: {memo[n]}")
        return (memo[n])

    '''
    /// PwdValidation(self, strPwd)--function to to check a password validation
    /// Contains CodeYad lessons by video: 56
    /// ADDED by engineer B.Pourtavakoli on 1403/08/07
    '''
    def PwdValidation(self, strPwd):
        if (len(strPwd) < 8):
            print("Your password must be at least 8 character.")
        elif (strPwd.isnumeric()):
            print("Your password must be at least one letter.")
        elif (strPwd.isalpha()):
            print("Your password must be at least one number.")
        else:
            print("Yest, your password is correct.")
        print()

    '''
    /// CodeYad13(self)--function to review the Python language by CodeYad.com
    /// Contains CodeYad lessons by video: 53..56
    /// ADDED by engineer B.Pourtavakoli on 1403/07/20
    /// Review by engineer B.Pourtavakoli on 1403/08/06
    /// ADD/Review by engineer B.Pourtavakoli on 1403/08/07
    '''
    def CodeYad13(self):
        strOldPwd = ""
        while (True):
            strPwd = input("Please enter your password: ")
            if (strPwd.lower() == "quit"):
                if (len(strOldPwd) > 0):
                    strPwd = strOldPwd
                else:
                    strPwd = "Pwd"
                break
            self.PwdValidation(strPwd)
            strOldPwd = strPwd
        
        print(f"\r\nPassword: {strPwd}, IsNumeric: {strPwd.isnumeric()}, IsAlpha: {strPwd.isalpha()}")
        print(f"IsAscii: {strPwd.isascii()}, IsDigit: {strPwd.isdigit()}")
        
        strPassword1 = "password"
        print(f"\r\nMD5: {Hash_MD5(strPassword1)}, SHA1: {Hash_SHA1(strPassword1)}")
        print(f"SHA1 & MD5: {Hash_SHA1(Hash_MD5(strPassword1))}, MD5 & SHA1: {Hash_MD5(Hash_SHA1(strPassword1))}")

    '''
    /// NoLimitFunc(self, *args, **kwargs)--function to show args and keword args
    /// Contains CodeYad lessons by video: 57..60
    /// ADDED by engineer B.Pourtavakoli on 1403/08/07
    '''
    def NoLimitFunc(self, *args, **kwargs):
        print(f"args: {args} - Type: {type(args).__name__}")
        print(f"kwargs: {kwargs} - Type: {type(kwargs).__name__}")

    '''
    /// CharRecognizer(self, strText)--function to recognize each character of user text
    /// Contains CodeYad lessons by video: 63
    /// ADDED by engineer B.Pourtavakoli on 1403/08/08
    '''
    def CharRecognizer(self, strText):
        intUpper = intLower = intDigit = intAscii = intSpace = intAlpha = intDecimal = intNumeric = 0
        for intI in strText:
            if (intI.isupper()):
                intUpper += 1
            elif (intI.islower()):
                intLower += 1
            elif (intI.isdigit()):
                intDigit += 1
            elif (intI.isascii()):
                intAscii += 1
            elif (intI.isspace()):
                intSpace += 1
            elif (intI.isalpha()):
                intAlpha += 1
            elif (intI.isdecimal()):
                intDecimal += 1
            elif (intI.isnumeric()):
                intNumeric += 1

        print(f"Text: {strText} - Length: {len(strText)}")
        print(f"Number of Upper case character is: {intUpper}")
        print(f"Number of Lower case character is: {intLower}")

        print(f"Number of Digit character is     : {intDigit}")
        print(f"Number of Ascii character is     : {intAscii}")

        print(f"Number of Space character is     : {intSpace}")

        print(f"Number of Alpha character is     : {intAlpha}")
        print(f"Number of Decimal character is   : {intDecimal}")
        print(f"Number of Numeric character is   : {intNumeric}")

    '''
    /// CodeYad14(self)--function to review the Python language by CodeYad.com
    /// Contains CodeYad lessons by video: 57..63,64..67
    /// ADDED by engineer B.Pourtavakoli on 1403/08/07
    '''
    def CodeYad14(self):
        self.NoLimitFunc("behdad", "james", SecretCode="002", Organazation="MI6")
        print()
        self.CharRecognizer("The Name is Bond, James Bond, 007, 3.14")

    '''
    /// newfunc1(self)--function to prepare a normal nested function
    /// Contains CodeYad lessons by video: 68
    /// ADDED by engineer B.Pourtavakoli on 1403/08/11
    '''
    def newfunc1(self, n):
        def newrefunc(a):
            return (a * n)
        return (newrefunc)

    '''
    /// newfunc2(self)--function to prepare a lambda function for calculation
    /// Contains CodeYad lessons by video: 68
    /// ADDED by engineer B.Pourtavakoli on 1403/08/11
    '''
    def newfunc2(self, n):
        return (lambda a : a * n)

    '''
    /// CodeYad15(self)--function to review the Python language by CodeYad.com
    /// Contains CodeYad lessons by video: 68
    /// ADDED by engineer B.Pourtavakoli on 1403/08/11
    '''
    def CodeYad15(self):
        abcs = self.newfunc1(20)
        print(abcs(50))

        abcs = self.newfunc2(20)
        print(abcs(50))

    '''
    /// CodeYad16(self)--function to review the Python language by CodeYad.com
    /// Using map() object by lambda technique
    /// Contains CodeYad lessons by video: 69
    /// ADDED by engineer B.Pourtavakoli on 1403/08/11
    '''
    def CodeYad16(self):
        mylist = [1, 3, 5, 7, 9]
        mylist2 = [2, 4, 6, 8, 10]
        
        x = list(map(lambda a, b : a * b, mylist, mylist2))
        print(x)

    '''
    /// CodeYad17(self)--function to review the Python language by CodeYad.com
    /// Class, object oriented
    /// Contains CodeYad lessons by video: 70..79
    /// ADDED by engineer B.Pourtavakoli on 1403/08/11
    '''
    def CodeYad17(self):
        print(self.__class__)

    '''
    /// CodeYad18(self)--function to review the Python language by CodeYad.com
    /// Review Class, object oriented
    /// Contains CodeYad lessons by video: 74..79 and W3Schools.com
    /// ADDED by engineer B.Pourtavakoli on 1403/08/20
    '''
    def CodeYad18(self):
        lstDatabase = []
       
        # car1 = clsCar("Toyota Corolla", 2022, "White")
        # lstDatabase.append(car1)
        # print(car1.get_info())
        
        NewStudent = clsStudents(140308201, "Behdad", "Pourtavakoli", 2594395587, "1360/06/26", "bpourtavakoli@gmail.com", "0924312079")
        lstDatabase.append(NewStudent)
        # NewStudent.StudentInfo()

        NewStudent = clsStudents(140308202, "Hilda", "Haghdoost", 2593375051, "1358/09/10", "hl.haghdoost@gmail.com", "09111304858")
        lstDatabase.append(NewStudent)

        NewStudent = clsStudents(140308203, "Hila", "Pourtavakoli", 2582688223, "1395/02/01", "hilapourtavakoli@gmail.com", "01333500583")
        lstDatabase.append(NewStudent)
        
        for lstItems in lstDatabase:
            lstItems.StudentInfo()
            print()

    '''
    /// CodeYad19(self)--function to review the Python language by CodeYad.com
    /// Class inheritance
    /// Contains CodeYad lessons by video: 80..87 and W3Schools.com
    /// ADDED by engineer B.Pourtavakoli on 1403/08/21
    '''
    def CodeYad19(self):
        clsP1 = clsPersons("Behdad", "Pourtavakoli", "2594395587", "1360/06/26", "Hamid", "09113304169", 
                           "No. 7, 4th Floor, Anahita Building, Nargess Alley, Saffari st., Bisetoon st., Rasht, Guilan, Iran", 
                           "bpourtavakoli@gmail.com")
        clsP1.PersonInfo()
        
        print()
        
        clsP2 = clsUsers("Behdad", "Pourtavakoli", "2594395587", "1360/06/26", 50496, "Hamid", "09113304169", 
                         "No. 7, 4th Floor, Anahita Building, Nargess Alley, Saffari st., Bisetoon st., Rasht, Guilan, Iran", 
                         "bpourtavakoli@gmail.com")
        clsP2.PersonInfo()

    '''
    /// CodeYad20(self)--function to review the Python language by CodeYad.com
    /// data structure review: List, Tuple, Set, Dictionary
    /// Contains CodeYad lessons by video: 86..86 and W3Schools.com
    /// ADDED by engineer B.Pourtavakoli on 1403/08/21
    '''
    def CodeYad20(self):
        lstList = [ 'Blueberry', 'Kiwi', 'Apple', 'Banana', 'Kiwi', 'Tomato', 'Kiwi' ]
        tupTuple = ( "Name", "Behdad", "Family", "Pourtavakoli", "Age", "43", "Job", "Developer" )
        setSet = { 'Blueberry', 'Kiwi', 'Apple', 'Banana', 'Kiwi', 'Tomato', 'Kiwi' }
        dicDictionary = { "Name": "Behdad", "Family": "Pourtavakoli", "Age": "43", "Job": "Developer" }
        
        for i in range(1, 11):
            print(f"{random.choice(lstList)} - {random.choice(tupTuple)}")        

    def ConvertJ2G(self, dtYear, dtMonth, dtDay):
        """
        ConvertJ2G()--function to convert Jalali to Gregorian date

        ADDED by engineer B.Pourtavakoli on 1403/08/29

        Parameters:
        dtYear (int): Year
        dtMonth (int): Month
        dtDay (int): Day
        """
        try:
            dtJalaliDate = jdatetime.date(dtYear, dtMonth, dtDay)
            dtGregorianDate = dtJalaliDate.togregorian()
            dtGregorianDate = str(dtGregorianDate).replace("-", "/")
            return (dtGregorianDate)
        except ValueError as e:
            return (f"خطا در تبدیل تاریخ: {e}")

    def ConvertG2J(self, dtYear, dtMonth, dtDay):
        """
        ConvertG2J()--function to convert Gregorian to Jalali date

        ADDED by engineer B.Pourtavakoli on 1403/08/29

        Parameters:
        dtYear (int): Year
        dtMonth (int): Month
        dtDay (int): Day
        """
        try:
            dtGregorianDate = datetime(dtYear, dtMonth, dtDay)
            dtJalaliDate = jdatetime.date.fromgregorian(date=dtGregorianDate)
            dtJalaliDate = str(dtJalaliDate).replace("-", "/")
            return (dtJalaliDate)
        except ValueError as e:
            return (f"خطا در تبدیل تاریخ: {e}")

    def CodeYad21(self):
        '''
        /// CodeYad21(self)--function to review the Python language by CodeYad.com

        /// , Datetime

        /// Contains CodeYad lessons by video: 87..92 and W3Schools.com

        /// ADDED by engineer B.Pourtavakoli on 1403/08/21

        /// EDITED by engineer B.Pourtavakoli on 1403/08/28
        '''
        dtToday = datetime.now()
        dtYear = dtToday.year
        dtMonth = dtToday.month
        dtDay = dtToday.day
        
        dtHour = dtToday.hour
        dtMinute = dtToday.minute
        dtSecond = dtToday.second
        dtTimePeriod = dtToday.strftime("%p")
        dtWeekday1 = dtToday.strftime("%a")
        dtWeekday2 = dtToday.strftime("%A")
        dtMonth1 = dtToday.strftime("%b")
        dtMonth2 = dtToday.strftime("%B")
        
        print(f"Today is {dtToday}")
        print(f"Today: {dtYear}/{dtMonth}/{dtDay} ({dtMonth1} - {dtWeekday1}) / ({dtMonth2} - {dtWeekday2}) - "
              f"{dtHour}:{dtMinute}:{dtSecond}:{dtTimePeriod}")
        
        dtShortDT1 = dtToday.strftime("%c")
        dtShortDT2 = dtToday.strftime("%x")
        dtShortDT3 = dtToday.strftime("%X")
        print(f"Today is: {dtShortDT1} - {dtShortDT2} - {dtShortDT3}")

        print()
        
        dtEnd = dtToday + timedelta(hours=48)
        dtDifferents = dtEnd - dtToday
        print(f"Start date: {dtToday}, End date: {dtEnd}, Differents: {dtDifferents.days} days, "
              f"Differents: {int(dtDifferents.total_seconds() / 86400)} Times")
        
        print()
        
        print(f"Year: {dtToday.year}, Month: {dtToday.month}, Day: {dtToday.day}")
        
        dtDate = (1402, 8, 28)        
        dtJalaliDate = self.ConvertJ2G(1402, 8, 28)
        
        dtDate = (2024, 11, 19)        
        dtGregorianDate = self.ConvertG2J(2024, 11, 19)
        
        print(f"Gregorian date: {dtGregorianDate}{NEWLINE}Jalali date: {dtJalaliDate}")
        
        return

        dicDictionary = { }
        tupTuple = [ "Asia/Tehran", "Europe/London", "Europe/Berlin", "America/New_York", "America/Los_Angeles",
                     "Africa/Cairo", "Australia/Sydney", "America/Sao_Paulo", "UTC" ]

        for tz in tupTuple:
            tzTimeZone = pytz.timezone(tz)
            now = datetime.now(tzTimeZone)

            utc_offset = now.strftime("%z")
            # print(utc_offset, utc_offset[:3] + ":" + utc_offset[3:])
            formatted_offset = f"UTC{utc_offset[:3]}:{utc_offset[3:]}"
            dicDictionary[tz] = f"{now.strftime('%Y-%m-%d %H:%M:%S')} ({formatted_offset})"

        pprint.pprint(dicDictionary)

        # tzTimeZone = pytz.all_timezones
        # print(f"All Time Zones: {tzTimeZone}")

        
        return

        print(f"OP System: {platform.system()}")
        print(f"Processor Type: {platform.processor()}")

        for i in range(1, 11):
            print(f"{random.randint(100, 999)} - {random.randrange(100, 999)}")

        x = dir(platform)
        pprint.pprint(x)

    def CodeYad22(self):
        '''
        /// CodeYad22(self)--function to review the Python language by CodeYad.com
        
        /// Some usefull functions, math.*
        
        /// Contains CodeYad lessons by video: 93 and W3Schools.com
        
        /// ADDED by engineer B.Pourtavakoli on 1403/09/01
        '''
        x = [46, 15, 8, 95]
        print(min(x), max(x))
        
        y = -128.511
        print(abs(y))
        
        print(pow(10, 128))
        
        x = int(math.sqrt(64))
        print(x)
        
        x = math.ceil(1.5)
        y = math.floor(1.5)
        print(x, y)

    def CodeYad23(self):
        '''
        /// CodeYad23(self)--function to review the Python language by CodeYad.com
        
        /// JSon
        
        /// Contains CodeYad lessons by video: 94..98
        
        /// ADDED by engineer B.Pourtavakoli on 1403/09/01
        '''
        # Not a real dictionary
        dicJSonList = '{ "Microsoft": "Visual C++", "MSVS": "C# .Net", "VSCode": "Python", "Borland": "Delphi" }'
        print(dicJSonList)
        
        jsJSonList = json.loads(dicJSonList)
        print(jsJSonList)
        
        print()
        
        dicJSonList = { "Microsoft": "C# .Net", "VSCode": "Python", "age": 43, "Developer": True, "Familiar": None }
        print(dicJSonList)
        
        jsJSonList = json.dumps(dicJSonList, indent=8, sort_keys=True)
        print(jsJSonList)

    def CodeYad24(self):
        '''
        /// CodeYad24(self)--function to review the Python language by CodeYad.com
        
        /// RE (Regular Expression)
        
        /// Contains CodeYad lessons by video: 99
        
        /// ADDED by engineer B.Pourtavakoli on 1403/09/01
        '''
        strTemp = "Don't forget Engineer Behdad Pourtavakoli"
        # reRegEx = re.search("^Engineer.*Behdad$", strTemp);
        reRegEx = re.search("Beh", strTemp);
        print(reRegEx)

    def CodeYad25(self):
        '''
        /// CodeYad25(self)--function to review the Python language by CodeYad.com
        
        /// PIP, Cowsay module
        
        /// Contains CodeYad lessons by video: 100..102
        
        /// ADDED by engineer B.Pourtavakoli on 1403/09/01
        '''
        strMessage = "Hi buddy, My developer...!"
        cowsay.cow(strMessage)
        cowsay.dragon(strMessage)
        cowsay.cow(strMessage)
        cowsay.cow(strMessage)
        cowsay.cow(strMessage)
        cowsay.cow(strMessage)
        print()
        my_fish = r'''
        \
        \  
                /`·.¸
            /¸...¸`:·
        ¸.·´  ¸   `·.¸.·´)
        : © ):´;      ¸  {
        `·.¸ `·  ¸.·´\`·¸)
            `\\´´\¸.·´
        '''
        cowsay.draw('Sharks are my best friend', my_fish)
        print()

    def CodeYad26(self):
        '''
        /// CodeYad26(self)--function to review the Python language by CodeYad.com

        /// Virtual Environment in Python: >>> Python -m venv [env name]

        /// by cmd go to [Virtual Environment folder\\[env name]\\Scripts\\] >>> pip list & >>> pip install [package name]
        
        /// >>> pip install requests [another important library]

        /// Contains CodeYad lessons by video: 103

        /// ADDED by engineer B.Pourtavakoli on 1403/09/01
        '''
        pass
    
    def CodeYad27(self):
        '''
        /// CodeYad27(self)--function to review the Python language by CodeYad.com

        /// Error handling

        /// Contains CodeYad lessons by video: 104..106

        /// ADDED by engineer B.Pourtavakoli on 1403/09/01
        '''
        try:
            print(1 / 0)
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Error: {e}")
        else:
            print("Else occurred")
        finally:
            print("Finally occurred")

    def CodeYad27(self):
        '''
        /// CodeYad27(self)--function to review the Python language by CodeYad.com

        /// Pycharm, ...

        /// Contains CodeYad lessons by video: 107..108

        /// ADDED by engineer B.Pourtavakoli on 1403/09/01
        '''
        pass
            
    def CodeYad28(self):
        '''
        /// CodeYad28(self)--function to review the Python language by CodeYad.com

        /// List comperhension (.append(), inline instruction, range())

        /// Contains CodeYad lessons by video: 109..110

        /// ADDED by engineer B.Pourtavakoli on 1403/09/01
        '''
        names = [ 'Hilda', 'Hila', 'Behdad', 'Soheila', 'Hamid', 'Behnaz' ]

        namelist = [name for name in names if "H" in name]
        print(names)
        print(namelist)

        namelist = []
        for name in names:
            if ("e" in name):
                namelist.append(name)
        print(names)
        print(namelist)

        numbers = [ 1, 3, 5, 7, 9 ]
        numlist = [num * 3 for num in numbers]
        print(numbers)
        print(numlist)

    def CodeYad29(self):
        '''
        /// CodeYad29(self)--function to review the Python language by CodeYad.com

        /// iterator vs Iterable: iter(), next(), for functions: __iter__, __next__

        /// Contains CodeYad lessons by video: 111..112

        /// ADDED by engineer B.Pourtavakoli on 1403/09/01
        '''
        try:
            name = "Behdad Pourtavakoli"
            myiterator = iter(name)
            print(next(myiterator))
            print(next(myiterator))
            print(next(myiterator))
            print(next(myiterator))
            print(next(myiterator))
            print(next(myiterator))
            print(next(myiterator))
            print(next(myiterator))
            print(next(myiterator))
            print(next(myiterator))
            print(next(myiterator))
            print(next(myiterator))
            print(next(myiterator))
            print(next(myiterator))
            print(next(myiterator))
            print(next(myiterator))
            print(next(myiterator))
            print(next(myiterator))
            print(next(myiterator))
            print(next(myiterator))
        except StopIteration:
            print("No more item")

        try:
            namesList = [ 'Hilda', 'Hila', 'Behdad', 'Soheila', 'Hamid', 'Behnaz' ]
            myiterator = iter(namesList)
            print(next(myiterator))
            print(next(myiterator))
            print(next(myiterator))
            print(next(myiterator))
            print(next(myiterator))
            print(next(myiterator))
            print(next(myiterator))
            print(next(myiterator))
            print(next(myiterator))
            print(next(myiterator))
        except StopIteration:
            print("No more item")
            
        for name in namesList:
            print(name)

    def CodeYad30(self):
        '''
        /// CodeYad30(self)--function to review the Python language by CodeYad.com

        /// def FunctionCaller(func) ... return func /// var = FuynctionCaller(SecondFunction) /// var.func features
        
        /// decorators in function: @function name
        
        /// make a property for decorator, @property

        /// Contains CodeYad lessons by video: 113..115 & 116 semi-half and CodeYad3.py {Source 1..9 & 11..13}

        /// ADDED by engineer B.Pourtavakoli on 1403/09/01
        /// UPDATED by engineer B.Pourtavakoli on 1403/09/03
        '''
        pass

    def CodeYad31(self):
        '''
        /// CodeYad31(self)--function to review the Python language by CodeYad.com

        /// use [ _ ] underline or underscore instead variable name in loop for lists.
        
        /// resevred words, (Localization), REPL, (Special Methods or Dunder Methods)

        /// OOP: Encapsulation(_[var name] -> protected, __[var name] -> private)

        /// Contains CodeYad lessons by video: 116..118 and CodeYad3.py {Source 10}

        /// ADDED by engineer B.Pourtavakoli on 1403/09/03
        '''
        pass

    def CodeYad32(self):
        '''
        /// CodeYad32(self)--function to review the Python language by CodeYad.com

        /// abstract class, polymorphism

        /// Contains CodeYad lessons by video: 119..120 and CodeYad3.py {Source 14..15}

        /// ADDED by engineer B.Pourtavakoli on 1403/09/03
        '''
        pass

    def CodeYad33(self):
        '''
        /// CodeYad33(self)--function to review the Python language by CodeYad.com

        /// str vs repr: Returns a readable version of an object, generators [yield] (for big data), fibonacci function by yield

        /// Contains CodeYad lessons by video: 121..123 and CodeYad3.py {Source 16..19}

        /// ADDED by engineer B.Pourtavakoli on 1403/09/03
        '''
        s = "Hello Behdad"
        print(str(s))
        print(str(2.0 / 11.0))

        print(repr(s))
        print(repr(2.0 / 11.0))
        
    def CodeYad33(self):
        '''
        /// CodeYad33(self)--function to review the Python language by CodeYad.com

        /// __name__

        /// Contains CodeYad lessons by video: 124 and CodeYad3.py {Source 20}

        /// ADDED by engineer B.Pourtavakoli on 1403/09/03
        '''
        pass

    def CodeYad34(self):
        '''
        /// CodeYad34(self)--function to review the Python language by CodeYad.com

        /// id -> objecct identification, namespace and score
        
        /// build-in, global, local, nonlocal
        
        /// global keyword: global variable

        /// Contains CodeYad lessons by video: 125..126

        /// ADDED by engineer B.Pourtavakoli on 1403/09/03
        '''
        a = 2
        print(id(2))
        print(id(a))
        
        b = a
        print(id(b))

        c = 2
        print(id(c))

    def CodeYad35(self):
        '''
        /// CodeYad35(self)--function to review the Python language by CodeYad.com

        /// GUI (Graphic User Interface): PyQt5, Kkinter, Kivy, PySimpleGUI, PyGUI, wxPython, Pyforms

        /// Contains CodeYad lessons by video: 128..130 and 131 (instaloader) CodeYad3.py {Source 21}

        /// ADDED by engineer B.Pourtavakoli on 1403/09/03
        '''
        window = Tk()
        window.title("Instagram profile downloader")
        window.geometry("600x400")
        window.minsize(320, 200)
        window.maxsize(860, 568)
        
        lblTemp = Label(window, text="Hello Behdad")
        lblTemp.pack()
        
        txtEntry = Entry(window)
        txtEntry.pack()
        
        button = Button(window, text="Calculate", command=Button_Click)
        button.pack()
        # button.place(100, 200)
        button.config()
        
        window.mainloop()

    def Factorial(self, n):
        if (n <= 1):
            return (1)
        else:
            return (n * self.Factorial(n - 1))

    def Fibonacci(self, n):
        if (n <= 1):
            return (n)
        else:
            return (self.Fibonacci(n - 1) + self.Fibonacci(n - 2))

    def CodeYad36(self):
        '''
        /// CodeYad36(self)--function to review the Python language by questions.

        /// Review something to remember. / Wiederholen Sie etwas, das Sie sich merken möchten.

        /// ADDED by engineer B.Pourtavakoli on 1403/09/05
        '''
        intTemp = 5
        print(f"Factorial({intTemp}): {self.Factorial(intTemp)}")

        intTemp = 10
        print(f"Fibonacci({intTemp}): {self.Fibonacci(intTemp)}")

    def CodeYad37(self):
        '''
        /// CodeYad37(self)--function to review the Python language by CodeYad.com

        /// binance, digital marketing, bitcoin, synchronous/asynchronous programming

        /// Contains CodeYad lessons by video: 132..142 (End of CodeYad-Python-Learning)

        /// ADDED by engineer B.Pourtavakoli on 1403/09/05
        '''
        pass

    async def TaskRunner(self, tskName, intDuring):
        pass
        dtStart = time.time()
        print(f"{tskName} Starting...")
        await asyncio.sleep(intDuring)
        dtEnd = time.time()
        print(f"{tskName} Ended | ETA Time: {dtEnd - dtStart:2f} seconds.")

    async def task1(self):
        print("Task 1 Starting...")
        await asyncio.sleep(2)
        print("Task 1 Ended.")

    async def task2(self):
        print("Task 2 Starting...")
        await asyncio.sleep(3)
        print("Task 2 Ended.")

    async def task3(self):
        print("Task 3 Starting...")
        await asyncio.sleep(2)
        print("Task 3 Ended.")

    async def main_caller(self):
        print("APP Tasks Starting...")
        await asyncio.gather(
            self.TaskRunner("Task1", 2.1), 
            self.TaskRunner("Task2", 2), 
            self.TaskRunner("Task3", 2.1), 
        )
        # await asyncio.gather(self.task1(), self.task2(), self.task3())
        print("APP Tasks Ended.")

    def MeineErfahrung1(self):
        '''
        /// MeineErfahrung1(self)--function to continue review the Python language by w3schools and geeksforgeeks

        /// asynchronous programming (async, await)

        /// ADDED by engineer B.Pourtavakoli on 1403/09/05
        '''
        start_time = time.time()
        asyncio.run(self.main_caller())
        end_time = time.time()
        print(f"APP ETA Time: {end_time - start_time:.2f} Seconds.")

    def MeineErfahrung2(self):
        '''
        /// MeineErfahrung2(self)--function to continue review the Python language by w3schools and geeksforgeeks

        /// File operation #1
        
        /// https://www.w3schools.com/python/python_file_handling.asp

        /// ADDED by engineer B.Pourtavakoli on 1403/09/05
        /// UPDATED by engineer B.Pourtavakoli on 1403/09/06
        '''
        
        try:
            strMainPath1 = str(pathlib.Path(__file__).parent.resolve())
            if (not strMainPath1.endswith("\\")):
                strMainPath1 += "\\"

            strMainPath2 = str(pathlib.Path().resolve())
            if (not strMainPath2.endswith("\\")):
                strMainPath2 += "\\"

            print(strMainPath1)
            print()
            print(strMainPath2)

            strMainPath1 += "bot_output.log"
            check_file = os.path.isfile(strMainPath1)
            if (check_file):
                file = open(strMainPath1, "r")
                for line in file:
                    print(line.strip())
                file.close()
            else:
                print("Error: File not fount.")

        except Exception as e:
            print(f"File handling error: {e}")

    def MeineErfahrung3(self):
        '''
        /// MeineErfahrung3(self)--function to continue review the Python language by w3schools and geeksforgeeks

        /// File operation #2
        
        /// https://www.w3schools.com/python/python_file_handling.asp

        /// ADDED by engineer B.Pourtavakoli on 1403/09/06
        '''
        try:
            strMainPath = str(pathlib.Path(__file__).parent.resolve())
            if (not strMainPath.endswith("\\")):
                strMainPath += "\\"
            strFilePath = strMainPath + "Python_File.txt"
            
            with open(strFilePath, "w", encoding="utf-8") as file:
                file.write("Hi Behdad\n")
                file.write("This is a sample text, created by Python in VS Code.\n")

            with open(strFilePath, "a", encoding="utf-8") as file:
                file.write("And, the New text inserted.\n")

            with open(strFilePath, "r", encoding="utf-8") as file:
                for line in file:
                    print(line.strip())
                # content = file.read()
                # print(content)

            if os.path.exists(strFilePath):
                os.remove(strFilePath)
                print(f"The file [{strFilePath}] removed.")
            else:
                print(f"The file [{strFilePath}] does not exist")
        except Exception as e:
            print(f"File handling error: {e}")

    def fn_ListDuplicateRemover(self, lstTemp):
        return list(dict.fromkeys(lstTemp))

    def fn_TupleDuplicateRemover(self, tupTuple):
        return tuple(dict.fromkeys(tupTuple))

    def MeineErfahrung4(self):
        '''
        /// MeineErfahrung4(self)--function to continue review the Python language by w3schools and geeksforgeeks

        /// Python How To: How to Remove Duplicates From a Python List
        
        /// https://www.w3schools.com/python/python_howto_remove_duplicates.asp

        /// ADDED by engineer B.Pourtavakoli on 1403/09/06
        '''
        try:
            myList = [ "a", "b", "a", "c", "c", "b", "d", "a", "a", "d", "b" ]
            print(f"List: {myList}")

            myList = list(dict.fromkeys(myList))
            print(f"List: {myList}\r\n")

            myTuple = ( "a", "b", "a", "c", "c", "b", "d", "a", "a", "d", "b" )
            print(f"Tuple: {myTuple}")

            myTuple = list(dict.fromkeys(myTuple))
            print(f"Tuple: {myTuple}\r\n")

            mySet = { "a", "b", "a", "c", "c", "b", "d", "a", "a", "d", "b" }
            print(f"Set: {mySet}")

            mySet = list(dict.fromkeys(mySet))
            print(f"Set: {mySet}\r\n")

            myList = [ "a", "b", "a", "c", "c", "b", "d", "a", "a", "d", "b" ]
            myTuple = ( "a", "b", "a", "c", "c", "b", "d", "a", "a", "d", "b" )
            print(f"List: {self.fn_ListDuplicateRemover(myList)}")
            print(f"Tuple: {self.fn_TupleDuplicateRemover(myTuple)}\r\n")
            
        except Exception as e:
            print(f"OP error: {e}")        

    def MeineErfahrung5(self):
        '''
        /// MeineErfahrung5(self)--function to continue review the Python language by w3schools and geeksforgeeks

        /// Python How To: Reverse string and text
        
        /// https://www.w3schools.com/python/python_howto_reverse_string.asp

        /// ADDED by engineer B.Pourtavakoli on 1403/09/06
        '''
        try:
            strTemp = "Behdad Pourtavakoli"
            print(f"Normal Text: {strTemp}")
            print(f"Reverse Text: {strTemp[::-1]}")
        except Exception as e:
            print(f"OP error: {e}")

    def MeineErfahrung6(self):
        '''
        /// MeineErfahrung6(self)--function to continue review the Python language by w3schools and geeksforgeeks

        /// NumPy Tutorial: array, ndim, 
        
        /// https://www.w3schools.com/python/numpy/default.asp

        /// ADDED by engineer B.Pourtavakoli on 1403/09/06
        '''
        try:
            arrX = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                             [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
                             [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])
            print(f"Number of Dimensions of arrX: {arrX.shape}, {arrX.ndim}")
            print(arrX)


            '''
            print(f"NumPy Version: {np.__version__}")
            
            arr1 = np.array(42)
            print(f"NumPy Array: {arr1}, NumPy Type: {type(arr1)}")
            
            arr2 = np.array([1, 2, 3, 4, 5])
            print(f"NumPy Array: {arr2}, NumPy Type: {type(arr2)}")

            arr3 = np.array([[1, 2, 3], [4, 5, 6]])
            print(f"NumPy Array: {arr3}")
            
            arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
            print(f"NumPy Array: {arr4}")

            arr5 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [1, 2, 3]], [[1, 2, 3], [4, 5, 6]]])
            print(f"NumPy Array: {arr5}")

            arr6 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                             [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
                             [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])
            print(f"NumPy Array: {arr6}")

            arr_4d = np.array([[[[1, 2], [3, 4]], 
                                
                                [[5, 6], [7, 8]]], 
                               
                               [[[9, 10], [11, 12]], 
                                
                                [[13, 14], [15, 16]]]])


            arr7 = np.array([[[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 
                            [[10, 11, 12], [13, 14, 15], [16, 17, 18]], 
                            [[19, 20, 21], [22, 23, 24], [25, 26, 27]]],
                             
                            [[[28, 29, 30], [31, 32, 33], [34, 35, 36]], 
                            [[37, 38, 39], [40, 41, 42], [43, 44, 45]], 
                            [[46, 47, 48], [49, 50, 51], [52, 53, 54]]],
                            
                            [[[55, 56, 57], [58, 59, 60], [61, 62, 63]], 
                            [[64, 65, 66], [67, 68, 69], [70, 71, 72]], 
                            [[73, 74, 75], [76, 77, 78], [79, 80, 81]]]])

  
            # arr6 = np.array([[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [1, 2, 3]], [[4, 5, 6], [7, 8, 9]])
            # print(f"NumPy Array: {arr6}, NumPy Type: {type(arr6)}")
  
            print(f"A1 Number of Dimensions: {arr1.ndim}")
            print(f"A2 Number of Dimensions: {arr2.ndim}")
            print(f"A3 Number of Dimensions: {arr3.ndim}")
            print(f"A4 Number of Dimensions: {arr4.ndim}")
            print(f"A5 Number of Dimensions: {arr5.ndim}")
            print(f"A6 Number of Dimensions: {arr6.ndim}")'''
        except Exception as e:
            print(f"OP error: {e}")

    def MeineErfahrung7(self):
        '''
        /// MeineErfahrung7(self)--function to continue review the Python language by w3schools and geeksforgeeks

        /// File handling and NumPy
        
        /// https://www.w3schools.com/python/numpy/numpy_creating_arrays.asp , https://chatgpt.com/c/67458316-0130-8003-a08c-e12fdb4b57c6

        /// ADDED by engineer B.Pourtavakoli on 1403/09/06
        '''
        exit(0)
        try:
            strMainPath = str(pathlib.Path(__file__).parent.resolve())
            if (not strMainPath.endswith("\\")):
                strMainPath += "\\"
            strFilePath = strMainPath + "bot_output.log"
            
            with open(strFilePath, "r", encoding="utf-8") as file:
                text = file.read()
            numbers = re.findall(r'\d+', text)
            numbers = [int(num) for num in numbers]
            print(numbers)
        except Exception as e:
            print(f"OP error: {e}")

# **********************************************************************************************************
# endregion

# region Other classes
# **********************************************************************************************************
'''
/// Other classes: clsStudents, clsCar, clsPersons, clsUsers, ...
/// ADDED by engineer B.Pourtavakoli on 1403/08/01
'''

class clsStudents:
    def __init__(self, intStCode, strName, strFamily, intIdCode, strBDate, strEMail = "", strCellphone = ""):
        self.intStCode = intStCode
        self.strName = strName
        self.strFamily = strFamily
        self.intIdCode = intIdCode
        self.strBDate = strBDate
        self.strEMail = strEMail
        self.strCellphone = strCellphone
    
    def StudentInfo(self):
        print(f"Student No: {self.intStCode}, Student Name: {self.strName} {self.strFamily}")
        print(f"Student Identification Code: {self.intIdCode}, Student Birth date: {self.strBDate}")
        print(f"EMail: {self.strEMail}, Cellphone: {self.strCellphone}")

        if self.intStCode:
            print(f"EMail: {self.strEMail}", end=', ')
            
        if self.intStCode:
            print(f"Cellphone: {self.strCellphone}")

class clsCar:
    def __init__(self, model, year, color="Black"):
        self.model = model           # مدل خودرو
        self.year = year             # سال تولید
        self.color = color           # رنگ خودرو
        self.speed = 0               # سرعت خودرو که به صورت پیش‌فرض ۰ است
        self.is_on = False           # وضعیت روشن یا خاموش بودن خودرو

    def start(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.model} started.")
        else:
            print(f"{self.model} is already running.")

    def stop(self):
        if self.is_on:
            self.is_on = False
            self.speed = 0
            print(f"{self.model} stopped.")
        else:
            print(f"{self.model} is already off.")

    def accelerate(self, increase):
        if self.is_on:
            self.speed += increase
            print(f"{self.model} accelerated by {increase} km/h. Current speed: {self.speed} km/h.")
        else:
            print(f"Can't accelerate. {self.model} is off.")

    def brake(self, decrease):
        if self.is_on:
            self.speed = max(0, self.speed - decrease)
            print(f"{self.model} slowed down by {decrease} km/h. Current speed: {self.speed} km/h.")
        else:
            print(f"Can't brake. {self.model} is off.")

    def get_info(self):
        status = "on" if self.is_on else "off"
        return f"Model: {self.model}, Year: {self.year}, Color: {self.color}, Speed: {self.speed} km/h, Status: {status}"

class clsPersons:
    def __init__(self, strName, strFamily, strUId, strBDate, strFather = "", strCellphone = "", strAddress = "", strEMail = ""):
        self.strName = strName
        self.strFamily = strFamily
        self.strUId = strUId
        self.strBDate = strBDate
        self.strFather = strFather
        self.strCellphone = strCellphone
        self.strEMail = strEMail
        self.strAddress = strAddress
    
    def PersonInfo(self):
        print(f"Person Unique ID: {self.strUId}, Person name: {self.strName} {self.strFamily}")
        
        if self.strFather:
            print(f"Father name: {self.strFather}", end=', ')
            
        print(f"Birth date: {self.strBDate}")
        
        if self.strCellphone:
            print(f"Cellphone: {self.strCellphone}")

        if self.strEMail:
            print(f"EMail: {self.strEMail}", end=', ')

        if self.strAddress:
            print(f"Address: {self.strAddress}")

class clsUsers(clsPersons):
    def __init__(self, strName, strFamily, strUId, strBDate, intUserId, strFather="", strCellphone="", strAddress="", strEMail=""):
        super().__init__(strName, strFamily, strUId, strBDate, strFather, strCellphone, strAddress, strEMail)
        self.intUserId = intUserId

    def PersonInfo(self):
        print(f"User IDentification: {self.intUserId}, Person name: {self.strName} {self.strFamily}")
        
        if self.strFather:
            print(f"Father name: {self.strFather}", end=', ')
            
        print(f"Birth date: {self.strBDate}")
        
        if self.strCellphone:
            print(f"Cellphone: {self.strCellphone}")

        if self.strEMail:
            print(f"EMail: {self.strEMail}", end=', ')

        if self.strAddress:
            print(f"Address: {self.strAddress}")

# **********************************************************************************************************
# endregion

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
/// WinMain()--Main program, contains main statements and calling functions
/// ADDED by engineer B.Pourtavakoli on 1403/06/30
'''
def WinMain():
    # region CodeYad section
    # **********************************************************************************************************
    CY1 = CodeYad1()
    CY1.ClearScreen()

    CY1.MeineErfahrung6()
    CY1.MeineErfahrung7()
    
    # CY1.MeineErfahrung5()
    # CY1.MeineErfahrung4()
    # CY1.MeineErfahrung3()
    # CY1.MeineErfahrung2()
    # CY1.MeineErfahrung1()
    
    # CY1.CodeYad37()
    # CY1.CodeYad36()
    # CY1.CodeYad35()
    # CY1.CodeYad34()
    # CY1.CodeYad33()
    # CY1.CodeYad32()
    # CY1.CodeYad31()
    # CY1.CodeYad30()
    # CY1.CodeYad29()
    # CY1.CodeYad28()
    # CY1.CodeYad27()
    # CY1.CodeYad26()
    # CY1.CodeYad25()
    # CY1.CodeYad24()
    # CY1.CodeYad23()
    # CY1.CodeYad22()
    # CY1.CodeYad21()
    # CY1.CodeYad20()
    # CY1.CodeYad19()
    # CY1.CodeYad18()
    # CY1.CodeYad17()
    # CY1.CodeYad16()
    # CY1.CodeYad15()
    # CY1.CodeYad14()
    # CY1.CodeYad13()

    # CY1.CodeYad8()
    
    # for i in range(1, 11):x
    #     print(f"Fibonacci sequense ({i}): {CY1.Fibonacci(i)}")

    # CY1.CodeYad12()
    # CY1.CodeYad11()
    # CY1.CodeYad10()
    # CY1.CodeYad9()
    # CY1.CodeYad7()
    # CY1.CodeYad6()
    # CY1.CodeYad5()
    # CY1.CodeYad4()
    # CY1.CodeYad3()
    # CY1.CodeYad2()
    # CY1.CodeYad1()
    
    # CY1.PyClassCaller()
    # **********************************************************************************************************
    # endregion

    return

    # region Encryptior/Decryptor section
    # **********************************************************************************************************
    strText = "Behdad Pourtavakoli"
    
    strText = lorem.text()
    strText = strText[:128]
    print(f"Plain Text: {strText}\r\n")

    strKey = b'Eng.B2e5h8d4a1d4' # 16-byte key for AES-128
    encEncrypted = AES_Encrypt_L1(strText, strKey)
    print(f"Encrypted Text by Level 1: {Encrypted_Formated(encEncrypted)} - Length: {len(encEncrypted)}\r\n")

    # Generate a 32-byte key (AES-256)
    strKey = os.urandom(32)
    encEncrypted = AES_Encrypt_L2(strText, strKey)
    print(f"Encrypted Text by Level 2: {Encrypted_Formated(encEncrypted)} - Length: {len(encEncrypted)}\r\n")

    # 24-byte key for AES-192
    strKey = b'B2e5h8d4a1d4Pourtavakoli'
    encEncrypted = AES_Encrypt_L3(strText, strKey)
    print(f"Encrypted Text by Level 3: {Encrypted_Formated(encEncrypted)} - Length: {len(encEncrypted)}\r\n")

    ## Save_Encrypted_Data(encEncrypted, strKey)
    ## print("Encryption Level 3 complete. Data saved in files.")

    # 16-byte key for AES-128
    strKey = b'Eng.B2e5h8d4a1d4'
    encEncrypted = AES_Encrypt_L4(strText, strKey)
    print(f"Encrypted Text by Level 4: {Encrypted_Formated(encEncrypted)} - Length: {len(encEncrypted)}\r\n")

    # Generate a random key
    strKey = Generate_Key()
    encEncrypted = AES_Encrypt_L5(strText, strKey)
    print(f"Encrypted Text by Level 5: {Encrypted_Formated(encEncrypted)} - Length: {len(encEncrypted)}")

    # **********************************************************************************************************
    # endregion
   
    # print("Press Enter key to exit...", end='')
    # input()
# **********************************************************************************************************
# endregion

# region Main program caller
# **********************************************************************************************************
'''
///*********************************************************************************************************
///* Main program caller
///*********************************************************************************************************
'''
if (__name__ == "__main__"):
    WinMain()
# **********************************************************************************************************
# endregion
