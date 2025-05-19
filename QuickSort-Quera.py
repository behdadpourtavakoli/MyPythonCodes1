def Insert_Sort(arrTemp):
    if len(arrTemp) <= 1:
        return arrTemp
    intPivot = arrTemp[len(arrTemp) // 2]
    intLeft = [x for x in arrTemp if x < intPivot]
    intMiddle = [x for x in arrTemp if x == intPivot]
    intRight = [x for x in arrTemp if x > intPivot]
    return Insert_Sort(intLeft) + intMiddle + Insert_Sort(intRight)

strTemp = input()

arrParams = list(map(int, strTemp.split()))

if len(arrParams) > 500000:
    exit()
arrParams = Insert_Sort(arrParams)
print(" ".join(map(str, arrParams)))

'''def Quick_Sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    
    return Quick_Sort(left) + [pivot] + Quick_Sort(right)

def QuickSort():
    input_string = input()
    numbers = list(map(int, input_string.split()))
    sorted_numbers = Quick_Sort(numbers)
    print(" ".join(map(str, sorted_numbers)))'''
