# GCD and sort
n = int(input('Enter no of inputs: '))
arr = []

# Input elements
for i in range(n):
    el = input()
    try:
        el = eval(el)
    except:
        el = ord(el)
    arr.append(el)

def findGCD(a, b):
    if a > b:
        a, b = b, a
    while a >= 0.001:
        a, b = b % a, a
    return round(b, 3)

def calculateArrayGCD(arr):
    gcd = arr[0]
    for i in range(1, len(arr)):
        gcd = findGCD(gcd, arr[i])
    
    return gcd

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j] > arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

if __name__ == '__main__':
    gcd = calculateArrayGCD(arr)
    print('GCD:', gcd)
    arr.append(gcd)
    sortedArr = bubbleSort(arr)
    print(sortedArr)