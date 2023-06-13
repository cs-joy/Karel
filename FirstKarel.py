# File: FirstKarel.py
# -----------------------------
# The FirstKarel program defines a "main" 
# function with three commands. These commands cause  
# Karel to move forward one block, pick up a beeper
# and then move ahead to the next corner.
from karel.stanfordkarel import *

def main():
  move()
  pick_beeper()
  move()
