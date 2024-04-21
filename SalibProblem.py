def game(intNumber):

    intFirstNum = int(intNumber / 10)
    intSecondNum = int(intNumber % 10)

    intResult = -1
    if (intFirstNum > intSecondNum):
        intResult = intFirstNum - intSecondNum
    else:
        intResult = intSecondNum - intFirstNum

    return(intResult)

intNumber = int(input())
print(game(intNumber))
