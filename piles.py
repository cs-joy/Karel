from stanfordkarel import *

# File: piles.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel
# pick up all the beepers in the world.

def rotate_and_collect():
    move()
    pick_beeper()
    
    move()
    move()
    
    pick_beeper()
    
    move()
    move()
    
    pick_beeper()
    move()
def set_right_direction():
    turn_left()
    
    move()
    
    turn_left()
    
    
    moved()
    
    turn_left()
    
    move()
    
    turn_left()
    
def moved():
    for i in range(6):
        move()


def movement():
    for i in range(9):
        set_right_direction()
        rotate_and_collect()
def main():
    rotate_and_collect()
    movement()

   
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    run_karel_program()