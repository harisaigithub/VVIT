n = int(input("Enter no.of Employees:"))
l = []
bonus = 100
total = 0
names = []
print ("...........")
for i in range (n):
    name = input("Enter Employees name: ")
    names.append(name)
    sal = int(input("Enter Employee Salary : "))
    l.append(sal)
    emp.id = int(input("Enter Employee id: "))
    exp = int(input("Enter Employee Experience : "))
    if exp <= 2:
        print ("no bonus")
    else:
        net_sal = sal + bonus
        print ("Net Salary Of The Employee Is: " , net_sal)
        print (".............")
        print("Name: Salary")
for i in range(n):
    print("Highest Salary:" , l[i])
    l = sorted (l)
    print ("Highest Salary : " , l[-1])
    print ("Lowest Salary : " , l[0])
for i in range(n):
    print(name[i], ":" , l[i])
    l = sorted(i)
    print ("Highest Salary : " , l[-1])
    print ("Lowest Salary : " , l[0])
for i in range(n):
    total = total + l [i]
    avg = total|n
    print ("avg salary is " , avg)
