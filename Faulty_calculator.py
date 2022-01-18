# Python Exercise 2 - Faulty Calculator


print("Please choose one of these options:\n1. Addition.\n2. Subtraction.\n3. Multiplication.\n4. Division.")
option1 = int(input())
first = int(input())
second = int(input())
if option1 == 1:
    if first == 56 and second == 9:
        print("The result of addition is 77")
    else:
        add = first + second
        print("The result of addition is", add)
elif option1 == 2:
    subtraction = first - second
    print("The result of subtraction is", subtraction)
elif option1 == 3:
    if first == 45 and second == 3:
        print("The result of multiplication is 555")
    else:
        multiplication = first * second
        print("The result of multiplication is", multiplication)
elif option1 == 4:
    if second == 0:
        print("The second input cann't be 0 (zero)")
    elif first == 56 and second == 6:
        print("The result of division is 4")
    else:
        division = first / second
        print("The result of division  is", division)
