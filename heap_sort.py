import sys
sys.path.insert(0, '../data_structures')
from heap import MinHeap

def heapSort(arr):
    """
    Sorts an array by creating a heap and continually extracting minimums.
    Array is not sorted in place.
    type arr: List[]
    rtype: List[]
    """
    heap = MinHeap()
    heap.createMinHeap(arr)
    return heap.extractAll()

def main():
    arr = [12, 3, 76, -8, -100, 4, 87, 13, 1, 0, -6, 4, 13]
    sorted_arr = heapSort(arr)
    print(sorted_arr)

if __name__ == "__main__":
    main()
    
