"""
Hints:
# Treasure Island Flow Chart: https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
# Add your own ASCII art: https://ascii.co.uk/art
"""

print('''
*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

first = input("Left or right?\nType Right/Left: ").lower()
if first == "right":
  print('''                      -     =    .--._
                - - ~_=  =~_- = - `.  `-.
              ==~_ = =_  ~ -   =  .-'    `.
            --=~_ - ~  == - =   .'      _..:._
           ---=~ _~  = =-  =   `.  .--.'      `.
          --=_-=- ~= _ - =  -  _.'  `.      .--.:
            -=_~ -- = =  ~-  .'      :     :    :
             -=-_ ~=  = - _-`--.     :  .--:    D
               -=~ _=  =  -~_=  `;  .'.:   ,`---'@
             --=_= = ~-   -=   .'  .'  `._ `-.__.'
            --== ~_ - =  =-  .'  .'     _.`---'
           --=~_= = - = ~  .'--''   .   `-..__.--.
             --==~ _= - ~-=  =-~_-   `-..___(  ===;
          --==~_==- =__ ~-=  - -    .'       `---'
  ''')
  print("Sonic got the treasure before you, try again.")
elif first == 'left':
  print('''
   _                                                           
  | |                                                          
  | |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ __ ___   __ _ _ __  
  | __| '__/ _ \/ _` / __| | | | '__/ _ \ '_ ` _ \ / _` | '_ \ 
  | |_| | |  __/ (_| \__ \ |_| | | |  __/ | | | | | (_| | |_) |
  \__|_|  \___|\__,_|___/\__,_|_|  \___|_| |_| |_|\__,_| .__/ 
                                                        | |    
                                                        |_| 
  ''')
  print("Nice, you made it to the next level!")

  second = input("Your map shows that you need to get to Treasure Island, you can wait to board a ship or swim accross the sea, pick one.\nType Swim/Wait: ").lower()
  if second == "swim":
    print('''
                    (`.
                    \ `.
                      )  `._..---._
    \`.       __...---`         o  )
    \ `._,--'           ,    ___,'
      ) ,-._          \  )   _,-'
    /,'    ``--.._____\/--''
        ''')
    print("Unfortunately, you were eaten by a Great White Shark, try again.")
  elif second == "wait":
    print("Nice, you made it to the next level, you're pretty good at this!")
    print ("Welcome to:")
    print ('''
     _                                     _     _                 _ 
    | |                                   (_)   | |               | |
    | |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
    | __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
    | |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
    \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
    ''')

    third = input("Now that you've made it to Treasure Island, you can dig or search the cave. \n Type Dig/Cave: ").lower()
    if third == "dig":
      print("You've found the treasure, you win!")
    elif third == "cave":
      print('''
      _                     
      | |                    
      | |__   ___  __ _ _ __ 
      | '_ \ / _ \/ _` | '__|
      | |_) |  __/ (_| | |   
      |_.__/ \___|\__,_|_|   
                  ''')
      print("You were eaten by a bear, game over.")
