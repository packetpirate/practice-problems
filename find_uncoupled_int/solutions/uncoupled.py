# This function will return the one unpaired integer in a list.
# ie: Given the list [1,2,3,1,2], the function returns 3.
def unpaired(A):
    result = 0
    for i in A:
        result ^= i
    return result
