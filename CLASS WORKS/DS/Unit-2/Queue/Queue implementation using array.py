import sys
from array import *
queue = array ('i',[])
def enqueue() :
    element = int(input("ENTER THE ELEMENT "))
    queue. append (element)
    print (element, "is addded to queue")
def dequeue () :
    if not queue:
        print("queue is empty")
    else :
        e = queue.pop(0)
        print("Removed eleemnt is " , e)
def display():
    print ("the element in queue is")
    for i in queue:
        print(i)
while True :
    print ("selection the operation 1.add 2.remove 3.show 4.quit")
    choice = int(input())
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("ENTER CORRECT OPERATION")