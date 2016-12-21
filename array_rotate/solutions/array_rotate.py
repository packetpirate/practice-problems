# This function will rotate an array right.
# ie: Given [1,2,3], the function outputs [3,1,2]
def rotate(A,n):
    return [A[(i-n)%len(A)] for i in range(0, len(A))]
