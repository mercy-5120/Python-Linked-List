# LinkedList.py

class Node:
    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.next = None  # Pointer to the next node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_index(self, index, data):
        if index < 0:
            raise IndexError("Index cannot be negative.")
        new_node = Node(data)
        if index == 0:
            self.insert_at_start(data)
            return
        temp = self.head
        for i in range(index - 1):
            if not temp:
                raise IndexError("Index out of range.")
            temp = temp.next
        if not temp:
            raise IndexError("Index out of range.")
        new_node.next = temp.next
        temp.next = new_node

    def delete_at_index(self, index):
        if index < 0 or not self.head:
            raise IndexError("Index out of range.")
        if index == 0:
            self.head = self.head.next
            return
        temp = self.head
        for i in range(index - 1):
            if not temp.next:
                raise IndexError("Index out of range.")
            temp = temp.next
        if not temp.next:
            raise IndexError("Index out of range.")
        temp.next = temp.next.next

    def search(self, value):
        temp = self.head
        index = 0
        while temp:
            if temp.data == value:
                return index
            temp = temp.next
            index += 1
        return -1

    def display(self):
        temp = self.head
        if not temp:
            print("List is empty")
            return
        while temp:
            print(temp.data, end=" -> " if temp.next else "")
            temp = temp.next
        print()
