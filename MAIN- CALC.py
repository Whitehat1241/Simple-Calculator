# Schneider Theodule
# Program will calculate basic math function (Integration 1)
# This program will also take the square root and perform quadratic equations (Integration 2)


import math

# Loop to preform multiple operations at once
a = 'SELECT'
b = 'OPERATION'
greeting = [a, b]
print(*greeting, sep=" AN ", end="\n    -------\n", )
while True:

    # Define Operations
    print("q or Q: QUIT")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Raise to a Power")
    print("6: Square Root")
    print("7: Quadratic formula", end="\n     -------\n")
    options = ['1', '2', '3', '4', '5', '6', '7', 'q', 'Q']

    choice = input("Enter Your Choice: ", )

    if choice in options:
        try:
            # Check for which operation is selected & what to do
            if int(choice) == 1:  # Addition
                num1 = float(input("Enter Number 1: ", ))
                num2 = float(input("Enter Number 2: ", ))
                print(num1, "+", num2, "=", (num1 + num2))

            elif int(choice) == 2:  # Subtraction
                num1 = float(input("Enter Number 1: ", ))
                num2 = float(input("Enter Number 2: ", ))
                print(num1, "-", num2, "=", (num1 - num2))

            elif int(choice) == 3:  # Multiplication
                num1 = float(input("Enter Number 1: ", ))
                num2 = float(input("Enter Number 2: ", ))
                print(num1, "*", num2, "=", (num1 * num2))

            elif int(choice) == 4:  # Division
                try:
                    num1 = float(input("Enter Number 1: ", ))
                    num2 = float(input("Enter Number 2: ", ))
                    if num2 == 0.0:  # Checking if user selects 0.0
                        print("ERROR: DIVIDE BY 0")
                    else:
                        print("\nResult: {} / {} = {:.2f}".format(num1, num2, num1 / num2))
                        print("\nRemainder :", (num1 % num2))
                except:
                    print("ERROR")

            elif int(choice) == 5:  # Raising to a Power
                num1 = float(input("Enter Number 1: ", ))
                num2 = float(input("Enter Number 2: ", ))
                print(num1, "**", num2, "=", (num1 ** num2))

            elif int(choice) == 6:  # Square Root
                while True:
                    try:
                        num1 = float(input("Enter Power of Root: ", ))
                        num2 = float(input("Enter the Radicand:", ))
                        print(int(num1), "√", int(num2), " = ", num2 ** (1 / num1))
                        break
                    except:
                        pass

            elif int(choice) == 7:  # Quadratic Formula
                possible = True
                while possible:

                    a = float(input("a=? ", ))
                    b = float(input("b=? ", ))
                    c = float(input("c=? ", ))
                    d = (b ** 2)
                    e = (4 * a * c)  # For final project, delete variables d & e// change variable f to d----|
                    f = d - e
                    if (d != 0) and (d > e):
                        if (f > 0) or (f == 0):  # This part will return a value if (b**2) > (4 * a * c) or else it will
                                                # be an imaginary value

                            solution1 = (-b + math.sqrt(f)) / (2 * a)
                            solution2 = (-b - math.sqrt(f)) / (2 * a)
                            answer = "ROOTS EQUAL: {:.10f} and {:.10f}".format(solution1, solution2)
                            print("Result: ", answer)  # I want answer to have 10 numbers// 10 after decimal and 10
                                                                # with decimal

                            print("Done!", end="\n     -------\n")
                            possible = not True
                        elif (b ** 2) < (4 * a * c):
                            print("ERROR: NON-REAL ANSWER", "\n    XXXXXXX    ")
                            break
                    else:
                        pass
        except:
            if str(choice) == 'q' or str(choice) == 'Q':
                print("Done!")
                break
            else:
                print("Invalid")
    else:
        print("   XXXX-XXXX-XXXX-XXXX  ", "\nINVALID INPUT: TRY AGAIN!", )
        print("     -------")


# ****import parser? what is that


# Got help from:

    # Integration 1:

        # LearningLad on youtube:   https://www.youtube.com/watch?v=5_CAo_C523g

        # Paulo Drefahl: strings & if else statements:   https://www.w3schools.com/python/python_strings.asp

        # 'Sep =' & 'end =': https://blog.finxter.com/the-separator-and-end-arguments-of-the-python-print-function/

    # Integration 2

        # quadratic formula: https://www.youtube.com/watch?v=qXW-9jYYja8

        # Jakeb Brown: while loops, formatting, algorithmic fixes
