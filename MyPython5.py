# region Copyright
# **********************************************************************************************************
'''
///*-=============================================================================================-*
/// File name             : BSD Group Standard Python Source 1403-2025 En.py
/// Version               : 1.0.0.0
/// Start                 : 2024-11-27 (1403/09/07)
/// Last update           : 2024-11-27 (1403/09/07)
/// Autor                 : Engineer Behdad Pourtavakoli
/// Trademark             : Behdad Software Developers Group™
/// ----------------------------------------------------------------------------------------------
/// Copyright © 1380-1403 (2001-2025) by B.S.D Group™
/// All rights reserved.
/// ----------------------------------------------------------------------------------------------
///
/// Description: 
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

import os, platform, time
from pathlib import Path

import drawangle_module as dam

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

class MainClass():
    def ClearScreen(self):
        '''
        /// ClearScreen()--function to clear the output screen
        
        /// ADDED by engineer B.Pourtavakoli on 1403/09/07
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
        
        /// ADDED by Engineer B.Pourtavakoli on 1403/09/07
        
        /// UPDATE by Engineer B.Pourtavakoli on 1403/09/07
        '''
        strVersionVersionsnummer = str(platform.python_version())
        strNachricht = "Behdad Software Developers Group™ Presents\n\n"
        
        strNachricht += "Welcome to the B.S.D Group™ Production\n\n"
        
        strNachricht += "Copyright © 1380-1403 (2001-2025) by B.S.D Group™\n"
        strNachricht += "All rights reserved.\n\n"
        
        strNachricht += "Design and develop by Engineer Behdad Pourtavakoli\n\n"
        strNachricht += Path(__file__).name + " (Python v" + strVersionVersionsnummer + ") - ®B.S.D Group™"
        print(strNachricht)

    def Drawing(self):
        '''
        /// Drawing()--function to draw a Rhombus / Diamond (Raute)
        
        /// Square, Rectangle, Triangle, Circle, Oval, Rhombus/Diamond, Pentagon, Hexagon
        
        /// Quadrat, Rechteck, Dreieck, Kreis, Oval, Raute/Diamant, Fünfeck, Sechseck
        
        /// ADDED by Engineer B.Pourtavakoli on 1403/09/07
        '''
        intMaxLength = 7
        chrDraw = 'O'
        chrSpace = ' '
        chrEndSpace = ' '
        
        # # 1: Draw the left side top of the Triangle
        # dam.DrawTriangle(1, intMaxLength, chrDraw, chrSpace, chrEndSpace)

        # # 2: Draw the right side top of the Triangle
        # dam.DrawTriangle(2, intMaxLength, chrDraw, chrSpace, chrEndSpace)

        # # 3: Draw the left side bottom of the Triangle
        # dam.DrawTriangle(3, intMaxLength, chrDraw, chrSpace, chrEndSpace)

        # # 4: Draw the right side bottom of the Triangle
        # dam.DrawTriangle(4, intMaxLength, chrDraw, chrSpace, chrEndSpace)

        # 5: Draw top side of Rhombus/Diamond
        dam.DrawInvertedDiamond(intMaxLength, chrDraw, chrSpace, chrEndSpace)

        chrDraw = '@'
        # 6: Draw top side of Rhombus/Diamond
        dam.DrawDiamond(intMaxLength, chrDraw, chrSpace, chrEndSpace)

        print()


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
    
    /// ADDED by engineer B.Pourtavakoli on 1403/09/07
    '''
    intStartTime = time.time()
    
    # print(Path(__file__).resolve().parent.parent)
    # exit(0)
    
    clsMClass = MainClass()
    clsMClass.ClearScreen()
    
    clsMClass.Drawing()
    exit(0)
    
    print("Enter Enter key to continue...", end='')
    input()
    print()
    
    clsMClass.About()

    intEndTime = time.time()
    intElapsedTime = intEndTime - intStartTime
    print("Elapsed time: %s ms" % round(intElapsedTime, 3), end=NEWLINE+NEWLINE)
    
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
/// ADDED by Engineer B.Pourtavakoli on 1403/09/07
'''
if (__name__ == "__main__"):
    WinMain()
# **********************************************************************************************************
# endregion
