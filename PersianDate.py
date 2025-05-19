import jdatetime
from datetime import datetime
import os

def shamsi_to_miladi(year, month, day):
    try:
        shamsi_date = jdatetime.date(year, month, day)
        miladi_date = shamsi_date.togregorian()
        miladi_date = str(miladi_date).replace("-", "/")
        return miladi_date
    except ValueError as e:
        return f"خطا در تبدیل تاریخ: {e}"

def miladi_to_shamsi(year, month, day):
    try:
        miladi_date = datetime(year, month, day)
        shamsi_date = jdatetime.date.fromgregorian(date=miladi_date)
        shamsi_date = str(shamsi_date).replace("-", "/")
        return shamsi_date
    except ValueError as e:
        return f"خطا در تبدیل تاریخ: {e}"

if (os.name == "nt"):
    _ = os.system("cls")

strTemp = "Engineer Behdad Pourtavakoli"
print(f"Text: {strTemp} - Split: {strTemp.split()}")

print(f"Slice 1:{strTemp[0:8]}-{strTemp[9:15]}-{strTemp[16:29]}-")
print(f"Slice 2:{strTemp[:8]}-{strTemp[9:15]}-{strTemp[16:]}-")

str = "GeeksForGeeks is best!"
substring_start = str[:5]
print(substring_start)
tupTuple = tuple(str.split()) # Convert data from List to Tuple - Sorted by Base source
setSet = set(str.split())     # Convert data from List to Set - Unsorted
print(f"Split: {str.split()}\r\nSplit: {tupTuple}\r\nSplit: {setSet}")

exit(0)

print()
print()
dtToday = datetime.now()

dtYear = dtToday.year
dtMonth = dtToday.month
dtDay = dtToday.day
dtShamsi = miladi_to_shamsi(dtYear, dtMonth, dtDay)
print(f"Miladi 2 Shamsi: {dtShamsi}")

dtShamsi = str(dtShamsi)
print(f"{dtShamsi} - {type(dtShamsi)} - {len(dtShamsi)}")

print(f"{dtShamsi[0:4]} - {dtShamsi[5:7]} - {dtShamsi[8:10]}")


if (len(dtShamsi) == 10):
    intYear = dtShamsi[0:4]
    intMonth = dtShamsi[5:7]
    intDay = dtShamsi[8:10]
    print(f"{intYear} : {intMonth} : {intDay}")
exit(0)

dtYear = dtShamsi.year
dtMonth = dtShamsi.month
dtDay = dtShamsi.day
print(f"Shamsi 2 Milad: {shamsi_to_miladi(1402, 8, 28)}")
