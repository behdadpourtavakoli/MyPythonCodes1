strNumber = input()

intLen = len(strNumber)
if (intLen <= 0 or intLen > 100):
    exit(0)

arrNumber = []
for intI in range(0, intLen):
    arrNumber.append(str(strNumber[intI]))

for intI in range(0, len(arrNumber)):
    intTemp = int(arrNumber[intI])
    print(str(intTemp), ": ", end='', sep='')
    for intI in range(0, intTemp):
        print(str(intTemp), end='', sep='')
    print()
