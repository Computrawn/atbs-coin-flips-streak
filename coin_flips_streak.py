# Coin flip streak practice problem

"""
Modified original idea (a set 10,000 trails) by allowing user to input number of trials.
I could probably refine this by a lot, but it's working for now.
Revisit when inspiation strikes.
"""

import random


def streakCounter():
    numberOfStreaks = 0
    print("Please enter the integer value of trials you would like to conduct.")
    print("For more precise results, enter intergers of 10000 or greater.")
    print("(Note: Precision comes at the cost of time.)")
    numberOfTrials = input()
    try:
        for experimentNumber in range(int(numberOfTrials)):
            results = []
            streak = []
            heads = 0
            tails = 0
            for flips in range(100):
                if random.randint(0, 1) == 0:
                    results.append("H")
                else:
                    results.append("T")
            while results[heads] == "H":
                streak.append("H")
                heads += 1
                if len(streak) >= 6:
                    numberOfStreaks += 1
            while results[tails] == "T":
                streak.append("T")
                tails += 1
                if len(streak) >= 6:
                    numberOfStreaks += 1
        print(
            "Chance of streak: %s%%" % (numberOfStreaks / (int(numberOfTrials) / 100))
        )
    except:
        print("You must enter an integer.")


streakCounter()
