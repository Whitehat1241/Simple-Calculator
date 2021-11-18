# Schneider Theodule

# Integration 1: Program will calculate basic math function
# Integration 2: This program will also take the square root and perform quadratic equations

import math
import time


def functions(one, two, three, four, five, six, seven, eight):
    print(one + two + three + four + five + six + seven + eight)
       
        
# Loop to preform multiple operations at once
start = input("To begin, select any key followed by the enter button: ",)
beginList = {start}


for start in beginList:

    a = 'SELECT'
    b = 'OPERATION'
    greeting = [a, b]
    print("Starting in")
    count = 3

    for e in range(3):
        print(count, '...')
        time.sleep(1)
        count -= 1
    print(*greeting, sep=" AN ", end="\n    -------\n", )
    
    while True:
        functions("q or Q: QUIT\n", "1: Addition\n", "2: Subtraction\n"
                  , "3: Multiplication\n", "4: Division\n"
                  , "5: Raise to a Power\n", "6: Square Root\n"
                  , "7: Quadratic formula")
        
        options = ['1', '2', '3', '4', '5', '6', '7', 'q', 'Q']

        choice = input("Enter Your Choice: ", )

        if choice in options:
            try:
                # Check for which operation is selected & what to do
                if int(choice) == 1:  # Addition
                    num1 = float(input("Enter Number 1: ", ))
                    num2 = float(input("Enter Number 2: ", ))
                    num1 += num2
                    print("----------------------------")
                    print(num1, "+", num2, "=", num1)
                    print("----------------------------")

                elif int(choice) == 2:  # Subtraction
                    num1 = float(input("Enter Number 1: ", ))
                    num2 = float(input("Enter Number 2: ", ))
                    print("----------------------------")
                    print(num1, "-", num2, "=", (num1 - num2))
                    print("----------------------------")

                elif int(choice) == 3:  # Multiplication
                    num1 = float(input("Enter Number 1: ", ))
                    num2 = float(input("Enter Number 2: ", ))
                    print("----------------------------")
                    print(num1, "*", num2, "=", (num1 * num2))
                    print("----------------------------")

                elif int(choice) == 4:  # Division
                    try:
                        num1 = float(input("Enter Number 1: ", ))
                        num2 = float(input("Enter Number 2: ", ))
                        if num2 == 0.0:  # Checking if user selects 0.0
                            print("ERROR: DIVIDE BY 0")
                        else:
                            print("----------------------------")
                            print("Result: {} / {} = {:.2f}".format(num1, num2, num1 / num2))
                            print("\nRemainder :", (num1 % num2))
                            print("----------------------------")
                    except:
                        print("ERROR")

                elif int(choice) == 5:  # Raising to a Power
                    num1 = float(input("Enter Number 1: ", ))
                    power = float(input("Enter Power: ", ))
                    answer = "{:.9f}".format(num1 ** power)
                    print("----------------------------")
                    print("Result: ", answer)
                    print("----------------------------")

                elif int(choice) == 6:  # Square Root
                        try:
                            num1 = float(input("Enter Power of Root: ", ))
                            num2 = float(input("Enter the Radicand:", ))
                            if num1 >= 0:
                                answer = "{:.9f}".format(num2 ** (1 / num1))  # add code: print int if answer is whole #
                                print("----------------------------")
                                print("Result: ", answer)
                                print("----------------------------")
                            else:
                                print("ERROR")    
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
                            if (f > 0) or (f == 0):  # This part will return a value if (b**2) > (4 * a * c) or else it
                                # will be an imaginary value

                                solution1 = (-b + math.sqrt(f)) / (2 * a)
                                solution2 = (-b - math.sqrt(f)) / (2 * a)
                                answer = "ROOTS EQUAL: {:.10f} and {:.10f}".format(solution1, solution2)
                                print("---------------------------------------------------------")
                                print("Result: ", answer)  # Answer will have 10 numbers// 10 after decimal and 10
                                # with decimal
                                print("---------------------------------------------------------")
                                possible = not True
                                
                            elif (b ** 2) < (4 * a * c):
                                print("ERROR: NON-REAL ANSWER", "\n    XXXXXXX    ")
                                break
                        else:
                            break
            except:
                if str(choice) != 'q' and str(choice) != 'Q':
                    print("Invalid")
                else:
                    print("Done!")
                    break
        else:
            print("   XXXX-XXXX-XXXX-XXXX  ", "\nINVALID INPUT: TRY AGAIN!", )
            print("     -------")


# ****import parser? what is that

# **** An operating system is software/program that acts as an interface between the user and the computer hardware
# controls the execution of all kinds of programs*****


# Got help from:

    # Integration 1:

        # LearningLad on youtube:   https://www.youtube.com/watch?v=5_CAo_C523g

        # Paulo Drefahl: strings & if else statements:   https://www.w3schools.com/python/python_strings.asp

        # 'Sep =' & 'end =': https://blog.finxter.com/the-separator-and-end-arguments-of-the-python-print-function/

    # Integration 2

        # quadratic formula: https://www.youtube.com/watch?v=qXW-9jYYja8

        # Jakeb Brown: while loops, formatting, algorithmic fixes

