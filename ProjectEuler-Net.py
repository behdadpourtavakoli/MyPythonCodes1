# This Program displays natural numbers between 1 and 1000, that are multiples of 3 or 5. The sum of these multiples
# is 23 for the range 1 to 10.
# Design and developed by Engineer Behdad Pourtavakoli on 1403/07/10

# Dieses Programm zeigt natürliche Zahlen zwischen 1 und 1000 an, die Vielfache von 3 oder 5 sind. Die Summe dieser
# Vielfachen beträgt 23 für den Bereich von 1 bis 10.
# Entworfen und entwickelt von Ingenieur Behdad Pourtavakoli am 1403/07/10
class ProjectEuler_Net:
    def winmain(self):
        intX = 0
        for intI in range(1, 1000):
            if (intI % 3 == 0):
                intX += intI
                # print(intI)
            elif (intI % 5 == 0):
                intX += intI
                # print(intI)

        print("\r\nResult:", intX)

if (__name__ == "__main__"):
    clsPEN = ProjectEuler_Net()
    clsPEN.winmain()
