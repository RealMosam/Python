print("Welcome to the calculator!")

try:
    n1 = float(input("Enter the First No.:"))
except ValueError:
    print("Error: Enter a proper number")
    exit()

try:
    n2 = float(input("Enter the Second No.:"))
except ValueError:
    print("Error: Enter a proper number")
    exit()

print("Enter the Operation you want to perform:\n" ""
      "1. + For Addition\n"
      "2. - For Subtraction\n"
      "3. * For Multiplication\n"
      "4. / For Division")

op = input()

f = open("my_cal_ans.txt", "w")

if op == "+":
    add = n1+n2
    print("Addition is:", add)
    f.write(str(add))
elif op == "-":
    sub = n1-n2
    print("Subtraction is:", sub)
    f.write(str(sub))
elif op == "*":
    mul = n1*n2
    print("Multiplication is:", mul)
    f.write(str(mul))
elif op == "/":
    try:
        div = n1/n2
        print("Division is:", div)
        f.write(str(div))
    except ZeroDivisionError:
        print("Error: Cannot Divide by 0.")
else:
    print("Error: Select the proper operation.")
