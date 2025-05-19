import os
from itertools import cycle

class Class:
    def __iter__(self):
        print("iter called")
        yield from range(3)

if (os.name == "nt"):
    _ = os.system("cls")

iterator = cycle(Class())

for number in iterator:
    print(number)
