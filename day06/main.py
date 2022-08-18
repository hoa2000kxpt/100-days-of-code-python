def turn_right():    
    turn_left()
    turn_left()
    turn_left()

# Draw Square
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()

while front_is_clear():
    move()
turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

# CHALLENGE: THE HURDLES LOOP CHALLENGE
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def go_to_final_road():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

step = 0
while step < 6:
    go_to_final_road()
    step = step + 1


#Challgen
def turn_right():
    turn_left()
    turn_left()
    turn_left()


while front_is_clear():
    move()
turn_left()

while front_is_clear():
    move()
turn_left()

while front_is_clear():
    move()
turn_left()

while front_is_clear():
    move()
turn_left()

move()
move()
move()
move()











