from tqdm import tqdm_gui
import time, random, pythoncom

intSek = 15
my_list = [1, 2, 3, 4, 5, 6, 7 , 8]

#print("Progress: ", end='', sep='')
for i in tqdm_gui(my_list):
    print(i, end='', sep='')
    # Etwas tun.
    intSleep = (random.randint(1, intSek)) / 100
    time.sleep(intSleep)
    pythoncom.PumpWaitingMessages()
    print("\b", end='')
print()
    
for i in tqdm_gui(my_list):
    print(i, end='', sep='')
    # Etwas tun.
    intSleep = (random.randint(1, intSek)) / 100
    time.sleep(intSleep)
    pythoncom.PumpWaitingMessages()
    print("\b", end='')
#print()

#progress_bar = [(print(i, end='', sep=''), time.sleep(0.2), print("\b", end='')) for i in tqdm_gui(my_list)]
