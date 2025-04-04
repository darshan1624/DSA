# Q1. Second Largest Element in an array



"""
Solution: 
The function finds the second largest number by keeping track of the top two values while looping through the array. It updates firstmax and secmax accordingly and returns secmax.
"""

def getSecondLargest(self, arr):
        # Code Here
        firstmax = -1
        secmax = -1 
        
        for value in arr:
            if value > firstmax:
                secmax = firstmax
                firstmax = value
            elif value > secmax and value != firstmax:
                secmax = value
                
        return secmax