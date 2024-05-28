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
choice1 = input('You\'re at a crossroad, where do you want to go ? Type "left" or "right".').lower()
if choice1 == 'left':
    choice2 = input('You come to lake. There is an island in the middle of the lake.Type wait or swim ? ').lower()
    if choice2 == 'wait':
        choice3 = input('You arrive at the island inharmed. There is house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ').lower()
        if choice3 == 'yellow':
            print('You found the treasure! You win!')
        elif choice3 == 'red':
            print('Its a room full of fire. Game over')
        elif choice3 == 'blue':
            print('its a room full a water. Game over!')
        else:
            print('u have to be choose the door, u didnt. Game over')
    else:
        print('You got attacked by angry trout. Game over')
else:
    print('You fell into a hole. Game over')