# Q3. Remove Duplicates Sorted Array

"""

[1,1,2,3]
0,1,2
seq = [arr[0]]
for i in range(1,len(arr)):
    if arr[i] != arr[i-1]:
        seq.append(arr[i])

return seq
"""

"""
brute force: We have to maintain additional set/list.

solution: This method goes through a sorted list and keeps only unique elements. It starts with the first element and adds a new number only if it's different from the previous one. This way, duplicates are skipped, and the result contains only distinct values.
"""


def removeDuplicates(arr):
    #Code Here
    seq = [arr[0]]
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            seq.append(arr[i])
    print(seq)
    return len(seq)

removeDuplicates([2,2,2,2,2,2,4,4,4,4,4,4,4])


"""Time complxity = O(n)
    Space complexity = O(n)
    """


"""
Optimal Solution:
This function uses a two-pointer approach to remove duplicates in a sorted list in-place. The i pointer tracks unique elements, while j iterates through the list, updating i+1 when a new unique element is found

"""

def removeDuplicates(nums):
    i = 0 
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            nums[i+1] = nums[j]
            i = i +1 
    return i+1



"""Time complxity = O(n)
    Space complexity = O(1)
"""

