def factorial(number):
    result = 1
    i = 0
    while i < number:
       result = result * (i + 1)
       i += 1
    print(f"The result is: {result}")
 

print("Enter a number: ") 
number = int(input())
print(f"Your entered number is: {number}")   
factorial(number)