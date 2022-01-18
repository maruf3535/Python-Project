
print("Enter 1st number: ")
a = int(input())
print("Enter 2nd number: ")
b = int(input())
print("Enter 3rd number: ")
c = int(input())
smallNumberValue = None

# Find the smallest number in these 3 numbers.
def smallest_number(a, b, c):
    if a < b:
        if a < c:
            print(f"a = {a} is the smallest number in this sequence.")
            return "a"
        elif c < a:
            print(f"c = {c} is the smallest number in this sequence.")
            return "c"
    elif b < a:
        if b < c:
            print(f"b = {b} is the smallest number in this sequence.")
            return "b"
        elif c < b:
            print("c = {c} is the smallest number in this sequence.")
            return "c"

# Find the middle number in these 3 numbers.
def middle_number(a, b, c):
    # Justify middle number for 'a'.
    if (a > c) and (a < b):
        print(f"a = {a} is the middle number in this sequence.")
        return "a"
    elif (a < c) and (a > b):
        print(f"a = {a} is the middle number in this sequence.")
        return "a"


    # Justify middle number for 'b'.
    elif (b > a) and (b < c):
        print(f"b = {b} is the middle number in this sequence.")
        return "b"
    elif (b < a) and (b > c):
        print(f"b = {b} is the middle number in this sequence.")
        return "b"


    # Justify middle number for 'c'.
    elif (c > a) and (c < b):
        print(f"c = {c} is the middle number in this sequence.")
        return "c"
    elif (c < a) and (c > b):
        print(f"c = {c} is the middle number in this sequence.")
        return "c"

# Find the largest number in these 3 numbers.
def largest_number(a, b, c):
    if a > b:
        if a > c:
            print(f"a = {a} is the largest number in this sequence.")
            return "a"
        elif c > a:
            print(f"c = {c} is the largest number in this sequence.")
            return "c"
    elif b > a:
        if b > c:
            print(f"b = {b} is the largest number in this sequence.")
            return "b"
        elif c > b:
            print(f"c = {c} is the largest number in this sequence.")
            return "c"


smallNumber = smallest_number(a, b, c)
middleNumber = middle_number(a, b, c)
largeNumber = largest_number(a, b, c)
print(f"{smallNumber} < {middleNumber} < {largeNumber}")
print(f"{largeNumber} > {middleNumber} > {smallNumber}")
