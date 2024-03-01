#intNumber = int(input())
#print(intNumber)

strNumber = input()
intLen = len(strNumber)

arrNumber = []
for intI in range(0, intLen):
    arrNumber.append(str(strNumber[intI]))

strNumber = ''.join(map(str, arrNumber))
intNumber = int(strNumber)

intSum = 0
while True:
    while (intNumber >= 10):
        intSum += int(intNumber % 10)
        intNumber /= 10

    intSum += int(intNumber % 10)

    if (intSum < 10):
        break
    else:
        intNumber = intSum
        intSum = 0

print(intSum)
