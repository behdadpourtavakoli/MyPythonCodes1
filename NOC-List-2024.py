# region Copyright
# **********************************************************************************************************
'''
///*-=============================================================================================-*
/// File name             : NOC-List-2024.py
/// Version               : 1.0.0.0
/// Start                 : 2024-09-20 (1403/08/22)
/// Last update           : 2024-10-28 (1403/08/22)
/// Autor                 : Engineer Behdad Pourtavakoli
/// Trademark             : Behdad Software Developers Group™
/// ----------------------------------------------------------------------------------------------
/// Copyright © 1380-1403 (2001-2024) by B.S.D Group™
/// All rights reserved.
/// ----------------------------------------------------------------------------------------------
///
/// Description: Top Secret - Agents: Non Official Cover (NOC-List)
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

import string
import os, platform, time, hashlib, random, base64
from pathlib import Path

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

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

# Secret.Agency.Code
SAC = b'!Beh!dad!258!414!Pour!tava!koli!'

# **********************************************************************************************************
# endregion

# region Handwritten functions and procedures
# **********************************************************************************************************
'''
///*********************************************************************************************************
///* Handwritten functions and procedures
///*********************************************************************************************************
'''

class MainClass():
    '''
    /// ClearScreen()--function to clear the output screen
    /// ADDED by engineer B.Pourtavakoli on 1403/08/22
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
    /// Divider()--function to create a separator line with a given character.
    /// Parameters:
    /// bolLF: line feed, default: False
    /// chrTL: separator, default: '*'
    /// intMax: number of character repetitions, default: 70
    /// ADDED by engineer B.Pourtavakoli on 1402/11/20
    /// UPDATE by engineer B.Pourtavakoli on 1402/11/22
    '''
    def Divider(self, bolLF = False, chrTL = '*', intMax = 70):
        print(*intMax*(chrTL,), sep=' ')

        if (bolLF):
            print("")

    '''
    /// About()--function to display program information, version number and copyright as English
    /// ADDED by Engineer B.Pourtavakoli on 1402/07/18
    /// UPDATE by Engineer B.Pourtavakoli on 1403/08/22
    '''
    def About(self):
        strVersionVersionsnummer = str(platform.python_version())
        strNachricht = "Behdad Software Developers Group™ Presents\n\n"
        
        strNachricht += "Welcome to the B.S.D Group™ Production\n\n"
        
        strNachricht += "Copyright © 1380-1403 (2001-2024) by B.S.D Group™\n"
        strNachricht += "All rights reserved.\n\n"
        
        strNachricht += "Design and develop by Engineer Behdad Pourtavakoli\n\n"
        strNachricht += Path(__file__).name + " (Python v" + strVersionVersionsnummer + ") - ®B.S.D Group™"
        print(strNachricht)

    def generate_code(self, true_name, target_area):
        # ترکیب true_name و target_area
        combined = f"{true_name}:{target_area}"
        
        # ایجاد کد با استفاده از hashlib (نام کد شده)
        code_name = hashlib.sha1(combined.encode()).hexdigest()[:8].upper()
        
        # ایجاد شماره یا کد سیستمی با تولید یک شماره تصادفی
        code_no = f"IMF{random.randint(10, 99)}{code_name[:3]}{random.randint(10, 99)}"
        
        return code_name, code_no

    def decode_code(self, code_name, code_no):
        # این قسمت نیازمند ذخیره‌سازی true_name و target_area برای هر ترکیب است
        # یا می‌توانیم از یک دیتابیس استفاده کنیم تا true_name و target_area را پیدا کنیم
        
        print("برای دیکد کردن، باید true_name و target_area ترکیب شده ذخیره شده باشد.")

    def encrypt_data(self, true_name, target_area):
        combined = f"{true_name}:{target_area}"
        cipher = AES.new(SAC, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(combined.encode(), AES.block_size))
        
        # ترکیب IV و رمزنگاری شده برای استفاده در آینده
        iv = base64.b64encode(cipher.iv).decode('utf-8')
        ct = base64.b64encode(ct_bytes).decode('utf-8')
        
        # خروجی کد شده
        code_name = f"CN-{iv[:5]}{ct[:5]}"
        code_no = f"IMF-{iv[-5:]}{ct[-5:]}"
        
        return code_name, code_no, iv, ct

    def decrypt_data(self, iv, ct):
        # دیکد کردن IV و ciphertext از Base64
        iv = base64.b64decode(iv)
        ct = base64.b64decode(ct)
        
        # دیکد کردن داده‌ها با استفاده از AES
        cipher = AES.new(SAC, AES.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(ct), AES.block_size)
        true_name, target_area = decrypted.decode().split(":")
        
        return true_name, target_area

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
/// ADDED by engineer B.Pourtavakoli on 1403/08/22
'''
def WinMain():
    intStartTime = time.time()
    
    clsMClass = MainClass()
    clsMClass.ClearScreen()
    
    # characters = string.ascii_letters + string.digits
    # print(characters)
    # characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    # print(characters)

    true_name = "ANDREW EIO"
    target_area = "COVERT PRAGUE"
    code_name, code_no = clsMClass.generate_code(true_name, target_area)
    print("Code Name:", code_name)
    print("Code No.:", code_no)
    clsMClass.Divider(False, '-')

    code_name, code_no, iv, ct = clsMClass.encrypt_data(true_name, target_area)
    print(f"Code Name: {code_name} - Code No.: {code_no}")
    print(f"Encrypted Code Name: {iv} - Encrypted Code No.: {ct}")
    
    decoded_true_name, decoded_target_area = clsMClass.decrypt_data(iv, ct)
    print(f"True Name: {decoded_true_name} - Target Area.: {decoded_target_area}")

    decoded_true_name, decoded_target_area = clsMClass.decrypt_data(code_name, code_no)
    print(f"True Name: {decoded_true_name} - Target Area.: {decoded_target_area}")
    clsMClass.Divider(False, '-')

    intEndTime = time.time()
    intElapsedTime = intEndTime - intStartTime
    print("Elapsed time: %s ms" % round(intElapsedTime, 3), end=NEWLINE+NEWLINE)

    print("Press the Enter key to continue...", end='')
    input()
    
    clsMClass.About()
    
    print("Press Enter key to exit...", end='')
    input()
# **********************************************************************************************************
# endregion

# region Main program caller
# **********************************************************************************************************
'''
///*********************************************************************************************************
///* Main program caller
///*********************************************************************************************************
'''
'''
/// WinMain()--main program caller, contains the function caller WinMain()
/// ADDED by Engineer B.Pourtavakoli on 1403/08/22
'''
if (__name__ == "__main__"):
    WinMain()
# **********************************************************************************************************
# endregion
