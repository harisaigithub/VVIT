s = input("Enter a String:")
d = {}
if s.isspace():
    print("String Is Empty. ")
elif s. isdigit():
    print("Enter Charcters only: ")
else:
    for i in s:
        d[i] = s.count(i)
        print(d)
