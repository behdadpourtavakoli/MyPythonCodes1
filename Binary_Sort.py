def Insert_Sort(arrTemp):
    if (len(arrTemp) <= 1):
        return(arrTemp)
    intPivot = arrTemp[len(arrTemp) // 2]
    intLeft = [x for x in arrTemp if x < intPivot]
    intMiddle = [x for x in arrTemp if x == intPivot]
    intRight = [x for x in arrTemp if x > intPivot]
    return(Insert_Sort(intLeft) + intMiddle + Insert_Sort(intRight))

strTemp = input()

if (len(strTemp) > 500000):
    exit()

arrParams = strTemp.split(" ")

intMax = 1000000000
intLen = len(arrParams)
for intI in range(0, intLen):
    if (int(arrParams[intI]) > intMax):
        exit()

arrParams = Insert_Sort(arrParams)
for intI in range(0, intLen):
    print(arrParams[intI], ' ', end='', sep='')
