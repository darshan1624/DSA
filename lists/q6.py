# Q6. Reverse a given array. 
"""
[5, 7, 8, 1, 6, 3]

i = 0 
j = len(arr)-1

n = 6  6//3
itteration = 3

[5, 7, 8, 1, 6]
n = 5    5//2
itteration = 2
"""

"""
solution:
The function uses a two-pointer approach, swapping the first and last elements while moving toward the center. It iterates only up to half the array to ensure all elements are reversed in-place. This efficiently reverses the array with O(n) time complexity.
"""


def reverseArray(n, nums):
    # Write your code here
    i = 0 
    j = n-1
    for k in range(n//2):
        (nums[i], nums[j]) = (nums[j], nums[i])
        i = i+1 
        j = j-1
    return nums


"""
Try using less variables.

[5, 7, 8, 1, 6, 3]
n =6
iterations = 6//2
0,5     0,n-1
1,4	i,n-1-i	
2,3	i, n-1-i
"""

def reverseArray(n, nums):
    # Write your code here
    for i in range(n//2):
        (nums[i], nums[n-1-i]) = (nums[n-1-i], nums[i])
    return nums