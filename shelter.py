from stanfordkarel import *

# File: shelter.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel 
# move to the beeper, pick it up, and
# return home.

def turn_right():
    turn = 0
    while turn < 3:
        turn_left()
        turn += 1

def turn_around():
    turn = 0
    while turn < 2:
        turn_left()
        turn += 1

def go_forward():
    move()
    move()
    move()

def main():
    beepers_present()
    turn_right()
    move()
    turn_left()
    go_forward()
    pick_beeper()
    turn_around()
    go_forward()
    turn_right()
    move()
    turn_right()
    
    
if __name__ == '__main__':
    run_karel_program()