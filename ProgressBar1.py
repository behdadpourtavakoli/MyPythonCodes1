#!/usr/bin/env python
import random, time, pythoncom
#from __future__ import print_function
from progress.bar import (Bar, ChargingBar, FillingSquaresBar, FillingCirclesBar, IncrementalBar, PixelBar, ShadyBar)
from progress.spinner import (Spinner, PieSpinner, MoonSpinner, LineSpinner, PixelSpinner)
from progress.counter import Counter, Countdown, Stack, Pie
from progress.colors import bold

MAX = 100

def sleep2():
    t = 0.01
    t += t * random.uniform(-0.1, 0.1)  # Add some variance
    time.sleep(t)
    pythoncom.PumpWaitingMessages()

def sleep(intSek = 10):
    # Etwas tun.
    intSleep = (random.randint(1, intSek)) / 100
    time.sleep(intSleep)
    pythoncom.PumpWaitingMessages()

print("Progress Bar: Bar, ChargingBar, FillingSquaresBar, FillingCirclesBar")
for bar_cls in (Bar, ChargingBar, FillingSquaresBar, FillingCirclesBar):
    suffix = '%(index)d/%(max)d [%(elapsed)d / %(eta)d / %(eta_td)s] (%(iter_value)s)'
    bar = bar_cls(bar_cls.__name__, suffix=suffix)
    for i in bar.iter(range(MAX)):
        sleep()

# *Beste Wahl*
print("\nProgress Bar: IncrementalBar, PixelBar, ShadyBar")
for bar_cls in (IncrementalBar, PixelBar, ShadyBar):
    suffix = '%(percent)d%% [%(elapsed_td)s / %(eta)d / %(eta_td)s]'
    with bar_cls(bar_cls.__name__, suffix=suffix, max=MAX) as bar:
        for i in range(MAX):
            bar.next()
            sleep()

print("\nProgress Bar: Colored IncrementalBar")
bar = IncrementalBar(bold('Colored'), color='green')
for i in bar.iter(range(MAX)):
    sleep()

print("\nProgress Bar: Spinner, PieSpinner, MoonSpinner, LineSpinner, PixelSpinner")
for spin in (Spinner, PieSpinner, MoonSpinner, LineSpinner, PixelSpinner):
    for i in spin(spin.__name__ + ' %(index)d ').iter(range(MAX)):
        sleep()

print("\nProgress Bar: Counter, Countdown, Stack, Pie")
for singleton in (Counter, Countdown, Stack, Pie):
    for i in singleton(singleton.__name__ + ' ').iter(range(MAX)):
        sleep()

print("\nProgress Bar: Random IncrementalBar")
bar = IncrementalBar('Random', suffix='%(index)d')
for i in range(MAX):
    bar.goto(random.randint(0, MAX))
    sleep()
bar.finish()
