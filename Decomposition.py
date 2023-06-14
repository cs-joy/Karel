from stanfordkarel import *

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

def fill_pothole():
    turn_right()
    move()
    put_beeper()
    turn_around()
    move()
    turn_right()


def main():
    move()
    fill_pothole()
    move()

if __name__ == "__main__":
    run_karel_program()