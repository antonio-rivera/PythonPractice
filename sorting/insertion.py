def insertionSort(a: list):
    i = 0
    while(i < len(a)-1):
        if a[i] > a[i+1]:
            toInsert = a[i+1]
            j = i
            while(toInsert <= a[j] and j >= 0):
                a[j+1] = a[j]
                j -= 1
            j+=1
            a[j] = toInsert
        i += 1

a = [7, 1, 5, 3]
insertionSort(a)
print(a)