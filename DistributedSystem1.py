import os, random, time

def Distribute_Fairly(intAmount, lstUnits):
    '''
    /// Distribute_Fairly()--function to distributed fairly the intAmount to lstUnits items.
    
    /// Parameters:
    
    /// intAmount: main amount number
    
    /// lstUnits: List of units
    
    /// ADDED by Engineer B.Pourtavakoli on 1403/09/13
    '''
    lstUnits = sorted(lstUnits)  # مرتب‌سازی به ترتیب صعودی (برای توزیع بهتر به واحدهای کوچک‌تر)
    result = {unit: 0 for unit in lstUnits}
    intAmount2 = intAmount
    
    while (intAmount2 > 0):
        for unit in lstUnits:
            if (intAmount2 >= unit):
                result[unit] += 1
                intAmount2 -= unit

    # بررسی جمع نهایی
    #total = sum(unit * count for unit, count in result.items())
    #if (total != intAmount2):
        #print(f"Total: {total}, Main amount: {intAmount2}, Difference: {intAmount2 - total}")
        # raise ValueError(f"The total ({total}) is not equal to the original value!")

    return (result)


def Distribute_Randomly1(intAmount, lstUnits):
    '''
    /// Distribute_Randomly1()--function to distributed randomly the intAmount to lstUnits items as descending sort.
    
    /// Parameters:
    
    /// intAmount: main amount number
    
    /// lstUnits: List of units
    
    /// ADDED by Engineer B.Pourtavakoli on 1403/09/13
    '''    # مرتب‌سازی واحدها به ترتیب نزولی
    lstUnits = sorted(lstUnits, reverse=True)
    result = { unit: 0 for unit in lstUnits }

    while (intAmount > 0):
        # انتخاب تصادفی یک واحد
        unit = random.choice(lstUnits)
        
        # اگر عدد اصلی بزرگ‌تر یا مساوی واحد باشد، کاهش می‌دهیم
        if intAmount >= unit:
            result[unit] += 1
            intAmount -= unit

    return (result)


def Distribute_Randomly2(intAmount, lstUnits):
    '''
    /// Distribute_Randomly2()--function to distributed randomly the intAmount to lstUnits items as descending sort.
    
    /// Parameters:
    
    /// intAmount: main amount number
    
    /// lstUnits: List of units
    
    /// ADDED by Engineer B.Pourtavakoli on 1403/09/13
    '''
    lstUnits = sorted(lstUnits, reverse=True)
    result = { unit: 0 for unit in lstUnits }

    while (intAmount > 0):
        unit = random.choice(lstUnits)
        if intAmount >= unit:
            result[unit] += 1
            intAmount -= unit

    return (result)


#####################################################################################################
# Main Program

dtStartTime = time.time()

if (os.name == "nt"):
    _ = os.system("cls")

intAmount = 1000000
lstUnits = [1, 2, 5, 10, 20, 50, 100]

# Part 1
distribution = Distribute_Fairly(intAmount, lstUnits)

print("Fair Distribution:")
for unit, count in distribution.items():
    print(f"{unit} $: {count} $")

total = sum(unit * count for unit, count in distribution.items())
print(f"\nTotal: {total}\n")


# Part 2
distribution = Distribute_Randomly1(intAmount, lstUnits)

print("Fair randomly Distribution 1:")
for unit, count in distribution.items():
    # print(f"{unit} $: {count} $")
    print(f"{unit}: {count}")

total = sum(unit * count for unit, count in distribution.items())
print(f"\nTotal: {total}")


# Part 3
distribution = Distribute_Randomly2(intAmount, lstUnits)

print("Fair randomly Distribution 2:")
for unit, count in distribution.items():
    # print(f"{unit} $: {count} $")
    print(f"{unit}: {count}")

total = sum(unit * count for unit, count in distribution.items())
print(f"\nTotal: {total}")

dtEndTime = time.time()
dtElapsedTime = dtEndTime - dtStartTime
print("Elapsed time:: %s ms" % round(dtElapsedTime, 3))
