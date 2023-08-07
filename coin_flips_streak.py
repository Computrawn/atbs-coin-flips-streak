#!/usr/bin/env python3
# coin_flips_streak.py — An exercise in understanding lists.
# For more information, see README.md

from itertools import groupby
from random import choice
import logging
from constants import NUMBER_OF_TRIALS, NUMBER_OF_FLIPS, STREAK_MINIMUM

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
logging.disable(logging.CRITICAL)  # Note out to enable logging.


def main() -> None:
    total = count_streaks()
    percentage = total / 100
    print(
        f"Chance of {STREAK_MINIMUM} consecutive heads or tails per {NUMBER_OF_FLIPS} flips per {NUMBER_OF_TRIALS} trials: {percentage}%"
    )


def flip_coin(number: int) -> list:
    results = [choice(["H", "T"]) for _ in range(number)]
    # Non-list-comprehension version for comparison
    # results = []
    # for _ in range(number):
    #     results.append(random.choice(["H", "T"]))
    logging.debug(results)

    return results


def count_duplicates(results: list) -> int:
    streak_counter = 0
    streak = [len(list(group)) for _, group in groupby(results)]
    # Non-list-comprehension version for comparison
    # streak = []
    # for _, group in groupby(results):
    #     streak.append(len(list(group)))

    for i in streak:
        if i >= STREAK_MINIMUM:
            streak_counter += 1

    logging.debug(streak)
    logging.debug(streak_counter)

    return streak_counter


def count_streaks() -> int:
    streak_total = 0

    for _ in range(NUMBER_OF_TRIALS):
        results = flip_coin(NUMBER_OF_FLIPS)
        if count_duplicates(results) > 0:
            streak_total += 1

    logging.debug(streak_total)

    return streak_total


if __name__ == "__main__":
    main()
