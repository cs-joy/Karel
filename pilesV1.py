from stanfordkarel import *

def rotate_and_collect():
    for i in range(3):
        move()
        pick_beeper()
        move()

def turn_left_move_turn_left():
    turn_left()
    move()
    turn_left()
    
def set_right_direction():
    turn_left_move_turn_left()
    moved()
    turn_left_move_turn_left()
    
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

if __name__ == '__main__':
    run_karel_program()