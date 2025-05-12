# main.py

from LinkedList import LinkedList

ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_start(5)
ll.insert_at_index(1, 7)
ll.display()

print("Index of 7:", ll.search(7))
print("Index of 99:", ll.search(99))

ll.delete_at_index(1)
ll.display()
