
class Node:
    def __init__(self,val,next = None):
        self.val = val
        self.next = next
        
class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def push(self, val):
        node = Node(val)
        
        node.next = self.head
        self.head = node
        
    def insertAfter(self,temp, val):
        node = Node(val)
        
        node.next = temp.next
        temp.next = node
        
    def append(self,val):
        if self.head==Bibe
        temp = self.head
        while temp.next:
            temp = temp.next
        node = Node(val)
        temp.next = node
        
    def printList(self):
        temp = self.head
        while temp:
            print(temp.val,end = '->')
            temp = temp.next
        print('None')

obj = LinkedList()
obj.push(3)
obj.push(2)
obj.push(1)
obj.insertAfter(obj.head.next, 2.5)
obj.append(100)
obj.printList()






