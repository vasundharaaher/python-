""" Bubble Sorrt 


"""
"""
def buble_sort(arr):
    n = len(arr)
    for passes in range(0,n): 
        for j in range(0 , n-1 - passes):
            if(arr[j] > arr[j+1]):
                arr[j] , arr[j+1] = arr[j+1] , arr[j]

    return arr

unsorted_list = [12,25,11,34,90,22]
sorted_list = buble_sort(unsorted_list)
print("Sorteed Elements : ",sorted_list)

"""
##########################################

""" Selection Sort 
1) In each pass we see the arraay and select the minimum, we swap that to the right position.
"""
"""
def Selection_Sort(arr):
    n = len(arr)
    
    for j in range(n-1):
        min_index = j

        for i in range(j+1,n):

            if arr[min_index] > arr[i]:
                min_index = i

        arr[j], arr[min_index] = arr[min_index], arr[j]

    return arr


unsorted_list = [12,25,11,34,90,22]
sorted_list = Selection_Sort(unsorted_list)
print("Sorteed Elements : ",sorted_list)

"""
########################################

"""Insertion Sort
1) first round not required as 1 element always sorted
"""

def Insertion_Sort(arr):
    n = len(arr)
    
    for current in range(1 , n):
        currentCard = arr[current]
        correctPossition = current - 1      # It will go from i-1 to 0

        while correctPossition >= 0:
            if arr[correctPossition] < currentCard:
                break
            else :
                arr[correctPossition + 1] = arr[correctPossition] 
                correctPossition -= 1

            arr[correctPossition + 1] = currentCard
            
    return arr

unsorted_list = [12,25,11,34,90,22]
sorted_list = Insertion_Sort(unsorted_list)
print("Sorteed Elements : ",sorted_list)