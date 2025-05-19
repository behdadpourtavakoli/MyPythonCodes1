# region Copyright
# **********************************************************************************************************
'''
///*-=============================================================================================-*
/// File name             : drawangle_module.py
/// Version               : 1.0.0.0
/// Start                 : 2024-11-27 (1403/09/07)
/// Last update           : 2024-11-27 (1403/09/07)
/// Autor                 : Engineer Behdad Pourtavakoli
/// Trademark             : Behdad Software Developers Group™
/// ----------------------------------------------------------------------------------------------
/// Copyright © 1380-1403 (2001-2024) by B.S.D Group™
/// All rights reserved.
/// ----------------------------------------------------------------------------------------------
///
/// Description: drawing triangle and diamond
///
/// ----------------------------------------------------------------------------------------------
/// The developer's word: Do not forget the engineer Behdad Pourtavakoli.
///-=============================================================================================-*///
'''
# **********************************************************************************************************
# endregion

# region Handwritten functions and procedures
# **********************************************************************************************************
'''
///*********************************************************************************************************
///* Handwritten functions and procedures
///*********************************************************************************************************
'''

def DrawTriangle(intMode, intMaxLength, chrDraw, chrSpace, chrEndSpace):
    '''
    /// DrawTriangle()--function to draw a customized Rhombus/Diamond (Raute/Diamant)

    /// Parameters:
    
    /// intMod: set triangle angle corner: 1: Top Left, 2: Top Right, 3: Bottom Left, 4: Bottom Right
    
    /// intMaxLength: maximum length of diamon, default: 10
            
    /// chrDraw: character to draw diamond, default: '*'
            
    /// chrSpace: space character, default: ' '
            
    /// chrEndSpace: end character, default: ' '
            
    /// ADDED by Engineer B.Pourtavakoli on 1403/09/07
    '''
    if (intMode == 1):
        # 1: Draw the left side top of the Triangle
        if (intMaxLength <= 2):
            return

        for i in range(intMaxLength, 0, -1):
            for k in range(intMaxLength + 1, i, -1):
                print(chrDraw, end=chrEndSpace)
            print()
    elif (intMode == 2):
        # 2: Draw the right side top of the Triangle
        if (intMaxLength <= 2):
            return

        for i in range(intMaxLength, 0, -1):
            for j in range(0, i, 1):
                print(chrSpace, end=chrEndSpace)

            for k in range(intMaxLength + 1, i, -1):
                print(chrDraw, end=chrEndSpace)
            print()
    elif (intMode == 3):
        # 3: Draw the left side bottom of the Triangle
        for i in range(0, intMaxLength + 1, 1):
            for k in range(intMaxLength + 1, i, -1):
                print(chrDraw, end=chrEndSpace)
            print()
    elif (intMode == 4):
        # 4: Draw the right side bottom of the Triangle
        for i in range(0, intMaxLength + 1, 1):
            for j in range(0, i, 1):
                print(chrSpace, end=chrEndSpace)

            for k in range(intMaxLength + 1, i, -1):
                print(chrDraw, end=chrEndSpace)
            print()

    if (intMode in [1, 2, 3, 4]):
        print()

def DrawInvertedDiamond(intMaxLength, chrDraw, chrSpace, chrEndSpace):
    '''
    /// DrawInvertedDiamond()--function to draw a customized Rhombus/Diamond (Raute/Diamant)

    /// Parameters:
    
    /// intMaxLength: maximum length of inverted diamon, default: 10
            
    /// chrDraw: character to draw inverted diamond, default: '*'
            
    /// chrSpace: space character, default: ' '
            
    /// chrEndSpace: end character, default: ' '
            
    /// ADDED by Engineer B.Pourtavakoli on 1403/09/07
    '''
    # 5-1: Draw top side of Rhombus/Diamond
    for i in range(intMaxLength, 0, -1):
        for j in range(0, i, 1):
            print(chrSpace, end=chrEndSpace)

        for k in range(intMaxLength + 1, i, -1):
            print(chrDraw, end=chrEndSpace)

        for k in range(i, intMaxLength, 1):
            print(chrDraw, end=chrEndSpace)
        print()

    # 5-2: Draw bottom side of Rhombus/Diamond
    for i in range(0, intMaxLength + 1, 1):
        for j in range(0, i, 1):
            print(chrSpace, end=chrEndSpace)

        for k in range(intMaxLength + 1, i, -1):
            print(chrDraw, end=chrEndSpace)

        for k in range(i, intMaxLength, 1):
            print(chrDraw, end=chrEndSpace)
        print()
    print()

def DrawDiamond(intMaxLength, chrDraw, chrSpace, chrEndSpace):
    '''
    /// DrawDiamond()--function to draw a customized Rhombus/Diamond (Raute/Diamant)

    /// Parameters:
    
    /// intMaxLength: maximum length of diamon, default: 10
            
    /// chrDraw: character to draw diamond, default: '*'
            
    /// chrSpace: space character, default: ' '
            
    /// chrEndSpace: end character, default: ' '
            
    /// ADDED by Engineer B.Pourtavakoli on 1403/09/07
    '''
    if (intMaxLength <= 2):
        return

    for i in range(0, intMaxLength, 1):
        for j in range(intMaxLength, i, -1):
            print(chrDraw, end=chrEndSpace)

        for k in range(0, i, 1):
            print(chrSpace, end=chrEndSpace)

        for l in range(i, 0, -1):
            print(chrSpace, end=chrEndSpace)

        for m in range(i, intMaxLength, 1):
            print(chrDraw, end=chrEndSpace)
        print()

    
    for i in range(intMaxLength - 1, -1, -1):
        for j in range(intMaxLength, i, -1):
            print(chrDraw, end=chrEndSpace)

        for k in range(0, i, 1):
            print(chrSpace, end=chrEndSpace)

        for l in range(i, 0, -1):
            print(chrSpace, end=chrEndSpace)

        for m in range(i, intMaxLength, 1):
            print(chrDraw, end=chrEndSpace)
        print()

    # 6-1: Draw top side of Rhombus/Diamond
    '''for i in range(0, intMaxLength):
        for j in range(intMaxLength, i, -1):
            print(chrDraw, end=chrEndSpace)

        for k in range(0, 2 * i):
            print(chrSpace, end=chrEndSpace)

        for m in range(intMaxLength, i, -1):
            print(chrDraw, end=chrEndSpace)
        print()

    # 6-2: Draw bottom side of Rhombus/Diamond
    for i in range(intMaxLength - 1, -1, -1):
        for j in range(intMaxLength, i, -1):
            print(chrDraw, end=chrEndSpace)

        for k in range(0, 2 * i):
            print(chrSpace, end=chrEndSpace)

        for m in range(intMaxLength, i, -1):
            print(chrDraw, end=chrEndSpace)
        print()'''
    print()

# **********************************************************************************************************
# endregion
