import insertion_sort
import merge_sort
import quick_sort
import heap_sort
import random
import datetime

def createArray(n, minimum, maximum):
    arr = []
    for i in range(n):
        arr.append(random.randint(minimum, maximum))
    return arr

def compareArrays(ar1, ar2):
    if len(ar1) != len(ar2): return False

    for i in range(len(ar1)):
        if ar1[i] != ar2[i]: return False

    return True

def testSort(tests, n, minimum, maximum):
    time = [datetime.timedelta(0)] * 6
    for i in range(tests):
        ar = createArray(n, minimum, maximum)
        
        i_sort = list(ar)
        m_sort = list(ar)
        q_sort = list(ar)
        qr_sort = list(ar)
        h_sort = list(ar)

        d = datetime.datetime.now()
        insertion_sort.insertionSort(i_sort)
        time[0] += (datetime.datetime.now() - d)

        d = datetime.datetime.now()
        m_sort = merge_sort.mergeSort(m_sort)
        time[1] += (datetime.datetime.now() - d)

        d = datetime.datetime.now()
        quick_sort.quickSort(q_sort)
        time[2] += (datetime.datetime.now() - d)
        
        d = datetime.datetime.now()
        quick_sort.quickSortRand(qr_sort)
        time[3] += (datetime.datetime.now() - d)

        d = datetime.datetime.now()
        h_sort = heap_sort.heapSort(h_sort)
        time[4] += (datetime.datetime.now() - d)

        d = datetime.datetime.now()
        bible = sorted(ar)
        time[5] += (datetime.datetime.now() - d)
        
        error = False
        if not compareArrays(bible, i_sort):
            print "Insertion sort error: ar =",ar, ", i_sort =", i_sort, ", bible =", bible
            error = True
        if not compareArrays(bible, m_sort):
            print "Merge sort error: ar =",ar, ", m_sort =", m_sort, ", bible =", bible
            error = True
        if not compareArrays(bible, q_sort):
            print "Quick sort (deterministic) error: ar =",ar, ", q_sort =", q_sort, ", bible =", bible
            error = True
        if not compareArrays(bible, qr_sort):
            print "Quick sort (random) error: ar =",ar, ", qr_sort =", qr_sort, ", bible =", bible
            error = True
        if not compareArrays(bible, h_sort):
            print "Heap sort error: ar =",ar, ", h_sort =", h_sort, ", bible =", bible
            error = True

        if not error:
            print "Test", i+1, "successful"

    print "Insertion sort time =", time[0]
    print "Merge sort time =", time[1]
    print "Quick sort (deterministic) time =", time[2]
    print "Quick sort (random) time =", time[3]
    print "Heap sort time =", time[4]
    print "Default Python sort time =", time[5]


def main():
    testSort(100, 1000, -10000, 10000)


if __name__ == "__main__":
    main()


