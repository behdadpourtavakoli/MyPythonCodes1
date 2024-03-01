intNumber = int(input())

if (intNumber < 1 or intNumber > 10):
    exit()

print('W', end='', sep='')
for intI in range(0, intNumber):
    print('O', end='', sep='')
print('W!')
