from Array import Array
# from badarray import Array
maxSize = 10
arr = Array(10)

arr.insert(77)
arr.insert(99)
arr.insert("Foo")
arr.insert("bar")
arr.insert(44)
arr.insert(55)
arr.insert(12.34)
arr.insert(0)
arr.insert("baz")
arr.insert(-17)

print("Array containing", len(arr), "items")
arr.traverse()

print("Search for 12 returns", arr.search(12))

print("Search for 12.34 returns", arr.search(12.34))

print("Deleting 0 returns", arr.delete(0))

print("Deleting 17 returns", arr.delete(17))

print("Array after deletions has", len(arr), "items")
arr.traverse()

print("Element at position 2: ", arr[2])

arr.set_item(50, 2)

print("Element after modification: ", arr[2])
