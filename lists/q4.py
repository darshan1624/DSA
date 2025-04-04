# Q4. Left Rotate the Array by One

"""
Brute Force:
Maintain a seprate list.
"""


def rotateArray(arr):
    # Write your code from here. 
    arr = arr[1:] + arr[:1]       # createing a new list
    return arr  

"""
Time complxity = O(n)
Space complxity = O(n)
"""


"""
Optimal solution:
Modify existing db by changing previous elements.

The first element is stored separately, all other elements are shifted left by one position, and the stored element is placed at the end to complete the rotation.
"""

def rotateArray1(arr):
    # Write your code from here. 
    first_value = arr[0] 
    for i in range(1,len(arr)):
        arr[i-1] = arr[i]
    
    arr[-1] = first_value
    return arr  

print(rotateArray1([1,2,3,4]))