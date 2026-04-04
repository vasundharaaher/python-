""" Reverce String without using slicing """

# st = "vasun"
# ls=[]
# j=len(st)-1
# for i in range(j,-1,-1):
#     print(st[i])
#     ls.append(st[i])

# ls="".join(ls)
# print(ls)


""" Check Palindrome """

# def palindrome(st):
#     st = st
#     j = len(st)//2 
#     n = len(st)-1
#     count=0
#     # print(j)
#     for i in range(j+1):
#         if st[i]==st[n]:
#             # print(st[i],st[n])
#             count += 1
#         else :
#             count -= 1
#         n-=1
#     if count == j+1:
#         return True
#     else :
#         return False


# result = palindrome("mada")
# print(result)


""" Find Largent Element """
# def maxnumber(ls):
#     ls = ls
#     max = ls[0]
#     for i in range(1,len(ls)):
#         if max < ls[i]:
#             max = ls[i]
#     return max

# n = int(input("number of element : "))
# ls = []
# for i in range(n):
#     inp = int(input("Enter your numbers : "))
#     ls.append(inp)

# max = maxnumber(ls)
# print(max)


""" Count Vowels in string """

# inp = input("Enter string : ")
# st = inp 
# ls = ["a","e","i","o","u"]
# count =0
# for i in st:
#     if i in ls:
#         count += 1

# print(count)


""" Factorial using loop """
# inp = 5
# fact = 1
# for i in range(1,inp+1,1):
#     fact = fact * i

# print (fact)

""" Factorial using recursion """

# def factorial(n):
   
#     if n == 1 or n == 0:
#         return 1
#     else : 
#         return n * factorial (n-1)

# rs = factorial(2)
# print(rs)



""" Fibonacci series using recursion """

# def fibonacciseries(n):
#     if n == 0 or n == 1 or n == 2 :
#         return n 
#     else:
#         return fibonacciseries(n-1) + fibonacciseries(n-2)
    
# print(fibonacciseries(4))


""" Capitalize String """

# st = "vasu"
# ls=[]
# for i in st:
#     n = ord(i)
#     n = chr(n-32)
#     ls.append(n)
# ls = "".join(ls)
# print(ls)

