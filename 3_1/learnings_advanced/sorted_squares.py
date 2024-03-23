sequence = input("Enter the sequence of numbers: ")
numbers = sequence.split()  
print("numbers:" , numbers)
sorted_numbers = sorted(numbers)
print("sorted_numbers:" , sorted_numbers)
square_numbers = [int (num) **2 for num in sorted_numbers]
print ("square_numbers:" , square_numbers)
