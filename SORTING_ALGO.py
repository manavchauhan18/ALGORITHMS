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
    # repeatedly swaps he adjacent elements if they are in wrong order
    # follows n number of passes where n = number of elements
    # Time complexity O(n^2)
    length = len(A)
    for i in range(length):
        for j in range(0, length-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    
    print("Sorted array: ")
    for n in range(len(A)):
        print("%d" %A[n],end=" ")

