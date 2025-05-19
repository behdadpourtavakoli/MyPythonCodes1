# region Copyright
# **********************************************************************************************************
'''
///*-=============================================================================================-*
/// File name             : ETACalculator.py
/// Version               : 1.0.0.0
/// Start                 : 2024-11-19 (1403/08/29)
/// Last update           : 2024-11-19 (1403/08/29)
/// Autor                 : Engineer Behdad Pourtavakoli
/// Trademark             : Behdad Software Developers Group™
/// ----------------------------------------------------------------------------------------------
/// Copyright © 1380-1403 (2001-2024) by B.S.D Group™
/// All rights reserved.
/// ----------------------------------------------------------------------------------------------
///
/// Description: Prepare a ETA calculator.
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
import os
import time, random

# **********************************************************************************************************
# endregion

# region clsETACalculator()--base class
# **********************************************************************************************************
'''
/// clsETACalculator()--base class
/// ADDED by engineer B.Pourtavakoli on 1403/08/29
'''
class clsETACalculator:
    def ClearScreen(self):
        """
         ClearScreen()--function to clear output screen

         ADDED by engineer B.Pourtavakoli on 1403/06/31
        """
        if (os.name == "nt"):
            _ = os.system("cls")

    def ETA_Calculator(self, total_iterations = 800):
        """
        ETA_Calculator()--function to prepare ETA calculator

        ADDED by engineer B.Pourtavakoli on 1403/08/29

        Parameters:
        total_iterations (int): default 800 times
        """

        try:
            print()
            total_iterations = 800
            base_delay = 0.01
            start_time = time.time()

            for i in range(1, total_iterations + 1):
                progressive_delay = base_delay * (1 + i / total_iterations)
                random_jump = random.choice([1, 5]) if random.random() < 0.1 else 1
                delay = progressive_delay * random_jump

                time.sleep(delay)

                elapsed_time = time.time() - start_time
                avg_time_per_iteration = elapsed_time / i
                remaining_time = avg_time_per_iteration * (total_iterations - i)
                estimated_total_time = avg_time_per_iteration * total_iterations
                
                print(f"\rIteration: {i}/{total_iterations} Elapsed Time: {elapsed_time:.2f}s | "
                    f"Remaining Time: {remaining_time:.2f}s | ETA: {estimated_total_time:.2f}s", end="", flush=True)
            print()
        except KeyboardInterrupt:
            print("")
        
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
/// ADDED by engineer B.Pourtavakoli on 1403/08/29
'''
def WinMain():
    # region clsETACalculator section
    # **********************************************************************************************************
    clsETACalc = clsETACalculator()
    clsETACalc.ClearScreen()
    clsETACalc.ETA_Calculator()

    # print("Press Enter key to exit...", end='')
    # input()
    # **********************************************************************************************************
    # endregion

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
