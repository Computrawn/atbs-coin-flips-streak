#!/usr/bin/env python3
# coin_flips_streak.py — An exercise in understanding lists.
# For more information, see README.md

import random
import logging
from constants import NUMBER_OF_TRIALS, FLIPS_PER_TRIAL, MIN_STREAK

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
logging.disable(logging.CRITICAL)  # Note out to enable logging.


def streak_counter(number: int) -> str:
    number_of_streaks = 0

    for _ in range(number):
        results, streak, heads, tails = [], [], 0, 0

        for _ in range(FLIPS_PER_TRIAL):
            if random.randint(0, 1) == 0:
                results.append("H")
            else:
                results.append("T")

        while results[heads] == "H":
            streak.append("H")
            heads += 1

            if len(streak) >= MIN_STREAK:
                number_of_streaks += 1

        while results[tails] == "T":
            streak.append("T")
            tails += 1

            if len(streak) >= MIN_STREAK:
                number_of_streaks += 1

    return f"Chance of streak: {number_of_streaks / 100}%"


def main() -> None:
    print(streak_counter(NUMBER_OF_TRIALS))


if __name__ == "__main__":
    main()
