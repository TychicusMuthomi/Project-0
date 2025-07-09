while True:
     try:
        num_1 = int(input("Enter first number: "))
        num_2 = int(input("Enter the second number: "))
        operator = input("Enter an operator(+,-,/,*): ")
        if operator== "+":
            print(f"The sum of {num_1} and {num_2} is {num_1+num_2}")
        elif operator == "-":
            print(f"The subtraction of {num_1} and {num_2} is {num_1- num_2}")
        elif operator == "/":
            print(f"The division of {num_1} by {num_2} is {num_1/num_2}")
        elif operator == "*":
            print(f"The multiplication of {num_1} and {num_2} is {num_2 * num_1}")
     except ValueError:
         print("Invalid input")
     except ZeroDivisionError:
         print("The first number cannot be divided by 0 ")
     ex = input("Would you like to exit: (y/n)")
     if ex == "y":
         break
     else:
         continue