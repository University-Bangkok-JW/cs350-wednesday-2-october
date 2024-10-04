class Node:
    def __init__(self, data=None):
        self.data = data
        self.nextNode = None

class SLinkedList:
    def __init__(self):
        self.headNode = None

    def printLinkedList(self):
        cur = self.headNode
        while cur is not None:
            print(cur.data)
            cur = cur.nextNode

array = [1, 2, 3, 4, 5]
list = SLinkedList()

for data in array:
    newNode = Node(data)
    if list.headNode is None:
        list.headNode = newNode
        cur = list.headNode
    else:
        cur.nextNode = newNode
        cur = cur.nextNode

list.printLinkedList()

newNode = Node(0)
cur = list.headNode

while cur.nextNode is not None:
    cur = cur.nextNode

cur.nextNode = newNode