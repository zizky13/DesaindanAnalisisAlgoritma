#function to find the parittion position
def partition(array, low, high):
    #choose the rightmost element as pivot
    pivot = array[high]

    #pointer for greater element
    i = low - 1

    for j in range (low, high):
        if array[j] <= pivot:

            #if element smaller than pivot is found
            #swap it with the greater element pointer by i
            i += 1

            #Swapping element at i with element at j
            (array[i],array[j]) = (array[j],array[i])

    (array[i + 1], array[high]) = (array[high], array[i+1])

    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)

        quickSort(array, low, pi - 1)

        quickSort(array, pi + 1, high)

data = [4,12,23,9,21,1,35,2,24]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print("Sorted Array in Ascending Order: ")
print(data)