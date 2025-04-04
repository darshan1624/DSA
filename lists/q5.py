# Q5. Left rotate an array by D places


# Logic for left rotate
"""

[1,2,3,4,5]
steps = 2 , left

if  steps > len(arr):
    steps  = steps % len(arr) 

k = [:2]

==============
way 1
i = 0 
for j in range(2,len(arr))
    arr[i] = arr[j]
    i = i+1

arr[-2:] = k
================


=========================
way 2
[1,2,3,4,5]
steps = 2 

How shifting happends
arr[0] = arr[2]     2-0 = 2  or we can say 2-2 = 0 
arr[1] = arr[3]     3-1 = 2 or 3-2 = 1
arr[2] = arr[4]     4-2 = 2 or 4-2 = 2 

for i in range(2, len(arr)):
    arr[i-steps] = arr[i]

arr[-2:] = k
=======================
"""
"""
solution:
The first k elements are stored separately, the remaining elements are shifted left, and the stored elements are placed at the end. If k exceeds the array length, it is adjusted using modulo.

"""



# steps = 3
# arr = [1,2,3,4,5,6,7]

def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    k = k % len(nums)
    if k == 0:
        return nums

    nums_to_append = nums[:k]

    for i in range(k, len(nums)):
        nums[i-k] = nums[i]

    for i in range(k):
        nums[len(nums) - k - i] = nums_to_append[i]

    return nums


# logic for right rotate
#############################################################################################################

# # nums = [1,2,3,4,5,6,7]
# # k = 3
# nums = [-1, -100, 3, 99]
# k = 2

# k = k % len(nums)

# nums_to_append_start = nums[(len(nums) - k)]


# for i in range(len(nums)-k):
#             nums[len(nums)-1 - i] = nums[len(nums) -k -1 - i]


# """logic building"""


# # nums = [1,2,3,4,5,6,7]
# #k = 3 

# 6 = 3        len(nums) - 1 = len(nums) - k -1
# 5 = 2        
# 4 = 1 
# 3 = 0


# # no. of itterations = 4  can be seen why beacuse we had to shift 4 elements
# # if have 7 elments and 3 shifts to be done then, elemnts to be moved = 4

# for i range(len(nums) - k)
# nums[len(nums) - 1 -i] = nums[len(nums) - k -1 - i]



# #nums = [1,2,3,4]
# k = 2
# 3 = 1  len(nums) -1 = len(nums) - k -1
# 2 = 0 

# #no. of itterations = 2  can be seen why beacuse we had to shift 2 elements 
# # if have 4 elments and 2 shifts to be done then, elemnts to be moved = 2

# range(len(nums)-k) 

# ============================


# # Now how to append list nums_to_append_start

# nums_to_append_start = [5,6,7]

# nums = [1,2,3,1,2,3,4]

# for i in range(k):
#     nums[i] = nums_to_append_start[i]


# print(nums)

"""
solution: 
The array is rotated by extracting the last k elements, shifting the remaining elements to the right, and placing the extracted elements at the beginning. If k exceeds the array length, it is adjusted using modulo.

"""


# Code: 
def rotate(nums, k):
    if k > len(nums):
        k = k % len(nums)

    if k==0:
        return nums

    nums_to_append_start = nums[(len(nums) - k):]

    for i in range(len(nums)-k):
        nums[len(nums)-1 - i] = nums[len(nums) -k -1 - i]

    for i in range(k):
        nums[i] = nums_to_append_start[i]
    
    return nums
                



# Rotate array with no extra list.
"""
Optimal Solution:
It reverses the first k elements. It reverses the remaining elements. It reverses the entire array to get the final rotated result.
"""

# # nums = [1,2,3, 4,5,6,7]
# # k = 3
# nums = [-1, -100, 3, 99]
# k = 2

# nums[:k]      [1,2,3]         reverse [3,2,1]           3,2,1,7,6,5,4        4,5,6,7,1,2,3
# nums[k:]       [4,5,6,7]      reverse [7,6,5,4]

# 4321 765     5671234

def reverse(nums):
    for i in range(len(nums)//2):
        nums[i], nums[len(nums)-1 - i ] = nums[len(nums)-1 - i ], nums[i]
    return nums

def rotate1(nums,k):
    a1 = reverse(nums[:k])
    a2 = reverse(nums[k:])  
    return reverse(a1 +a2)

print(rotate1([-1, -100, 3, 99], 2))