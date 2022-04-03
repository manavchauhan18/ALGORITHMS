Token - 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

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

def InsertionSort(A):
    # array is virtually split into sorted and unsorted array.
    # value from the unsorted are picked and placed into sorted part
    # Time complexity O(n^2)
    for i in range(1, len(A)):
        key = A[i]
        
        j = i-1
        while j >= 0 and key < A[j]:
            A[j+1] = A[j]
            j -= 1
        
        A[j+1] = key
    
    print("Sorted Array: ")
    for n in range(len(A)):
        print("%d" %A[n],end=" ")

def MergeSort(A):
    # it is a divide and conquer algorithm.
    # whole array is divided into simpler elements.
    # Time complexity T(n) = 2T(n/2) + theta(n)
    if len(A) > 1:

        mid = len(A) // 2

        L = A[:mid]
        R = A[mid:]

        MergeSort(L)
        MergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1

            k += 1

        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1
         
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1

    print("Sorted Array: ")
    for n in range(len(A)):
        print("%d" %A[n],end=" ")
