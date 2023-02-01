def selectionSortVariation(array: list[int]):
    for i in range(len(array) - 1):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

# arr = [6, 5, 4, 3, 2, 9]
# selectionSortVariation(arr)
# print(arr)

def selectionSort(array: list[int]):
    for i in range(len(array) - 1):
        minimum = array[i]
        minidx = i
        for j in range(i+1, len(array)):
            if array[j] < minimum:
                minidx = j
                minimum = array[j]
    
        array[i], array[minidx] = array[minidx], array[i]

arr = [1, 5, 4, 7, 2, 3]
selectionSort(arr)
print(arr)