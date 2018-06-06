
class MinHeap(object):
    def __init__(self):
        self.values = []

    def createMinHeap(self, keys):
        self.values = list(keys)
        for i in range(len(self.values)//2-1,-1,-1):
            self.__minHeapify(i)
        self.__repCheck()

    def decreaseKey(self, i, key):
        if i >= self.size() or key >= self.values[i]:
            return
        self.values[i] = key
        p = self.__parent(i)
        while i > 0 and self.values[i] < self.values[self.__parent(i)]:
            self.values[i], self.values[self.__parent(i)] = self.values[self.__parent(i)], self.values[i]
            i = self.__parent(i)
        # self.__repCheck()

    def findMin(self):
        if self.size() == 0: return None
        else: return self.values[0]

    def extractMin(self):
        if self.size() == 0: return None
        else:
            self.values[0], self.values[self.__last()] = self.values[self.__last()], self.values[0]
            minimum = self.values.pop()
            self.__minHeapify(0)
            # self.__repCheck()
            return minimum

    def __minHeapify(self, i):
        l = self.__left(i)
        r = self.__right(i)
        smallest = i
        if l < self.size() and self.values[l] < self.values[smallest]:
            smallest = l
        if r < self.size() and self.values[r] < self.values[smallest]:
            smallest = r
        if smallest != i:
            self.values[i], self.values[smallest] = self.values[smallest], self.values[i]
            self.__minHeapify(smallest)
        
    def insert(self, key):
        self.values.append(-float("inf"))
        self.decreaseKey(self.__last(),key)

    def delete(self, value):
        pass

    def size(self):
        return len(self.values)

    def __parent(self, i):
        return (i + 1) // 2 - 1

    def __left(self, i):
        return 2 * (i + 1) - 1

    def __right(self, i):
        return 2 * (i + 1)

    def __last(self):
        return self.size() - 1

    def __str__(self):
        return "MinHeap, values = " + str(self.values)

    def __repCheck(self):
        for i in range(self.size()):
            l = self.__left(i)
            r = self.__right(i)
            if l < self.size() and self.values[i] > self.values[l]:
                print "Rep Invariant Error, index =", i
            if r < self.size() and self.values[i] > self.values[r]:
                print "Rep Invariant Error, index =", i

def heapSort(arr):
    """ Sorts an array by creating a heap and sorting.
        type arr: List[]
        rtype: List[]
    """
    heap = MinHeap()
    heap.createMinHeap(arr)
    result = []
    while heap.size() > 0:
        result.append(heap.extractMin());

    return result

def main():
    arr = [12, 3, 76, -8, -100, 4, 87, 13, 1, 0, -6, 4, 13]
    sorted_arr = heapSort(arr)
    print(sorted_arr)

if __name__ == "__main__":
    main()
