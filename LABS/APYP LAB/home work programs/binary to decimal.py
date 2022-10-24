binary_num = int(input("Enter the Binary Number: "))
dec_num = 0
m = 1
length = len(str(binary_num))

for k in range(length):
    reminder = binary_num % 10
    dec_num = dec_num + (reminder * m)
    m = m * 2
    binary_num = int(binary_num/10)

print("Equivalent Decimal Value = ", dec_num)
