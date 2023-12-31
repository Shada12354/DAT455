"""
QA-session Advanced 2023-06-27
@author Shada Al-Wakkal, GitHub: Shada12354
Examples are from wikiHow.
"""

import time
import random


# COUNTDOWN
def countdown(t):
    while t > 0:
        print(t)
        t -= 1  # t = t -1
        time.sleep(1)
    print("Time's up!")


print("How many seconds to count down?>" + " ")
seconds = input()
while not seconds.isdigit():
    print("That wasn't an integer, please enter an integer>" + " ")
    seconds = input()
seconds = int(seconds)
countdown(seconds)

# HOW LONG HAVE I BEEN ALIVE
print("Let's see how long you have in days, minutes & seconds")
name = input("Please enter name>" + " ")
print("Now enter your age>")
age = int(input())

days = age * 365
minutes = age * 525948
seconds = age * 31556926

print(name, "has been alive for", days, "days", minutes, "minutes &", seconds, "seconds! Wow!")

# COINFLIP
print("Welcome to my coin flipping game")
choice = input("Enter your side, heads or tails? > ")

num = random.randint(1, 2)

if num == 1:
    result = "heads"

elif num == 2:
    result = "tails"

if choice == result:
    print("Good job, the coin flipped" + " " + result)

else:
    print("You lose, coin flipped" + " " + result)

print("Thanks for playing")
