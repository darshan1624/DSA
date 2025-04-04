# Q7. Move Zero's to End

"""
Solution: Brute Force
Create a new list and add all no -ve elements. Append with same count of zeros.
"""
# Time complexity = O(n)
# Space complexity = O(n)

def moveZeros(n, a):
    count = 0
    seq = []
    for i in a:
        if i == 0:
            count +=1
        else: 
            seq.append(i)
    

    for i in range(count):
        seq.append(0)

    return seq


"""
Optimal Solution:
Two pointer approach:
Identify the first 0 in sequence. pointer j will point to this.
Identify next non zero number after j ponter and swap the numbers. Incremnt j and i. 
"""
# Time complexity = O(n)
# Space Complexity = O(1)

# [1,2,0,0,2,3]

# for i in range(len(arr))
#     if arr[i] == 0:
#         j = i
#         break

# for i in range(j+1, len(arr)):
#     if arr[i] != 0:
#         swap(arr[i], arr[j])
#         j = j +1



def moveZeros(n,a):
    j =-1
    for i in range(n):
        if a[i] == 0:
            j = i 
            break
    
    if j != -1:
        for i in range(j+1, n):
            if a[i] != 0:
                a[i], a[j] = a[j], a[i]
                j = j+1
    
    return a