# region Copyright
# **********************************************************************************************************
'''
///*-=============================================================================================-*
/// File name             : SmartCopyrightUpdater.py
/// Version               : 1.0.0.0
/// Start                 : 2024-12-06 (1403/09/16)
/// Last update           : 2024-12-06 (1403/09/16)
/// Autor                 : Engineer Behdad Pourtavakoli
/// Trademark             : Behdad Software Developers Group™
/// ----------------------------------------------------------------------------------------------
/// Copyright © 1380-1403 (2001-2024) by B.S.D Group™
/// All rights reserved.
/// ----------------------------------------------------------------------------------------------
///
/// Description: Smart Copyright Updater by B.S.D Group™
///
/// ----------------------------------------------------------------------------------------------
/// The developer's word: Do not forget the engineer Behdad Pourtavakoli.
///-=============================================================================================-*///
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

import os, platform, time, re, glob
from pathlib import Path
from tqdm import tqdm

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

# Constants for the starting Persian and Gregorian years
START_PERSIAN_YEAR = 1380
START_GREGORIAN_YEAR = 2001
CURRENT_PERSIAN_YEAR = 1403
CURRENT_GREGORIAN_YEAR = 2024

persian_to_gregorian_offset = START_GREGORIAN_YEAR - START_PERSIAN_YEAR

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
    def ClearScreen(self):
        '''
        /// ClearScreen()--function to clear the output screen
        
        /// ADDED by engineer B.Pourtavakoli on 1403/09/16
        '''
        if (os.name == "nt"):
            _ = os.system("cls")

    def Divider(self, bolLF = False, chrTL = '*', intMax = 70):
        '''
        /// Divider()--function to create a separator line with a given character.
        
        /// Parameters:
        
        /// bolLF: line feed, default: False
        
        /// chrTL: separator, default: '*'
        
        /// intMax: number of character repetitions, default: 70
        
        /// ADDED by engineer B.Pourtavakoli on 1402/11/20
        
        /// UPDATE by engineer B.Pourtavakoli on 1402/11/22
        '''
        print(*intMax*(chrTL,), sep=' ')

        if (bolLF):
            print("")

    def About(self):
        '''
        /// About()--function to display program information, version number and copyright as English
        
        /// ADDED by Engineer B.Pourtavakoli on 1402/07/18
        
        /// UPDATE by Engineer B.Pourtavakoli on 1403/09/16
        '''
        strVersionVersionsnummer = str(platform.python_version())
        strNachricht = "Behdad Software Developers Group™ Presents\n\n"
        
        strNachricht += "Welcome to the B.S.D Group™ Production\n\n"
        
        strNachricht += "Copyright © 1380-1403 (2001-2024) by B.S.D Group™\n"
        strNachricht += "All rights reserved.\n\n"
        
        strNachricht += "Design and develop by Engineer Behdad Pourtavakoli\n\n"
        strNachricht += Path(__file__).name + " (Python v" + strVersionVersionsnummer + ") - ®B.S.D Group™"
        print(strNachricht)

    def Persian_to_Gregorian(self, persian_year):
        '''
        /// Persian_to_Gregorian()--function to convert Persian years to Gregorian years (approximate method)
        
        /// Simple conversion logic (this should be replaced with a proper converter)
        
        /// ADDED by Engineer B.Pourtavakoli on 1402/09/16
        '''
        return (persian_year + 621)

    def Gregorian_to_Persian(self, gregorian_year):
        '''
        /// Gregorian_to_Persian()--function to convert Gregorian years to Persian years (approximate method)
        
        /// Simple conversion logic (this should be replaced with a proper converter)
        
        /// ADDED by Engineer B.Pourtavakoli on 1402/09/16
        '''
        return (gregorian_year - 621)

    def Get_Year_Range(self, text):
        '''
        /// Get_Year_Range()--function to get the latest Persian and Gregorian year from the input
        
        /// Extract Persian years and Gregorian years using regular expressions
        
        /// ADDED by Engineer B.Pourtavakoli on 1402/09/16
        '''
        # Extract all year sequences (both Persian and Gregorian)
        year_matches = re.findall(r"(\d{4})", text)
        
        # Split into Persian and Gregorian ranges
        persian_years = [int(year) for year in year_matches if 1300 <= int(year) <= 1500]
        gregorian_years = [int(year) for year in year_matches if 1900 <= int(year) <= 2100]

        # Handling cases based on the extracted years
        if (persian_years and not gregorian_years):
            start_persian = persian_years[0]
            start_gregorian = self.persian_to_gregorian(start_persian)
            end_persian = persian_years[-1] if (len(persian_years) > 1) else start_persian
            end_gregorian = self.persian_to_gregorian(end_persian)
        elif (gregorian_years and not persian_years):
            start_gregorian = gregorian_years[0]
            start_persian = self.gregorian_to_persian(start_gregorian)
            end_gregorian = gregorian_years[-1] if len(gregorian_years) > 1 else start_gregorian
            end_persian = self.gregorian_to_persian(end_gregorian)
        elif (persian_years and gregorian_years):
            start_persian = persian_years[0]
            start_gregorian = gregorian_years[0]
            end_persian = persian_years[-1] if (len(persian_years) > 1) else start_persian
            end_gregorian = gregorian_years[-1] if (len(gregorian_years) > 1) else start_gregorian
        else:
            start_persian = START_PERSIAN_YEAR
            start_gregorian = START_GREGORIAN_YEAR
            end_persian = CURRENT_PERSIAN_YEAR
            end_gregorian = CURRENT_GREGORIAN_YEAR

        # Adjust start year to 1380 (for Persian) or 2001 (for Gregorian) if needed
        if (start_persian != START_PERSIAN_YEAR):
            start_persian = START_PERSIAN_YEAR
            start_gregorian = self.persian_to_gregorian(start_persian)

        if (start_gregorian != START_GREGORIAN_YEAR):
            start_gregorian = START_GREGORIAN_YEAR
            start_persian = self.gregorian_to_persian(start_gregorian)

        return (start_persian, end_persian, start_gregorian, end_gregorian)

    def Format_Copyright(self, text):
        '''
        /// SmartCopyrightUpdater()--function to format the copyright string correctly
        
        /// ADDED by Engineer B.Pourtavakoli on 1402/09/16
        '''
        start_persian, end_persian, start_gregorian, end_gregorian = self.get_year_range(text)
        return (f"Copyright © {start_persian}-{end_persian} ({start_gregorian}-{end_gregorian}) by B.S.D Group™")

    def SmartCopyrightUpdater(self):
        '''
        /// SmartCopyrightUpdater()--function to update copyright as a smart thinker.
        
        /// ADDED by Engineer B.Pourtavakoli on 1402/09/16
        '''
        # Example input
        strLines = [
            "Copyright © 1380-1391 by B.S.D Group™",
            "Copyright© 1380-1400,2001-2021 by B.S.D Group™",
            "Copyright © 1395,2016 by B.S.D Group™",
            "Copyright© 1395,2016 by B.S.D Group™",
            "Copyright © 1395,2016 by B.S.D Group™",
            "Copyright© 2016 by B.S.D Group™",
            "Copyright © 2016 by B.S.D Group™",
            "Copyright© 1395 by B.S.D Group™",
            "Copyright © 1380,2001 by B.S.D Group™",

            "Copyright© 1380-1398,2001-2019 by B.S.D Group™",
            "Copyright© 1400,2021 by B.S.D Group™",
            "Copyright© 1402,2023 by B.S.D Group™",
            "Copyright  © 1380-1393,2001-2015 by B.S.D Group™",
            "Copyright© 1402,2024 by B.S.D Group™",
            "Copyright© 1403,2024 by B.S.D Group™"
        ]

        # Process and print the output
        for line in strLines:
            print(self.format_copyright(line))


    def Search_and_Modify_Files(self, directory, patterns):
        modified_files = []
        total_files = 0
        searched_files = 0
        
        # جستجوی فایل‌ها بر اساس الگو
        for pattern in patterns:
            matched_files = glob.glob(os.path.join(directory, '**', pattern), recursive=True)
            searched_files += len(matched_files)
            
            for file in matched_files:
                total_files += 1
                
                # فرض کنیم که اگر فایل با الگو تطابق داشت، نیاز به اصلاح دارد
                # در اینجا اصلاحات دلخواه خود را اعمال می‌کنید
                
                modified_files.append(file)
                
                # در اینجا می‌توانید کدی برای اصلاح محتویات فایل اضافه کنید
                # به عنوان مثال باز کردن فایل، تغییر محتویات آن، و ذخیره‌سازی مجدد
                
        # چاپ گزارش
        print(f"Total files: {total_files}")
        print(f"Searched files (based on pattern): {searched_files}")
        print(f"Modified files: {len(modified_files)}")
        
        return (modified_files)

# **********************************************************************************************************
# endregion

# region Main program
# **********************************************************************************************************
'''
///*********************************************************************************************************
///* Main program
///*********************************************************************************************************
'''
def WinMain():
    '''
    /// WinMain()--Main program, contains main statements and calling functions
    
    /// ADDED by engineer B.Pourtavakoli on 1403/09/16
    '''
    intStartTime = time.time()
    
    clsMClass = MainClass()
    clsMClass.ClearScreen()
    
    # clsMClass.SmartCopyrightUpdater()

    directory = "M:/Artificial Intelligence (A.I)/Project(s)"
    patterns = ['*.sln', '*.cs', '*.resx', '*.Designer.*', '*.settings']
    modified_files = clsMClass.Search_and_Modify_Files(directory, patterns)

    # نمایش فایل‌های اصلاح شده
    print("\nModified Files:")
    for file in modified_files:
        print(file)
    
    # clsMClass.About()

    # intEndTime = time.time()
    # intElapsedTime = intEndTime - intStartTime
    # print("Elapsed time: %s ms" % round(intElapsedTime, 3), end=NEWLINE+NEWLINE)
    
    # print("Press the Enter key to continue...", end='')
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
/// ADDED by Engineer B.Pourtavakoli on 1403/09/16
'''
if (__name__ == "__main__"):
    WinMain()
# **********************************************************************************************************
# endregion
