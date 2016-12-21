# This function will, given a target sum and an array of integers,
# return whether or not two integers exist in the array that add up
# to the target sum.
# ie: Given sum 10 and an array [2,8,5,3,1,9], the function returns True.
def targetSum(A, n):
    for i in range(0, len(A)):
        c = n - A[i]
        # Subtract 1 from count to account for the number we're looking at.
        # This prevents cases where 2i = n and there is only one occurrence
        # of i in the array.
        if (A.count(c) - 1) > 0: return True
    return False

print(targetSum([1,2,3], 10))
print(targetSum([1,2,2,5,7,8], 10))
print(targetSum([1,1,2,3,5,6], 10))
