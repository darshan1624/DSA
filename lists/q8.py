# Q8. Union of 2 Sorted with Duplicates


"""
solution: Brute Force
 Itterate over length sum of both array and find if item in another array and not in required list.
"""

# time complexity = O(n+m)
# space complexity = O(n+m)

i = 0 
j = 0 
a = [10,20, 30,40]
b = [1,2,20,25,40,60]
union = [] 
for k in range(len(a) + len(b)):

	if i>=len(a):
		if not union or b[j] != union[-1]:
			union.append(b[j])
		j +=1
	elif j >=len(b):
		if not union or a[i] != union[-1]:
			union.append(a[i])
		i +=1

	elif (a[i] < b[j]):
		if not union or a[i] != union[-1]:
			union.append(a[i])
		i = i+1
	else:
		if not union or b[j] != union[-1]:
			union.append(b[j])
		j = j+1

print(union)
