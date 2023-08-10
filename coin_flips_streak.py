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
    """Run calculations on results to determine likelihood of streak and print results."""
    total = count_streaks()
    percentage = total / (NUMBER_OF_TRIALS / NUMBER_OF_FLIPS)
    print(
        f"Chance of {STREAK_MINIMUM} consecutive heads or tails per {NUMBER_OF_FLIPS} flips in {NUMBER_OF_TRIALS:,} trials: {percentage}%"
    )


def flip_coin(number: int) -> list[str]:
    """Create and return a list of n H's and T's."""
    results = [choice(["H", "T"]) for _ in range(number)]
    logging.debug(results)
    return results


def find_streak(results: list[str]) -> int:
    """Use groupby to convert consecutive H and T values to integers,
    cast those values to a list, reverse sort the new list and increment a counter
    if the first item is greater than the minimum streak value. Return counter."""
    streak_counter = 0
    streak = [len(list(group)) for _, group in groupby(results)]
    logging.debug(streak)
    streak.sort(reverse=True)

    if streak[0] >= STREAK_MINIMUM:
        streak_counter += 1

    logging.debug(streak_counter)
    return streak_counter


def count_streaks() -> int:
    """Get result from n number of trials, increment streak total counter and return it."""
    streak_total = 0

    for _ in range(NUMBER_OF_TRIALS):
        results = flip_coin(NUMBER_OF_FLIPS)
        if find_streak(results) > 0:
            streak_total += 1

    logging.debug(streak_total)
    return streak_total


if __name__ == "__main__":
    main()
