print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[apceh]
*******************************************************************************''')
print('Welcone to Treasure island. Your mission is to find the treasure.')
first_choice = input('where u go ? left or right?').lower()
if first_choice == 'left':
    print('you still alive, keep moving')
else:
    print('Fall into a hole. Game Over.')
    exit()
second_choice = input('u see a water. what do u do ? swim or wait ?').lower()
if second_choice == 'wait':
    print('u waiting and then u see the doors')
else:
    print('u swin and attacked by trout. Game over.')
    exit()
third_choice = input('Which door ? red, blue or yellow?').lower()
if third_choice == 'yellow':
    print('You win! Congratulations!')
elif third_choice == 'blue':
    print('Eaten by beasts. Game over')
    exit()
elif third_choice == 'red':
    print('Burned by fire. Game over')
    exit()
else:
    print('game over')
    exit()
print('First game from 100 days of code challenge epta')