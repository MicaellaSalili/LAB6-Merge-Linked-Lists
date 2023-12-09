class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

def merge_sorted_lists(list1, list2):
    temp = Node()
    current = temp

    while list1 is not None and list2 is not None:
        if list1.value < list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    if list1 is not None:
        current.next = list1
    elif list2 is not None:
        current.next = list2

    return temp.next

list1 = LinkedList()
list1.append(1)
list1.append(2)
list1.append(4)

list2 = LinkedList()
list2.append(1)
list2.append(3)
list2.append(4)

merged_list = merge_sorted_lists(list1.head, list2.head)

while merged_list is not None:
    print(merged_list.value, end="->")
    merged_list = merged_list.next
