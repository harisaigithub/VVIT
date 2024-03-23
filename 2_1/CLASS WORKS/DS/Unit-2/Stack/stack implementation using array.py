import sys
from array import *
a = array ('i', [])
while True:
    print("1.push 2.pop 3. Display 4.Exit")
    ch = int(input("Enter your choice"))
    if ch == 1:
        ele = int (input("Enter Element"))
        a.append(ele)
        print ("Inserted")
    elif ch == 2:
        if len (a) == 0:
            print ("stack is empty")
        else:
              print ("Deleted element is", a.pop())
    elif ch == 3:
         if len (a) == 0:
            print ("stack is empty")
         else:
             print ("The Element In The Stack is")
             for i in a:
                 print (i)
    elif ch == 4:
        sys.exit ()
    else:
        print ("Invalid Choice")