import sys

try:
    nums = [int(x) for x in input("Enter the numbers: ").split()]
except Exception as e:
    print("Enter only integer values!", e.__class__, "occurred.")
    sys.exit("Program will exit.")

nums.sort() # Ascending sort
print("Ascending order:",nums)

nums.sort(reverse=True)  # Descending sort
print("Descending order:", nums)


