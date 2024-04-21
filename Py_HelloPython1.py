import os
#import msvcrt
#import win32gui, win32con
#import pythoncom

#hwnd = win32gui.GetForegroundWindow()
#win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

print("Willkommen bei Python in Visual Studio Code (Welcome to the Python in Visual Studio Code)\n")

intSize = os.get_terminal_size()
print("Aktuelle Breite:" , intSize.columns, " - Aktuelle Höhe: ", intSize.lines)
input("Drücken Sie die ENTER-Taste, um fortzufahren...")

intSize = os.get_terminal_size()
print("Aktuelle Breite:" , intSize.columns, " - Aktuelle Höhe: ", intSize.lines)
input("Drücken Sie die ENTER-Taste, um fortzufahren...")

intSize = os.get_terminal_size()
print("Aktuelle Breite:" , intSize.columns, " - Aktuelle Höhe: ", intSize.lines)
input("Zum Beenden drücken Sie die ENTER-Taste...")

print("Zum Verlassen eine beliebige Taste druecken (Press ANY key to exit):", end='')
#pythoncom.PumpWaitingMessages()
#key = msvcrt.getch()
key = input()
#print('\033[3A')
#print('\033[2A')
#print('\033[2F')
