
def insertionSort(arr):
    """
    Sorts array arr in place, using insertion sort
    :type arr: List[object]
    :rtype: none
    """
    for i in range(len(arr)):
        for j in range(i-1,-1,-1):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
            else:
                break

def main():
    arr = [12, 4, 5, 81, 3, 2, 54, 19, 0, 123, 4, 5, 6, 2, -1, 6, 342]
    insertionSort(arr)
    print(arr)

if __name__ == "__main__":
    main()
