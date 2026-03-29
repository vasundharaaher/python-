
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