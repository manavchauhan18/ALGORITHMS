def SelectionSort(A):
    # this algo repeadly finds out the smallest element in the array and swaps  accordingly.
    # maintains 2 arrays i.e sorted and unsorted subarrays.
    # Time Complexity O(n^2)
    length = len(A)
    for i in range(length):
        min_idx = i
        for j in range(i+1, length):
            if A[min_idx] > A[j]:
                min_idx = j
            
        A[i], A[min_idx] = A[min_idx], A[i]

    print("Sorted Array: ")
    for i in range(len(A)):
        print("%d" %A[i],end=" ") 

def BubbleSort(A):
    pass