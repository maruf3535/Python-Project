# Exercise 5: Health Management System


import time

print("This is a Health Management System project from 'Code With Harry' YouTube channel.")
print("You have 3 clients.\n1. Maruf.\t2.Rafsan.\t3.Shihab.")
print("Enter your name: ")
clientName = input().capitalize()
print('\033[1A')
print(f"Your name is '{clientName}'")

# Function for Maruf
def maruf():
    print("What does you want to do?\n1. Log.\n2. Retrieve.")
    clientOption = input() # Log or Retrieve
    print("\033[1A") # Cursor up for one line
    if clientOption == "1":
        print("You want to 'Log'", "\nPlease choose one of these options:\n1. Diet. 2. Exercise.")
        clientActivityLog = input()
        print("\033[1A") # Cursor up for one line
        if clientActivityLog == "1":
            print("Maruf, now you can input your Diet activity in your file.")
            marufDietLogOpen = open("tutorial32MarufDiet.txt", "a")
            marufDietLogInput = input()
            marufDietLogWriteTime = str(time.ctime()) + ": "
            marufDietLogOpen.write(marufDietLogWriteTime + marufDietLogInput + "\n")
            marufDietLogOpen.close()
        elif clientActivityLog == "2":
            print("Maruf, now you can input your Exercise activity in your file.")
            marufExerciseLogOpen = open("tutorial32MarufExercise.txt", "a")
            marufExerciseLogInput = input()
            marufExerciseLogWriteTime = str(time.ctime()) + ": "
            marufExerciseLogOpen.write(marufExerciseLogWriteTime + marufExerciseLogInput + "\n")
            marufExerciseLogOpen.close()
    elif clientOption == "2":
        print("Maruf, You want to 'Retrieve'\nPlease choose one of these options:\n1. Diet. 2. Exercise.")
        clientActivityRetrieve = input()
        if clientActivityRetrieve == "1":
            marufDietRetrieveOpen = open("tutorial32MarufDiet.txt")
            marufDietRetrieveRead = marufDietRetrieveOpen.readlines()
            for i in marufDietRetrieveRead:
                print("\033[1A", i) # Cursor up for one line
            marufDietRetrieveOpen.close()
        elif clientActivityRetrieve == "2":
            marufExerciseRetrieveOpen = open("tutorial32MarufExercise.txt")
            marufExerciseRetrieveRead = marufExerciseRetrieveOpen.readlines()
            for i in marufExerciseRetrieveRead:
                print("\033[1A", i) # Cursor up for one line
            marufExerciseRetrieveOpen.close()

# Function for Rafsan
def rafsan():
    print("What does you want to do?\n1. Log.\n2. Retrieve.")
    clientOption = input() # Log or Retrieve
    print("\033[1A") # Cursor up for one line
    if clientOption == "1":
        print("You want to 'Log'", "\nPlease choose one of these options:\n1. Diet. 2. Exercise.")
        clientActivityLog = input()
        print("\033[1A") # Cursor up for one line
        if clientActivityLog == "1":
            print("Rafsan, now you can input your Diet activity in your file.")
            rafsanDietLogOpen = open("tutorial32RafsanDiet.txt", "a")
            rafsanDietLogInput = input()
            rafsanDietLogWriteTime = str(time.ctime()) + ": "
            rafsanDietLogOpen.write(rafsanDietLogWriteTime + rafsanDietLogInput + "\n")
            rafsanDietLogOpen.close()
        elif clientActivityLog == "2":
            print("Rafsan, now you can input your Exercise activity in your file.")
            rafsanExerciseLogOpen = open("tutorial32RafsanExercise.txt", "a")
            rafsanExerciseLogInput = input()
            rafsanExerciseLogWriteTime = str(time.ctime()) + ": "
            rafsanExerciseLogOpen.write(rafsanExerciseLogWriteTime + rafsanExerciseLogInput + "\n")
            rafsanExerciseLogOpen.close()
    elif clientOption == "2":
        print("Rafsan, You want to 'Retrieve'\nPlease choose one of these options:\n1. Diet. 2. Exercise.")
        clientActivityRetrieve = input()
        if clientActivityRetrieve == "1":
            rafsanDietRetrieveOpen = open("tutorial32RafsanDiet.txt")
            rafsanDietRetrieveRead = rafsanDietRetrieveOpen.readlines()
            for i in rafsanDietRetrieveRead:
                print("\033[1A", i) # Cursor up for one line
            rafsanDietRetrieveOpen.close()
        elif clientActivityRetrieve == "2":
            rafsanExerciseRetrieveOpen = open("tutorial32RafsanExercise.txt")
            rafsanExerciseRetrieveRead = rafsanExerciseRetrieveOpen.readlines()
            for i in rafsanExerciseRetrieveRead:
                print("\033[1A", i) # Cursor up for one line
            rafsanExerciseRetrieveOpen.close()

# Function for Shihab
def shihab():
    print("What does you want to do?\n1. Log.\n2. Retrieve.")
    clientOption = input() # Log or Retrieve
    print("\033[1A") # Cursor up for one line
    if clientOption == "1":
        print("You want to 'Log'", "\nPlease choose one of these options:\n1. Diet. 2. Exercise.")
        clientActivityLog = input()
        print("\033[1A") # Cursor up for one line
        if clientActivityLog == "1":
            print("Shihab, now you can input your Diet activity in your file.")
            shihabDietLogOpen = open("tutorial32ShihabDiet.txt", "a")
            shihabDietLogInput = input()
            shihabDietLogWriteTime = str(time.ctime()) + ": "
            shihabDietLogOpen.write(shihabDietLogWriteTime + shihabDietLogInput + "\n")
            shihabDietLogOpen.close()
        elif clientActivityLog == "2":
            print("Shihab, now you can input your Exercise activity in your file.")
            shihabExerciseLogOpen = open("tutorial32ShihabExercise.txt", "a")
            shihabExerciseLogInput = input()
            shihabExerciseLogWriteTime = str(time.ctime()) + ": "
            shihabExerciseLogOpen.write(shihabExerciseLogWriteTime + shihabExerciseLogInput + "\n")
            shihabExerciseLogOpen.close()
    elif clientOption == "2":
        print("Shihab, You want to 'Retrieve'\nPlease choose one of these options:\n1. Diet. 2. Exercise.")
        clientActivityRetrieve = input()
        if clientActivityRetrieve == "1":
            shihabDietRetrieveOpen = open("tutorial32ShihabDiet.txt")
            shihabDietRetrieveRead = shihabDietRetrieveOpen.readlines()
            for i in shihabDietRetrieveRead:
                print("\033[1A", i) # Cursor up for one line
            shihabDietRetrieveOpen.close()
        elif clientActivityRetrieve == "2":
            shihabExerciseRetrieveOpen = open("tutorial32ShihabExercise.txt")
            shihabExerciseRetrieveRead = shihabExerciseRetrieveOpen.readlines()
            for i in shihabExerciseRetrieveRead:
                print("\033[1A", i) # Cursor up for one line
            shihabExerciseRetrieveOpen.close()
if clientName == "Maruf":
    maruf()
elif clientName == "Shihab":
    shihab()
elif clientName == "Rafsan":
    rafsan()








# Explore


# from datetime import datetime as d
# date = d.now()
# print(date.strftime("%Y-%d-%m %H:%M:%S"))



# import time
# import datetime
# print(time.time())
# # 1586813438.419919
# print(time.ctime())
# # Mon Apr 13 23:30:38 2020
# print(datetime.datetime.now())
# # 2021-11-13 23:30:38.419951
# print(datetime.date.today())
# # 2021-11-13

# Text = "Python is easy"
# print(Text.capitalize())



# import sys
# myName = input()
# sys.stdout.write("\033[F") # Cursor up one line
# print("My name is:" + myName)




# # x = range(6)

# a = ["maruf", "rafsan", "shihab"]

# for n in a:
#   print(n)