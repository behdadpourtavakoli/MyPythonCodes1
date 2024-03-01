arrNumber = []
while (True):
    intNumber = int(input())
    if (intNumber == 0):
        break
    else:
        arrNumber.append(intNumber)

arrNumberX = arrNumber[::-1]

for intI in range(0, len(arrNumberX)):
    print(arrNumberX[intI])
