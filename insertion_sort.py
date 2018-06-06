

def insertionSort(arr):
    """ Sorts array arr in place, using insertion sort
        :type arr: List[object]
        :rtype: none
    """
    
    for i in range(len(arr)):
        for j in range(i-1,-1,-1):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break

def main():
    arr = [12, 4, 5, 81, 3, 2, 54, 19, 0]
    insertionSort(arr)
    print(arr)

if __name__ == "__main__":
    main()
