import random
import datetime

def quickSort(arr, start = -1, end = -1):
    """ Quick sort, deterministic. Sorts array arr in place. Always chooses last element as pivot.
        type arr: List[]
        type start: int
        type end: int
        rtype: none
    """
    if start == -1: start = 0
    if end == -1: end = len(arr)-1
    
    if start >= end: return

    p = arr[end]
    
    l_pt = start
    for i in range(start,end):
        if arr[i] <= p:
            arr[i], arr[l_pt] = arr[l_pt], arr[i]
            l_pt += 1
    arr[end], arr[l_pt] = arr[l_pt], arr[end]
    
    quickSort(arr, start, l_pt-1)
    quickSort(arr, l_pt, end)

def quickSortRand(arr, start = -1, end = -1):
    """ Quick sort, with random pivots. Sorts array arr in place. 
        type arr: List[]
        type start: int
        type end: int
        rtype: none
    """
    if start == -1: start = 0
    if end == -1: end = len(arr)-1
    
    if start >= end: return

    p_pt = random.randint(start,end)
    arr[end], arr[p_pt] = arr[p_pt], arr[end]
    p = arr[end]
    
    l_pt = start
    for i in range(start,end):
        if arr[i] <= p:
            arr[i], arr[l_pt] = arr[l_pt], arr[i]
            l_pt += 1
    arr[end], arr[l_pt] = arr[l_pt], arr[end]
    
    quickSort(arr, start, l_pt-1)
    quickSort(arr, l_pt, end)    
    
    
def main():
    arr = [1, 5, 3, 12, 31, 9, -1, -123, 34, 65, 8, 1, 3, 0, -91, 55, 2]
    d = datetime.datetime.now()
    quickSort(arr)
    print(arr)
    print(datetime.datetime.now() - d)
    
    arr = [1, 5, 3, 12, 31, 9, -1, -123, 34, 65, 8, 1, 3, 0, -91, 55, 2]
    d = datetime.datetime.now()
    quickSortRand(arr)
    print(arr)
    print(datetime.datetime.now() - d)

if __name__ == "__main__":
    main()
