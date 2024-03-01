intNumber = int(input())

if (intNumber < 1 or intNumber > 10):
    exit()

intFactorial = 1
for i in range(1, intNumber+1):
    intFactorial *= i

print(intFactorial)
