import math

max = 10000000000
intNumber = int(input())

if (intNumber < 1 or intNumber > max):
    exit()

for i in range(0, max):
    intTemp = int(math.pow(2, i))
    if (intTemp > intNumber):
        break
print(intTemp)
