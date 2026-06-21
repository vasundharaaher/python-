""" find missing number in an array """

# def find(a):
#     n = a[-1]
#     sum1 = 0
#     total = n*(n+1)//2
#     sum1 = sum(a)
#     print(total - sum1)

# find([1,2,4,5,6])

# def get_missing_xor(a):
#     n=len(a)
#     for index in range(0,n):
#         if (a[index] ^ index+1) != 0:
#             break

#     print(index+1)
# get_missing_xor([1,2,4,5,6])


""" find out pairs with given sum in array """

# def twosum(arr,target):
#     arr.sort()
#     # print(arr)
#     left = 0
#     right = len(arr)-1
#     count = 0
#     while left < right :
#         if arr[left]+arr[right] < target:
#             left += 1
#         elif arr[left]+arr[right] > target:
#             right -= 1 
#         elif arr[left]+arr[right] == target:
#             left += 1 
#             right -= 1
#             count += 1

#     return count

# result=twosum([3,4,1,2,6], 7)
# print(result)


