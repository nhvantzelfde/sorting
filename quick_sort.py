
def quickSort(arr, start = -1, end = -1):
    """ Quick sort, deterministic. Sorts array arr in place. Always chooses last element as pivot.
        type arr: List[]
        rtype: none
    """
    if start == -1: start = 0
    if end == -1: end = len(arr)-1
    
    if end >= start: return
    
    p = arr[end]
    
    l_pt = 0
    for i in range(start,end):
        if arr[i] <= p:
            arr[i], arr[l_pt] = arr[l_pt], arr[i]
            l_pt += 1
        
    quickSort(arr, start, l_pt)
    quickSort(arr, l_pt, end-1)

main():
    arr = [1, 5, 3, 12, 31, 9, -1, -123, 34, 65, 8, 1, 3, 0, -91, 55, 2]
    quickSort(arr)
    print(arr)

if __name__ == "__main__":
    main()
