import os
def clear():
  os.system('clear')
answer=input("you will name the home country of each car manufacturer, it will get harder every question and will be multi answer questions... press A to start")
clear()

points = 0
if answer.lower() == "a":
  answer = "a"


print("Question number One, \nWhich country is citron's home country?")

print("The possible answers are,  \nA=Belgium\nB=France\nC=Japan\nD=China")
answer=input()



if answer == 'a':
    points -= 0
    print('This answer is false, your points: {}'.format(points))

elif answer == 'b':
      
      points += 1
      print('This answer is correct, your points: {}'.format(points))

elif answer == 'c':
      
      points -= 0
      print('This answer is false, your points: {}'.format(points))

elif answer == 'd':
      
      points -= 0
      print('This answer is false, your points: {}'.format(points))

clear()











#check examplar for help on how to do the answers do the code to remember what to check and make sure to get the code from thje exemplar
#1. how to make score board
#2. how to make multi answers the only answers that wprk