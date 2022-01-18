# Python Exercise 4: Astrologer's Stars


print("How many rows do you want?")
rowsNumber = int(input())
print("Do you want to print this pattern in reverse or not? '0' for reverse and '1' for default.")
reverseINT = int(input())
reverseBOOL = bool(reverseINT)
i = 1
jDefault = 1
jReverse = rowsNumber

if reverseBOOL == True :
    # Default Printing Pattern
    while i <= rowsNumber:
        while jDefault <= i:
            print("*", end="")
            jDefault += 1
        print("")
        jDefault = 1
        i += 1
elif reverseBOOL == False:
    # Reverse Printing Pattern
    while i <= rowsNumber:
        while jReverse >= i:
            print("*", end="")
            jReverse -= 1
        print("")
        jReverse = rowsNumber
        i += 1

