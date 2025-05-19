'''
/// CodeYad31(self)--function to review the Python language by CodeYad.com
/// function decorator
/// Contains CodeYad lessons by video: 114 and https://www.geeksforgeeks.org/decorators-in-python/
/// ADDED by engineer B.Pourtavakoli on 1403/09/01
'''
import os

######################################################
def hello(strName = "Behdad"):
    def hello_behdad():
        print(f"Hi {strName}, You are the Best.")

    return (hello_behdad)

def hello_decorator(func):

    # wrapper
    def inner():
        print("Hi, this is before function execution.")
        func()
        print("this is after function execution.")

    return (inner)

def normal_hello():
    print("Hi Behdad.")
    
######################################################

@hello_decorator
def normal_hello2():
    print("Hi Behdad.")

######################################################

@hello_decorator
def normal_hello3(strMessage):
    return (f"{strMessage}")

######################################################

def decor1(func):
    def inner():
        x = func()
        return (x * x)
    return (inner)

def decor(func):
    def inner():
        x = func()
        return (2 * x)
    return (inner)

@decor1
@decor
def num(): 
    return (10)

@decor
@decor1
def num2():
    return (10)

# print(num())
# print()
# print(num2())

######################################################

if (os.name == "nt"):
    _ = os.system("cls")

print("Test1: ")
newFunc = hello()
newFunc()
print()

print("Test2: ")
newFunc = hello_decorator(normal_hello)
newFunc()
print()

print("Test3: ")
normal_hello2()
# print()
# normal_hello3("Fuck you asshole!") ## It has error / Es liegt ein Fehler vor. {Es hat ein Fehler.}
