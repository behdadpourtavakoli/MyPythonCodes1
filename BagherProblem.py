def Multiple(intNumber):
    bolResult = 0
    if (intNumber % 5 == 0):
        bolResult = 1
    return(bolResult)

strTemp = input()

arrParams = strTemp.split(" ")
intAngle1 = int(arrParams[0])
intAngle2 = int(arrParams[1])
intAngle3 = int(arrParams[2])
intSum = intAngle1 + intAngle2 + intAngle3

if (intAngle1 > 0 and intAngle2 > 0 and intAngle3 > 0) and ((Multiple(intAngle1) == 1) and (Multiple(intAngle2) == 1) 
    and (Multiple(intAngle3) == 1)) and (intSum == 180):
    print("YES")
else:
    print("NO")
