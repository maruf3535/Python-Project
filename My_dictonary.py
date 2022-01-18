# Python Exercise 1 - Apni Dictionary
# Create a dictonary and take input from user and return the meaning of the word from the dictonary


"""
go = যাওয়া
come = আসাা
read = পড়া
write = লিখা
listen = শোনা
"""
myWordDic = {
    "go": "যাওয়া",
    # "Go": "যাওয়া",
    "come": "আসাা",
    # "Come": "আসাা",
    "read": "পড়া",
    # "Read": "পড়া",
    "write": "লিখা",
    # "Write": "লিখা",
    "listen": "শোনা",
    # "Listen": "শোনা"
}
enterWord = print("Enter your word: ", end="")
inputWord = input()
inputWordLower = inputWord.lower()
print(inputWord, end=" = ")
print(myWordDic.get(inputWordLower))


# Related Explore
# str1 = "maruf"
# str2 = "mAruf"
# print(str1.islower())
# print(str2.islower())
