# File: FirstKarel.py
# -----------------------------
# The FirstKarel program defines a "main" 
# function with three commands. These commands cause  
# Karel to move forward one block, pick up a beeper
# and then move ahead to the next corner.
from stanfordkarel import * # alternative: https://pypi.org/project/stanfordkarel/

def main():
  move()
  pick_beeper()
  move()

if __name__ == "__main__":
    run_karel_program()