sequence = input("Enter the sequence of numbers: ")
numbers = sequence.split()  

count = 0
for num in numbers:
    if len(str(num)) % 2 == 0:
        count += 1

print("Count of numbers with even number of digits:", count)

