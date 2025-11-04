""" Linear Search 
Search for element one by one in give array
"""
"""
def Linear_Search(arr, target):
    n = len(arr)
    for i in range(0,n):
        if arr[i] == target:
            return i    
    return -1


list = [12,25,11,34,90,22]
result = Linear_Search(list, 22)
print(result)

result2 = Linear_Search(list, 12)
print(result2)

result3 = Linear_Search(list, 11)
print(result3)

"""

#########################

"""Binary Search 
1) Array should be sorted in increasing or decresing order
2) It will copaire target element with middel element (consider increasing ordered array if a target element is less then middle
    in next phase we will only consider first half of array And if a target element is greater then middle
    in next phase we will only consider second half of array 
    
    middel = """