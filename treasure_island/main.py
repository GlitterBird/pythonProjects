treasure = ('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************''')
print(treasure)
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
direction = input("Choose a direction. Left or right? ")
if direction == "right" or direction == "Right":
  print("You fell into a hole. Game over.")
elif direction == "left" or direction == "Left":
  option2 = input("Would you like to swim or wait? ")
  if option2 == "wait" or option2 == "Wait":
    doorColor = input("Which door color? ")
    if doorColor == "Red" or doorColor == "red":
      print("Burned by fire. Game Over.")
    elif doorColor == "blue" or doorColor == "Blue":
      print("Eaten by beasts. Game Over.")
    elif doorColor == "Yellow" or doorColor == "yellow":
      print("You win!")
    else:
      print("A color of that door doesn't exist LOL.\nGame Over.")
  else:
    print("Attacked by trout. Game Over.")
else:
  print("I don't understand. Please rerun the program again.")
