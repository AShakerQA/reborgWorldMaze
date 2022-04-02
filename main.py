def turn_right():
    turn_left()
    turn_left()
    turn_left()

#exit situations where robot gets stuck
#makes sure robot is next to wall
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
