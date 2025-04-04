# Q2. Check if an Array is Sorted

"""

Brute force 
1) sort the array  O(nlogn)
2) compare with original array O(n)

More Better:
if len(arr) == 1 return True 

def asc(arr)
    min = arr[0]
    for i in arr[1:]:
        if i < min:
            return False
    return True

def desc(arr)
    max = arr[0]
    for i in arr[1:]:
        if i>max:
            return False
    return True

isasc = is_asc(arr)
isdesc = is_desc(arr)


"""
"""
solution: 
The function checks if an array is sorted by comparing each element with the previous one. If any number is smaller, it returns False; otherwise, it returns True.
The first element is set as the minimum initially, and it updates as the loop runs."""


def arraySortedOrNot(arr) -> bool:
        # code here
        if len(arr) == 1:
            return True
        min = arr[0] 
        for i in arr[1:]:
            if i < min:
                return False
            min = i
        return True


print(arraySortedOrNot([1,2,3,4,5]))

"""
More Better approach: 
solution: 
The function uses a single-pointer traversal, iterating through the array from the second element. It checks if the previous element is greater than the current one. If any such case is found, it returns 0; otherwise, it returns 1, indicating the array is sorted.
"""

def isSorted(n,  a):
    # Write your code here.

    for i in range(1,len(a)):
        if a[i-1] > a[i]:
            return 0
    return 1     
