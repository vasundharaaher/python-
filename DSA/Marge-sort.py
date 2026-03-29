"""
    Marge Sort

    divide and conqure

"""

def Divide(arr , l , r):
    if(l < r):
        m = (l + r)//2
        Divide(arr , l , m)
        Divide(arr , m+1 , r)
        marge(arr , l , m , r)

def marge(arr , l , m , r):
    # we will take photo copy of Left and Right array first 
    # lenth of L and R array
    s1 = m - l + 1
    s2 = r - m
    # initialize array with 0 
    L = [0] * s1
    R = [0] * s2

    for i in range(s1):
        L[i] = arr[l+i]

    for j in range(s2):
        R[j] = arr[m + j + 1]
    
    i=0
    j=0
    k=l
    while ( i < s1 and j < s2):
        if L[i]<R[j]:
            arr[k]=L[i]
            i += 1
            k += 1
        else:
            arr[k]=R[j]
            j += 1
            k += 1

    while (i<s1):
        arr[k]=L[i]
        i += 1
        k += 1

    while (j<s2):
        arr[k]=R[j]
        j += 1
        k += 1


arr = [20,5,88,12,46,90,10]
Divide(arr , 0 , len(arr)-1)
print (arr)
