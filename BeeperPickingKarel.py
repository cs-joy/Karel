from stanfordkarel import *

def turn_right():
    turn = 0
    while turn < 3:
        turn_left()
        turn = turn + 1

def turn_around():
    turn = 0
    while turn < 2:
        turn_left()
        turn += 1

def main():
    move()
    turn_left()
    move()
    turn_right()
    move()
    put_beeper()
    turn_left()
    move()
    move()
    turn_around()

if __name__ == "__main__":
    run_karel_program()