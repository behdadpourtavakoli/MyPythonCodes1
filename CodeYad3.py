import os, time
from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#'''

######################################################
######## Source 21 on 1403/09/03 #            ########
######################################################

######################################################
if (os.name == "nt"):
    _ = os.system("cls")


try:
    driver_path = "D:\\Project(s)\\Python\\chromedriver_py-131.0.6778.85\\chromedriver_py\\chromedriver.exe"

    # تنظیم ChromeDriver با استفاده از Service
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)

    # # باز کردن صفحه وب
    # driver.get("https://www.instagram.com/accounts/login/")
    # print("Page Title:", driver.title)

    # # بستن مرورگر
    # driver.quit()

    # driver = webdriver.Chrome()
    # driver.get("https://www.instagram.com/accounts/login/")
    # time.sleep(3)

    # strUsername = "behdad_p"
    # strPssword = "James198181."
    # username_input = driver.find_element(By.NAME, strUsername)
    # password_input = driver.find_element(By.NAME, strPssword)
    # username_input.send_keys(strUsername)
    # password_input.send_keys(strPssword)
    # password_input.send_keys(Keys.RETURN)

    # time.sleep(5)

    # if ("challenge" in driver.current_url):
    #     print("نیاز به تأیید بیشتر: Challenge Required")
    # else:
    #     print("ورود موفق!")

    # # دریافت اطلاعات کاربری
    # driver.get("https://www.instagram.com/your_username/")
    # time.sleep(3)
    # profile_name = driver.find_element(By.CLASS_NAME, "_aacl").text
    # print(f"نام پروفایل: {profile_name}")
    # driver.quit()
except Exception as e:
    print(f"Error occurred: {e}")

exit(0)

######################################################
######## Source 21 on 1403/09/03 #2  FAIL     ########
######################################################

######################################################
if (os.name == "nt"):
    _ = os.system("cls")

try:
    shutil.rmtree("config", ignore_errors=True)

    bot = Bot()
    bot.delay = 5
    strUsername = "behdad_p"
    strPssword = "James198181."
    bot.login(username=strUsername, password=strPssword)

    if bot.user_id:
        print(f"Login successfully! account: {bot.user_id}")
    else:
        print("Unable to login.")

    bot.logout()
    if os.path.exists("config"):
        os.rmdir("config")

    user_info = bot.get_user_info(bot.user_id)
    print("Account Info:", user_info)
except Exception as e:
    print()
    print(f"Error occurred: {e}")

exit(0)

######################################################
######## Source 21 on 1403/09/03 #1           ########
######################################################

######################################################
if (os.name == "nt"):
    _ = os.system("cls")

ilInstagram = instaloader.Instaloader()
ilInstagram.context.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
ilInstagram.save_session_to_file()

strUsername = "behdad_p"
strPssword = "James198181."
ilInstagram.login(strUsername, strPssword)

ilProfile = instaloader.Profile.from_username(ilInstagram.context, strUsername)
# ilProfile = instaloader.Profile.from_username(ilInstagram.context, 'amir_codeyad')
print(ilProfile.followers)
print(ilProfile.followees)

exit(0)

######################################################
######## Source 20 on 1403/09/03              ########
######################################################

######################################################
if (os.name == "nt"):
    _ = os.system("cls")

print(__name__)

exit(0)
#'''

######################################################
######## Source 19 on 1403/09/03              ########
######################################################

def fib(limit):
    a, b = 0, 1
    fibs = []
    while (len(fibs) < limit):
        yield a
        fibs.append(a)
        
        a, b = b, a + b
        # a = b
        # b = a + b
    return (fibs)

######################################################
if (os.name == "nt"):
    _ = os.system("cls")

x = fib(10)
strTemp = ""
for value in x:
    strTemp = strTemp + f"{value}, "
    # print(strTemp[:-2])

# strTemp = strTemp[:-2]
print(strTemp[:-2])

exit(0)

######################################################
######## Source 18 on 1403/09/03              ########
######################################################

def fib(limit):
    a, b = 0, 1
    while (a < limit):
        yield a
        # a, b = b, a + b
        a = b
        b = a + b

######################################################
if (os.name == "nt"):
    _ = os.system("cls")

x = fib(4000)
strTemp = ""
for value in x:
    strTemp = strTemp + f"{value}, "

# strTemp = strTemp[:-2]
print(strTemp[:-2])

exit(0)

######################################################
######## Source 17 on 1403/09/03              ########
######################################################

def simpleGenerator():
    yield 1
    yield 2
    yield 3
    yield "Behdad Pourtavakoli"

######################################################
if (os.name == "nt"):
    _ = os.system("cls")

for value in simpleGenerator():
    print(value)

exit(0)

######################################################
######## Source 16 on 1403/09/03              ########
######################################################

class Teacher():
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return (f"Hi {self.name}!")

    def __repr__(self) -> str:
        return (self.name)

######################################################
if (os.name == "nt"):
    _ = os.system("cls")

t = Teacher("Behdad")
print(t)
# print(str(t))
# print(repr(t))

exit(0)

######################################################
######## Source 15 on 1403/09/03              ########
######################################################

class clsDeutschland():
    def capital():
        print("The Berlin is Deutschland capital.")

    def language():
        print("Deutschland language is Deutsch.")

class clsUSA():
    def capital():
        print("The Washington, D.C. is USA capital.")

    def language():
        print("English is the primary USA language.")

######################################################
if (os.name == "nt"):
    _ = os.system("cls")

obj_Deutschland = clsDeutschland
obj_USA = clsUSA
countries = (obj_Deutschland, obj_USA)
for country in countries:
    country.capital()
    country.language()

exit(0)

######################################################
######## Source 14 on 1403/09/03              ########
######################################################

class clsAnimal(ABC):
    
    @abstractmethod
    def move(self):
        # print("Animal is moving!")
        pass

    @property
    @abstractmethod
    def legs(self):
        pass

class clsLion(clsAnimal):
    def move(self):
        print("Lion is moving!")

    @property
    def legs(self):
        return (4)

class clsDog(clsAnimal):
    def move(self):
        print("Dog is moving!")

    @property
    def legs(self):
        return (2)

######################################################
if (os.name == "nt"):
    _ = os.system("cls")

clsL = clsLion()
clsD = clsDog()

clsL.move()
print(f"{clsL.legs}")

clsD.move()
print(f"{clsD.legs}")

exit(0)

######################################################
######## Source 13 on 1403/09/03 #3           ########
######################################################

class Person():
    def __init__(self) -> None:
        self.bp = "Behdad Pourtavakoli"
        self._hh = "Hilda Haghdoust"
        self.__hp = "Hila Pourtavakoli"
        self.__age = 42

    @property
    def age(self):
        return (self.__age)

    @age.setter
    def age(self, value):
        if (value >= 50):
            # raise ValueError("When you reach fifty, the plague comes to several places.")
            print("When you reach fifty, the plague comes to several places.")
        self.__age = value

    @age.deleter
    def age(self):
        del self.__age

######################################################
if (os.name == "nt"):
    _ = os.system("cls")

clsP = Person()
print(clsP.age)

clsP.age = 50
print(clsP.age)

exit(0)

######################################################
######## Source 12 on 1403/09/03 #2           ########
######################################################
class Person():
    def __init__(self) -> None:
        self.bp = "Behdad Pourtavakoli"
        self._hh = "Hilda Haghdoust"
        self.__hp = "Hila Pourtavakoli"
        self.__age = 42

    def get_age(self):
        return (self.__age)

    def set_age(self, value):
        self.__age = value

    def del_age(self):
        del self.__age

    age = property(get_age, set_age, del_age)

######################################################
if (os.name == "nt"):
    _ = os.system("cls")

clsP = Person()
# print(clsP.get_age())
print(clsP.age)

# clsP.set_age(43)
# print(clsP.get_age())
clsP.age = 43
print(clsP.age)

# del clsP.age
# print(clsP.age)

exit(0)

######################################################
######## Source 11 on 1403/09/03 #1           ########
######################################################

class Person():
    def __init__(self) -> None:
        self.bp = "Behdad Pourtavakoli"
        self._hh = "Hilda Haghdoust"
        self.__hp = "Hila Pourtavakoli"
        self.__age = 42

    def get_age(self):
        return (self.__age)

    def set_age(self, value):
        self.__age = value

######################################################
if (os.name == "nt"):
    _ = os.system("cls")

clsP = Person()
print(clsP.get_age())

clsP.set_age(43)
print(clsP.get_age())

exit(0)

######################################################
######## Source 10 on 1403/09/03              ########
######################################################

class Person:
    def __init__(self):
        self.bp = 2        # Public variable
        self._bp2 = "002"  # Protected variable
        self.__bp3 = "BHH" # Private variable
    
    def return_protect(self):
        return (self.__bp3)

    def change_protect(self):
        self.__bp3 = "H B H"

class Child(Person):
    def __init__(self):
        super().__init__()
        self._bp2 = "Hila"

######################################################
if (os.name == "nt"):
    _ = os.system("cls")

clsP = Person()
print(clsP.bp, clsP._bp2, clsP.return_protect())

clsP.bp = 258414
clsP._bp2 = "Hilda"
print(clsP.bp, clsP._bp2, clsP.return_protect())

clsP2 = Child()
clsP2._bp2 = "Hilda & Hila"
print(clsP2.bp, clsP2._bp2, clsP2.return_protect())

clsP.change_protect()
print(clsP.bp, clsP._bp2, clsP.return_protect())

exit(0)

######################################################
######## Source 9 on 1403/09/03               ########
######################################################

def MOP1_decorator(func):
    def wrapper(*args, **kwargs):
        x = func(*args, **kwargs)
        return (x * 3)
    return (wrapper)

def MOP2_decorator(func):
    def wrapper(*args, **kwargs):
        x = func(*args, **kwargs)
        return (x * 10)
    return (wrapper)

@MOP1_decorator
@MOP2_decorator
def test(num):
    return (num)

######################################################
if (os.name == "nt"):
    _ = os.system("cls")

print(test(5))

exit(0)

######################################################
######## Source 8 on 1403/09/03               ########
######################################################

def ETA_decorator(func):
    def wrapper(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Total time is {end - begin:.6f}")
    return (wrapper)

@ETA_decorator
def test(name):
    time.sleep(0.010)
    print (f"Hello {name}")
    time.sleep(0.010)

######################################################
if (os.name == "nt"):
    _ = os.system("cls")

test("Behdad Pourtavakoli")

exit(0)

######################################################
######## Source 7 on 1403/09/03               ########
######################################################

def UpperCase_Decorator(func):
    def inner_wrapper(*args, **kwargs):
        x = func(*args, **kwargs)
        return (x.upper())
    return (inner_wrapper)

def LowerCase_Decorator(func):
    def inner_wrapper(*args, **kwargs):
        x = func(*args, **kwargs)
        return (x.lower())
    return (inner_wrapper)

@LowerCase_Decorator
@UpperCase_Decorator
def test(name):
    return (f"{name}")

######################################################
if (os.name == "nt"):
    _ = os.system("cls")

# print(test("Behdad Pourtavakoli"))
x = test("Behdad Pourtavakoli")
print(x)

exit(0)

######################################################
######## Source 6 on 1403/09/02               ########
######################################################

def hello_decorator(func):
    
    def inner(*args, **kwargs):
        print("Something execute before decorator.")
        func(*args, **kwargs)
        print("Something execute after decorator.")
        
    return (inner)
######################################################
if (os.name == "nt"):
    _ = os.system("cls")

@hello_decorator
def hello(name, family):
    print(f"Hello {name} {family}.")

hello('Behdad', 'Pourtavakoli')

exit(0)

######################################################
######## Source 5 on 1403/09/02               ########
######################################################

def hello_decorator(func):
    
    def inner(name):
        print("Something execute before decorator.")
        func(name)
        print("Something execute after decorator.")
        
    return (inner)
######################################################
if (os.name == "nt"):
    _ = os.system("cls")

@hello_decorator
def hello(name):
    print(f"Hello {name}.")

hello()

exit(0)

######################################################
######## Source 4 on 1403/09/02               ########
######################################################

def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return (func(a, b))
    return (inner)

@smart_divide
def divide(a, b):
    print(a/b)
######################################################
if (os.name == "nt"):
    _ = os.system("cls")

divide(2,5)
divide(2,0)

exit(0)

######################################################
######## Source 3 on 1403/09/02               ########
######################################################

class ModelMeta(type):
    def __new__(cls, name, bases, dct):
        def save(self):
            print(f"Saving {self.__class__.__name__} to the database...")
        
        def delete(self):
            print(f"Deleting {self.__class__.__name__} from the database...")
        
        dct['save'] = save
        dct['delete'] = delete
        
        return super().__new__(cls, name, bases, dct)

class BaseModel(metaclass=ModelMeta):
    pass
######################################################
class User(BaseModel):
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Product(BaseModel):
    def __init__(self, title, price):
        self.title = title
        self.price = price

if (os.name == "nt"):
    _ = os.system("cls")

user = User("Alice", 30)
product = Product("Laptop", 1500)

user.save()
product.save()

user.delete()
product.delete()

exit(0)

######################################################
######## Source 2 on 1403/09/02               ########
######################################################

class MyMeta(type):
    def __new__(cls, name, bases, dct):
        dct['added_attribute'] = 'This is added by the metaclass'
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
    pass
######################################################
if (os.name == "nt"):
    _ = os.system("cls")

obj = MyClass()
print(obj.added_attribute)

exit(0)

######################################################
######## Source 1 on 1403/09/02               ########
######################################################

def karl(self, myName):
    print("RAY, " + myName)
######################################################
if (os.name == "nt"):
    _ = os.system("cls")

MyList = type('MyList', (list,), dict(x=62, karl=karl))

ml = MyList()
ml.append("Mango")
print("1) ", ml)
print()

print("2) ", ml.x)
print()

ml.karl("KARLOS")
print("3) ", ml.__class__.__class__)
