import os, random, time, pythoncom
from alive_progress import alive_bar
from tqdm import tqdm
from progressbar import Bar
# from progress.bar import (PixelBar, ShadyBar)
from progress.spinner import (MoonSpinner, PixelSpinner) #, Spinner, PieSpinner, LineSpinner)
from time import sleep

intMAX = int(9e6)
intMax = 50
intTyp = 1
intSek = 10
fltWait = 0.005

def WirdGeladen3(intMax = 100, intTyp = 1, intSek = 10):
    '''
    /// WirdGeladen3()-Funktion um das Warten etwas zu verkürzen.
    /// Parameter:
    /// intMax = Maximale Länge des Fortschrittsbalkens, Standardwert: 100
    /// intTyp = Art des Fortschrittsbalkens, Standardwert: 1
    /// intSec = maximale Wartezeit in Sekunden, Standardwert: 10 Sekunden
    /// HINZUFÜGEN von Ingenieur B.Pourtavakoli im 1403/06/18
    '''
    for i in tqdm(range(intMax)):
          sleep(0.01)

def simulate_progress(style_name, bar_format=None):
    print(f"Style: {style_name}")
    for _ in tqdm(range(intMax), desc=style_name, bar_format=bar_format, ncols=80):
        sleep(fltWait)
    print()

if (os.name == "nt"):
    _ = os.system("cls")

# Good on 1403/09/17
with alive_bar(intMax * 2, title="Processing") as bar:
    for _ in range(intMax * 2):
        sleep(fltWait * 5)
        bar()

# Very Good on 1403/09/17
with alive_bar(intMax, title="Custom Progress", spinner="dots_waves", bar="smooth") as bar:
    for _ in range(intMax):
        sleep(fltWait * 5)
        bar()
# exit(0)

tasks = [("Task 1", 50), ("Task 2", 70), ("Task 3", 100)]

for task, steps in tasks:
    with alive_bar(steps, title=task) as bar:
        for _ in range(steps):
            sleep(fltWait)
            bar()

simulate_progress("classic")
simulate_progress("classic2", "{l_bar}{bar}| {n_fmt}/{total_fmt}")
simulate_progress("smooth", "{l_bar}{bar:30}{r_bar}")
simulate_progress("blocks", "{l_bar}█{bar}█{r_bar}")
simulate_progress("bubbles", "{l_bar}⚪{bar:30}⚪{r_bar}")
simulate_progress("hollow", "{l_bar}[{bar:20}]| {n_fmt}/{total_fmt}")
simulate_progress("solid", "{l_bar}█{bar:30}█{r_bar}")
simulate_progress("circles", "{l_bar}⭕{bar:30}⭕{r_bar}")
simulate_progress("squares", "{l_bar}■{bar:20}■{r_bar}")
simulate_progress("checks", "{l_bar}✔{bar:30}✔{r_bar}")
simulate_progress("filling", "{l_bar}{bar:30}| {n_fmt}/{total_fmt}")
# exit(0)

# Good
suffix = '%(percent)d%% [%(elapsed_td)s / %(eta)d / %(eta_td)s]'
with PixelSpinner('Processing...', suffix=suffix) as bar:
    for i in range(intMax):
        # Etwas tun.
        intSleep = (random.randint(1, intSek)) / 100
        time.sleep(intSleep)
        pythoncom.PumpWaitingMessages()
        bar.next()
print()

# Good
with alive_bar(intMax, bar = 'classic', spinner = 'notes') as bar1:
    for i in range(intMax):
         sleep(fltWait)
         bar1()
print()

# Good
for i in tqdm(range(intMax), desc="Classic2", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}"):
    sleep(fltWait)
print()

# Good
for i in tqdm(range(intMax), desc="Smooth", bar_format="{l_bar}{bar:80}{r_bar}"):
    sleep(fltWait)
print()


for i in tqdm(range(intMax), desc="Blocks"):
    sleep(fltWait)
print()

bubble_bar = '{l_bar}{bar}| {n_fmt}/{total_fmt}'
for i in tqdm(range(intMax), desc="Bubbles", bar_format=bubble_bar, ncols=80):
    sleep(fltWait * 5)
print()

# Replace the default '█' with 'o'
bar_format = "{l_bar}{bar}| {n_fmt}/{total_fmt}"
with tqdm(total=intMax, desc="Bubbles", bar_format=bar_format) as progress_bar:
    for i in range(intMax):
        progress_bar.bar = lambda: 'o' * (progress_bar.n // 2)
        progress_bar.update(1)
        sleep(fltWait * 5)
print()

with MoonSpinner('Processing…') as bar:
    for intLoop in range(intMax):
        # Etwas tun.
        intSleep = (random.randint(1, intSek)) / 100
        sleep(intSleep)
        pythoncom.PumpWaitingMessages()
        bar.next()
print()

for i in tqdm(range(intMax)):
    # Etwas tun.
    intSleep = (random.randint(1, intSek)) / 150
    time.sleep(intSleep)
    pythoncom.PumpWaitingMessages()
print()

for i in tqdm(range(intMax), ncols=62):
    # Etwas tun.
    intSleep = (random.randint(1, intSek)) / 150
    time.sleep(intSleep)
    pythoncom.PumpWaitingMessages()
print()
    
for i in tqdm(range(intMax), ascii=True, desc="Progress:"):
    # Etwas tun.
    intSleep = (random.randint(1, intSek)) / 150
    time.sleep(intSleep)
    pythoncom.PumpWaitingMessages()
print()
