import random

arr = []

for i in range(100):
    arr.append(random.randint(0,100))

def merge(arr1, arr2):
    arrf = []
    while True:
        if arr1[0]<=arr2[0]:
            arrf.append(arr1.pop(0))
        else:
            arrf.append(arr2.pop(0))
        if arr1 == []:
            return arrf + arr2
        elif arr2 == []:
            return arrf + arr1
        
def mergesort(array):
    if len(array) == 1:
        return array
    else:
        mid = len(array)//2
        return merge(mergesort(array[:mid]),mergesort(array[mid:]))
    
print(mergesort(arr))
