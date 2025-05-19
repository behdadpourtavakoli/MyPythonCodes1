# https://t.me/IRPythonGP - Telegram Python Group
# 1403/08/21

# https://t.me/DevelopixPython
print()

lst = list()  
def func(arg: list = lst):  
    arg.append(0)  
    return arg  

print(func())  
print(func())
exit()

# Message 72:
from typing import NamedTuple  

class DevelopixGroup(NamedTuple):  
    username: str
    members: list = []

print("Telegram Python Group: Message 72")  
python_gp = DevelopixGroup("IRPythonGP")  
js_gp = DevelopixGroup("IRJavascriptGP")  

js_gp.members.append("ErfanXD")  
python_gp.members.append("General_alpha")

print(python_gp.members)
print(js_gp.members)
exit()

# Message 73:
from itertools import cycle

class Class:
    def __iter__(self):
        print("iter called")
        yield from range(3)

iterator = cycle(Class())

print("Telegram Python Group: Message 73")  
for number in iterator:
    print(number)
