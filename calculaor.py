num1 = float(input("Put your first number here :"))
num2 = float(input("Put your second number here : "))
operator = input("Enter 1 for sum , 2 for subraction , 3 for multiplication, 4 for divistion, 5 for reminder of two numbers : ")


if operator == "1":
    print("The sum will be : " + str(num1 + num2))
elif operator == "2":
    print("The subraction will be : "  + str(num1 - num2))
elif operator == "3":
    print("The product will be : " + str(num1 * num2))
elif operator == "4":
    print("The division will be : " + str(num1 / num2))
elif operator == "5":
    print("The reminder will be : " + str(num1 % num2))
else:
    print("Invalid input")
