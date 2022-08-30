"""
Challenge 1: Home 1
"""
move()
move()

"""
Challenge 2: Home 2
"""
move()
move()

"""
Challenge 3: Home 3
"""
move()
move()
turn_left()
move()

"""
Challenge 4: Home 4
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def three_steps():
    move()
    move()
    move()

three_steps()
turn_left()
three_steps()
turn_right()
move()
turn_right()
three_steps()
turn_left()
three_steps()
turn_right()
move()
turn_right()
three_steps()
turn_left()
three_steps()
turn_right()
move()
turn_right()
three_steps()
turn_left()
three_steps()

"""
Challenge 5: Around 1
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def go_straight():
    move()
    move()
    move()
    move()
    move()
    move()
    move()
    move()
    move()


for i in range(4):
    go_straight()
    turn_left()

"""
Challenge 6: Around 1 - variable
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def move_left():
    while front_is_clear():
        move()
    turn_left()


# Create an object
put()

# Go to the road 3 times
for i in range(3):
    go_around()

# Keep moving until the robot finds the object
while front_is_clear():
    move()
    if object_here():
        done()

"""
Challenge 7: Around 1 - apple
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()


for i in range(4):
    while front_is_clear():
        move()
        if object_here():
            take()
    turn_left()

"""
Challenge 8: Around 2
"""


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def move_left():
    while front_is_clear():
        move()
    turn_left()


# Create an object
put()

for k in range(2):
    move_left()

for i in range(5):
    move()
turn_right()

for j in range(3):
    move_left()

while front_is_clear():
    move()
    if object_here():
        done()

"""
Challenge 10: Around 3
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_left():
    while front_is_clear():
        move()
    turn_left()

put()
if wall_in_front():
    turn_left()
move()
turn_right()
move()
move()
turn_right()
move()
turn_left()
for i in range(2):
    move_left()

for j in range(5):
    move()
turn_right()

for k in range(3):
    move_left()

while front_is_clear():
    move()
    if object_here():
        done()

"""
Challenge 11: Around 4 
"""

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_left():
    while front_is_clear():
        move()
    turn_left()

put()
turn_left()
turn_left()
move()
turn_right()
move()
move()
turn_right()
move()
move()
move()
turn_right()
move()
move()
turn_left()
move_left()
move_left()
for i in range(5):
    move()
turn_right()
move_left()
move_left()
move_left()

while front_is_clear():
    move()
    if object_here():
        done()

"""
Challenge 12: Center 1 
"""
while front_is_clear():
    move()

    # Find the object at the both sides
    if object_here():
        turn_left()
        turn_left()
        take()
        move()
        put()
        move()

        # Find the object at the middle side
        if object_here():
            turn_left()
            turn_left()
            take()
            move()
            done()

    # If the robot faces the wall, move back and put the object
    if wall_in_front():
        turn_left()
        turn_left()
        put()
        move()































