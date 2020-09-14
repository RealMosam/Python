list = input("Enter a list elements separated by space:").split()

print("Your list is:", list)
# Calculating the sum of input list elements
sum = 0
for i in list:
#Exception for string elements entered
    try:
        sum = sum + int(i)
    except:
        print("Enter only integer values")

print("Sum of list elements=", sum)