class Node:
    def __init__(self, data):
     self.data = data
     self.next = None
    
class LinkedList:
    def __init__(self):
      self.head = None
    def printll(self):
      if self.head is None:
          print("The linked list is empty ")
      else :
         n = self.head
      while n is not None :
          print(n .data)
          n = n.ref
          ll1 = linkedlist()
          ll1 = printll()
    def add_begin(self,data):
      new_Node = Node(data)
      new_Node = self.head
      self.head = new_Node
ll1 = LinkedList ()    
ll1.add_begin(10)
ll1.add_begin(20)
ll1.add_begin(30)
ll1.printll()