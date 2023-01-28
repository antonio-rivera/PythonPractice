from Linkedlist import LinkedList

my_list = LinkedList()

for i in range(11):
    my_list.insert(i)

print(my_list)

my_list.deleteFirst()

print(my_list)

my_list.delete(1)

print(my_list)
# print(len(my_list))

my_list.insert(22)
print(my_list)

my_list.insertAfter(0, -1)
print(my_list)
