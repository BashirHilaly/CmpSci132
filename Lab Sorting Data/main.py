"""
----------------------------------------------------
-- CMPSC_132, Spring 2024, Bashir Hilaly
-- Lab Sorting Data
----------------------------------------------------
"""
import random

# Notes: 
# Keep track of:
#   Number of passes made through the list to sort everything
#   Total number of swaps executed

def BubbleSort(lst, ascending):

    print("\nList before the sort: \n\t", lst)

    totalPasses = 0
    totalSwaps = 0
    amountOfNums = len(lst)

    # Loop through the list
    for i in range(amountOfNums):
        # Leave the last element. Loop through the list and perform swaps
        for j in range(amountOfNums - i - 1):
            totalPasses += 1
            if ascending:
                # Checks if j is greater than the element after it, if so then swap
                if lst[j] > lst[j + 1]:
                    # Swap
                    temp = lst[j]
                    lst[j] = lst[j + 1]
                    lst[j + 1] = temp
                    totalSwaps += 1
            else: 
                if lst[j] < lst[j + 1]:
                    # Swap
                    temp = lst[j]
                    lst[j] = lst[j + 1]
                    lst[j + 1] = temp
                    totalSwaps += 1
    
    print("\nList after the sort: \n\t", lst)
    print(f"\nStats: \n\tNumber of passes: {totalPasses} \n\tNumber of swaps: {totalSwaps}")
    #return lst



if __name__ == '__main__':

    listLength = int(input("\nHow many integers would you like in your randomly generated list?: "))

    randomList = [random.randint(100, 1000000) for i in range(listLength)]

    ascendingOrDescending = input("\nType \'a\' for Ascending or \'d\' for Descending: ")
    direction = False
    if ascendingOrDescending == 'a':
        direction = True
    else:
        direction = False

    BubbleSort(randomList, direction)
