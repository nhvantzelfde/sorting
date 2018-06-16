
def mergeSort(arr):
    """
    Merge sort. Returns sorted array; original array is unchanged.
    :type arr: List[]
    :rtype: List[]
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    
    l_pt, r_pt = 0, 0
    result = []
    while l_pt < len(left) or r_pt < len(right):
        if l_pt >= len(left):
            result.append(right[r_pt])
            r_pt += 1
        elif r_pt >= len(right):
            result.append(left[l_pt])
            l_pt += 1
        else:
            if left[l_pt] <= right[r_pt]:
                result.append(left[l_pt])
                l_pt += 1
            else:
                result.append(right[r_pt])
                r_pt += 1
                
    return result

def main():
    arr = [1, 3, 5, 12, 31, 9, -1, -123, 34, 65, 8, 1, 3, 0, -91]
    sorted_arr = mergeSort(arr)
    print sorted_arr

if __name__ == "__main__":
    main()
