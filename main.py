import os, time


def clear():
    os.system('clear')


points = 0
answer = input(
"You will name the home country of each car manufacturer, difficulty will be random for every question and will be multi answer questions, press A to start    "
)
clear()
#the code below is how the quiz questions will be shown to the user

print("To make it easier they will be in groups in terms of what continent they are from")
time.sleep(2.5)
clear()
print("Europe")

time.sleep(2.5)
clear()
print("Question number One, \nWhich country is citron's home country?")

print("The possible answers are,  \nA=Belgium\nB=France\nC=Japan\nD=China")
answer = input()

if answer == 'a':
    print("Incorrect! The answer is b \n")
    print("points: ", points, "/ 1")
    print("\n")

elif answer == 'b':
    print("Correct!")
    points += 1
    print("points: ", points, "/ 1")
    print("\n")

elif answer == 'c':
    print("Incorrect! The answer is b \n")
    print("points: ", points, "/ 1")
    print("\n")

elif answer == 'd':
    print("Incorrect! The answer is b \n")
    print("points: ", points, "/ 1")
    print("\n")
#this code gives time for the user to read the answer and check their score and then clears it after 2 and seconds
time.sleep(2.0)
clear()

print("Question number two, \nWhich Country is Porsche's home country?")

print(
    "The possible answers are, \nA=Denmark\nB=Austria\nC=Germany\nD=Switzerand"
)
answer = input()

if answer == 'a':
    print("Incorrect! The answer is c \n")
    print("points: ", points, "/ 2")
    print("\n")

elif answer == 'b':
    print("Incorrect! The answer is c \n")
    print("points: ", points, "/ 2")
    print("\n")

elif answer == 'c':
    print("Correct!")
    points += 1
    print("points: ", points, "/ 2")
    print("\n")

elif answer == 'd':
    print("Incorrect! The answer is c \n")
    print("points: ", points, "/ 2")
    print("\n")

time.sleep(2.0)
clear()


print("Question number three, \nWhich Country is Ferrari's home Country?")

print("The possible answers are, \nA=Italy\nB=Yugoslavia\nC=Croatia\nD=France")
answer = input()
if answer == 'a':
    print("Correct!")
    points += 1
    print("points: ", points, "/ 3")
    print("\n")

elif answer == 'b':
    print("Incorrect! The answer is a \n")
    print("points: ", points, "/ 3")
    print("\n")

elif answer == 'c':
    print("Incorrect! The answer is a \n")
    print("points: ", points, "/ 3")
    print("\n")

elif answer == 'd':
    print("Incorrect! The answer is a \n")
    print("points: ", points, "/ 3")
    print("\n")

time.sleep(2.0)
clear()

print("Question number four, \nWhich Country is Monteverdi's home Country?")

print(
    "The possible answers are, \nA=Austria\nB=Switzerland\nC=Italy\nD=Slovenia"
)
answer = input()
if answer == 'a':
    print("Incorrect! The answer is b \n")
    print("points: ", points, "/ 4")
    print("\n")

elif answer == 'b':
    print("Correct!")
    points += 1
    print("points: ", points, "/ 4")
    print("\n")

elif answer == 'c':
    print("Incorrect! The answer is b \n")
    print("points: ", points, "/ 4")
    print("\n")

elif answer == 'd':
    print("Incorrect! The answer is b \n")
    print("points: ", points, "/ 4")
    print("\n")

time.sleep(2.0)
clear()




print("Question number five, \nWhich Country is Volvo's home Country?")

print("The possible answers are, \nA=Sweden\nB=Denmark\nC=Finland\nD=Norway")

answer = input()
if answer == 'a':
    print("Correct!")
    points += 1
    print("points: ", points, "/ 5")
    print("\n")

elif answer == 'b':
    print("Incorrect! The answer is a \n")
    print("points: ", points, "/ 5")
    print("\n")

elif answer == 'c':
    print("Incorrect! The answer is a \n")
    print("points: ", points, "/ 5")
    print("\n")

elif answer == 'd':
    print("Incorrect! The answer is a \n")
    print("points: ", points, "/ 5")
    print("\n")

time.sleep(2.0)
clear()


print("Question number six, \nWhich Country is Zenvo's home Country?")

print("The possible answers are, \nA=Spain\nB=Portugal\nC=Denmark\nD=Germany")

answer = input()

if answer == 'a':
    print("Correct!")
    points += 1
    print("points: ", points, "/ 6")
    print("\n")

elif answer == 'b':
    print("Incorrect! The answer is a \n")
    print("points: ", points, "/ 6")
    print("\n")

elif answer == 'c':
    print("Incorrect! The answer is a \n")
    print("points: ", points, "/ 6")
    print("\n")

elif answer == 'd':
    print("Incorrect! The answer is a \n")
    print("points: ", points, "/ 6")
    print("\n")

time.sleep(2.0)
clear()

print("Question number seven, \nWhich Country is Addax's home Country")

print("The possible answers are, \nA=Nederlands\nB=Poland\nC=France\nD=Belgium")


answer = input()
if answer == 'a':
    print("Incorrect! The answer is d \n")
    print("points: ", points, "/ 7")
    print("\n")

elif answer == 'b':
    print("Incorrect! The answer is d \n")
    print("points: ", points, "/ 7")
    print("\n")

elif answer == 'c':
    print("Incorrect! The answer is d \n")
    print("points: ", points, "/ 7")
    print("\n")

elif answer == 'd':
    print("Correct!")
    points += 1
    print("points: ", points, "/ 7")
    print("\n")

time.sleep(2.0)
clear()

print("Question number eight, \nWhich Country is Audi's home Country?")

print("The possible answers are, \nA=Nederlands\nB=Germany\nC=Denmark\nD=Austria")


answer = input()
if answer == 'a':
    print("Incorrect! The answer is b \n")
    print("points: ", points, "/ 8")
    print("\n")

elif answer == 'b':
    print("Correct!")
    points += 1
    print("points: ", points, "/ 8")
    print("\n")

elif answer == 'c':
    print("Incorrect! The answer is b \n")
    print("points: ", points, "/ 8")
    print("\n")

elif answer == 'd':
    print("Incorrect! The answer is b \n")
    print("points: ", points, "/ 8")
    print("\n")

time.sleep(2.0)
clear()




print("Question number nine, \nWhich Country is Maserati's home Country?")

print("The possible answers are, \nA=Serbia\nB=France\nC=Germany\nD=Italy")


answer = input()
if answer == 'a':
    print("Incorrect! The answer is d \n")
    print("points: ", points, "/ 9")
    print("\n")

elif answer == 'b':
    print("Incorrect! The answer is d \n")
    print("points: ", points, "/ 9")
    print("\n")

elif answer == 'c':
    print("Incorrect! The answer is d \n")
    print("points: ", points, "/ 9")
    print("\n")

elif answer == 'd':
    print("Correct!")
    points += 1
    print("points: ", points, "/ 9")
    print("\n")

time.sleep(2.0)
clear()

print("Asia")
time.sleep(2.5)
clear()
print("Quesion number ten, \nWhich Country is Holden's home Country?")
print(
    "The possible answers are, \nA=New Zealand\nB=Australia\nC=Solomon islands\nD=China"
)
answer = input()

if answer == 'a':
    print("Incorrect! The answer is b \n")
    print("points: ", points, "/ 10")
    print("\n")

elif answer == 'b':
    print("Correct!")
    points += 1
    print("points: ", points, "/ 10")
    print("\n")

elif answer == 'c':
    print("Incorrect! The answer is b \n")
    print("points: ", points, "/ 10")
    print("\n")

elif answer == 'd':
    print("Incorrect! The answer is b \n")
    print("points: ", points, "/ 10")
    print("\n")

time.sleep(2.0)
clear()

print("Question number eleven, \nWhich Country is Eltramco's home Country?")

print("The possible answers are, \nA=Algeria\nB=Morroco\nC=Egypt\nD=Tunisia")
answer = input()
if answer == 'a':
    print("Incorrect! The answer is c \n")
    print("points: ", points, "/ 11")
    print("\n")

elif answer == 'b':
    print("Incorrect! The answer is c \n")
    print("points: ", points, "/ 11")
    print("\n")

elif answer == 'c':
    print("Correct!")
    points += 1
    print("points: ", points, "/ 11")
    print("\n")

elif answer == 'd':
    print("Incorrect! The answer is c \n")
    print("points: ", points, "/ 11")
    print("\n")

time.sleep(2.0)
clear()

print("Question number twelve, \nWhich Country is Nissan's home Country?")

print(
    "The possible answers are, \nA=South Korea\nB=China\nC=Singapore\nD=Japan")
answer = input()
if answer == 'a':
    print("Incorrect! The answer is d \n")
    print("points: ", points, "/ 12")
    print("\n")

elif answer == 'b':
    print("Incorrect! The answer is d \n")
    print("points: ", points, "/ 12")
    print("\n")

elif answer == 'c':
    print("Incorrect! The answer is d \n")
    print("points: ", points, "/ 12")
    print("\n")

elif answer == 'd':
    print("Correct!")
    points += 1
    print("points: ", points, "/ 12")
    print("\n")

time.sleep(2.0)
clear()

print("Question number thirteen, \nWhich Country is Lexus home Country?")

print("The possible answers are, \nA=New Zealand\nB=China\nC=Japan\nD=Canada")

answer = input()
if answer == 'a':
    print("Incorrect! The answer is c \n")
    print("points: ", points, "/ 13")
    print("\n")

elif answer == 'b':
    print("Incorrect! The answer is c \n")
    print("points: ", points, "/ 13")
    print("\n")

elif answer == 'c':
    print("Correct!")
    points += 1
    print("points: ", points, "/ 13")
    print("\n")

elif answer == 'd':
    print("Incorrect! The answer is c \n")
    print("points: ", points, "/ 13")
    print("\n")

time.sleep(2.0)
clear()

print("North and South America")
time.sleep(2.5)
clear()


print("Question number twelve, \nWhich Country is Tata Motor's home Country?")

print("The possible answers are, \nA=Singapore\nB=USA\nC=India\nD=China")


answer = input()
if answer == 'a':
    print("Incorrect! The answer is c \n")
    print("points: ", points, "/ 14")
    print("\n")

elif answer == 'b':
    print("Incorrect! The answer is c \n")
    print("points: ", points, "/ 14")
    print("\n")

elif answer == 'c':
    print("Correct!")
    points += 1
    print("points: ", points, "/ 14")
    print("\n")

elif answer == 'd':
    print("Incorrect! The answer is c \n")
    print("points: ", points, "/ 14")
    print("\n")

time.sleep(2.0)
clear()

print("Question number thirteen, \nWhich Country is kamax's home Country?")

print("The possible answers are, \nA=Brazil\nB=USA\nC=Peru\nD=Bolivia")

answer = input()
if answer == 'a':
    print("Incorrect! The answer is c \n")
    print("points: ", points, "/ 15")
    print("\n")

elif answer == 'b':
    print("Incorrect! The answer is c \n")
    print("points: ", points, "/ 15")
    print("\n")

elif answer == 'c':
    print("Correct!")
    points += 1
    print("points: ", points, "/ 15")
    print("\n")

elif answer == 'd':
    print("Incorrect! The answer is c \n")
    print("points: ", points, "/ 15")
    print("\n")

time.sleep(2.0)
clear()


print("Question number ten, \nWhich Country is Agrale's home Country")

print("The possible answers are, \nA=Canada\nB=USA\nC=Argentina\nD=Brazil")


answer = input()
if answer == 'a':
    print("Incorrect! The answer is d \n")
    print("points: ", points, "/ 17")
    print("\n")

elif answer == 'b':
    print("Incorrect! The answer is d \n")
    print("points: ", points, "/ 17")
    print("\n")

elif answer == 'c':
    print("Incorrect! The answer is d \n")
    print("points: ", points, "/ 17")
    print("\n")

elif answer == 'd':
    print("Correct!")
    points += 1
    print("points: ", points, "/ 17")
    print("\n")

time.sleep(2.0)
clear()

print("Africa")
time.sleep(2.5)
clear()

print("Question number eleven, \nWhich Country is Eltramco's home Country?")

print("The possible answers are, \nA=Algeria\nB=Morroco\nC=Egypt\nD=Tunisia")
answer = input()
if answer == 'a':
    print("Incorrect! The answer is c \n")
    print("points: ", points, "/ 11")
    print("\n")

elif answer == 'b':
    print("Incorrect! The answer is c \n")
    print("points: ", points, "/ 11")
    print("\n")

elif answer == 'c':
    print("Correct!")
    points += 1
    print("points: ", points, "/ 11")
    print("\n")

elif answer == 'd':
    print("Incorrect! The answer is c \n")
    print("points: ", points, "/ 11")
    print("\n")

time.sleep(2.0)
clear()










































































































#write what the code is about at the top whgat the code does and everywhere






























































































































































































































































































































































