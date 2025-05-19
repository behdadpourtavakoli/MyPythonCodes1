
# **********************************************************************************************************
'''
/// Other classes: clsStudents, clsCar, clsPersons, clsUsers, ...
/// ADD by engineer B.Pourtavakoli on 1403/08/01
'''

class clsStudents:
    def __init__(self, intStCode, strName, strFamily, intIdCode, strBDate, strEMail = "", strCellphone = ""):
        self.intStCode = intStCode
        self.strName = strName
        self.strFamily = strFamily
        self.intIdCode = intIdCode
        self.strBDate = strBDate
        self.strEMail = strEMail
        self.strCellphone = strCellphone
    
    def StudentInfo(self):
        print(f"Student No: {self.intStCode}, Student Name: {self.strName} {self.strFamily}")
        print(f"Student Identification Code: {self.intIdCode}, Student Birth date: {self.strBDate}")
        print(f"EMail: {self.strEMail}, Cellphone: {self.strCellphone}")

        if self.intStCode:
            print(f"EMail: {self.strEMail}", end=', ')
            
        if self.intStCode:
            print(f"Cellphone: {self.strCellphone}")

class clsCar:
    def __init__(self, model, year, color="Black"):
        self.model = model           # مدل خودرو
        self.year = year             # سال تولید
        self.color = color           # رنگ خودرو
        self.speed = 0               # سرعت خودرو که به صورت پیش‌فرض ۰ است
        self.is_on = False           # وضعیت روشن یا خاموش بودن خودرو

    def start(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.model} started.")
        else:
            print(f"{self.model} is already running.")

    def stop(self):
        if self.is_on:
            self.is_on = False
            self.speed = 0
            print(f"{self.model} stopped.")
        else:
            print(f"{self.model} is already off.")

    def accelerate(self, increase):
        if self.is_on:
            self.speed += increase
            print(f"{self.model} accelerated by {increase} km/h. Current speed: {self.speed} km/h.")
        else:
            print(f"Can't accelerate. {self.model} is off.")

    def brake(self, decrease):
        if self.is_on:
            self.speed = max(0, self.speed - decrease)
            print(f"{self.model} slowed down by {decrease} km/h. Current speed: {self.speed} km/h.")
        else:
            print(f"Can't brake. {self.model} is off.")

    def get_info(self):
        status = "on" if self.is_on else "off"
        return f"Model: {self.model}, Year: {self.year}, Color: {self.color}, Speed: {self.speed} km/h, Status: {status}"

class clsPersons:
    def __init__(self, strName, strFamily, strUId, strBDate, strFather = "", strCellphone = "", strAddress = "", strEMail = ""):
        self.strName = strName
        self.strFamily = strFamily
        self.strUId = strUId
        self.strBDate = strBDate
        self.strFather = strFather
        self.strCellphone = strCellphone
        self.strEMail = strEMail
        self.strAddress = strAddress
    
    def PersonInfo(self):
        print(f"Person Unique ID: {self.strUId}, Person name: {self.strName} {self.strFamily}")
        
        if self.strFather:
            print(f"Father name: {self.strFather}", end=', ')
            
        print(f"Birth date: {self.strBDate}")
        
        if self.strCellphone:
            print(f"Cellphone: {self.strCellphone}")

        if self.strEMail:
            print(f"EMail: {self.strEMail}", end=', ')

        if self.strAddress:
            print(f"Address: {self.strAddress}")

class clsUsers(clsPersons):
    def __init__(self, strName, strFamily, strUId, strBDate, intUserId, strFather="", strCellphone="", strAddress="", strEMail=""):
        super().__init__(strName, strFamily, strUId, strBDate, strFather, strCellphone, strAddress, strEMail)
        self.intUserId = intUserId

    def PersonInfo(self):
        print(f"User IDentification: {self.intUserId}, Person name: {self.strName} {self.strFamily}")
        
        if self.strFather:
            print(f"Father name: {self.strFather}", end=', ')
            
        print(f"Birth date: {self.strBDate}")
        
        if self.strCellphone:
            print(f"Cellphone: {self.strCellphone}")

        if self.strEMail:
            print(f"EMail: {self.strEMail}", end=', ')

        if self.strAddress:
            print(f"Address: {self.strAddress}")

# **********************************************************************************************************
# endregion
