import math

#strTemp = input()
#arrParams = strTemp.split(" ")
#intAngle1 = int(arrParams[0])
#intAngle2 = int(arrParams[1])
#intAngle3 = int(arrParams[2])

intAngle1 = int(input())
intAngle2 = int(input())
intAngle3 = int(input())

intHypotenuse = math.sqrt(pow(intAngle1, 2) + pow(intAngle2, 2))

if (((intAngle1 >= 1 and intAngle1 <= 150) and (intAngle2 >= 0 and intAngle2 <= 150) and (intAngle3 >= 0 and intAngle3 <= 150))
    and (intHypotenuse == intAngle3)):
    print("YES")
else:
    print("NO")

#if (intAngle1 <= 0 or intAngle1 > 150) or (intAngle2 <= 0 or intAngle2 > 150) or (intAngle3 <= 0 or intAngle3 > 150):
#    print("NO")
#elif (math.sqrt(intHypotenuse) == intAngle3):
#    print("YES")
#else:
#    print("NO")