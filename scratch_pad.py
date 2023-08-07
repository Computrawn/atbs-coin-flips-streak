from itertools import groupby
import random
import logging
from constants import NUMBER_OF_TRIALS, FLIPS_PER_TRIAL, MIN_STREAK

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
# logging.disable(logging.CRITICAL)  # Note out to enable logging.


def coin_flip(number: int) -> list:
    results = []
    for _ in range(number):
        results.append(random.choice(["H", "T"]))
    logging.debug(results)
    return results


def coin_flip_comp(number: int) -> list:
    results = [random.choice(["H", "T"]) for _ in range(number)]
    logging.debug(results)
    return results


def count_duplicates(results: list) -> int:
    streak = []
    streak_counter = 0
    for _, group in groupby(results):
        streak.append(len(list(group)))

    for i in streak:
        if i >= MIN_STREAK:
            streak_counter += 1

    logging.debug(streak)
    logging.debug(streak_counter)
    return streak_counter


def count_duplicates_comp(results: list) -> int:
    streak_counter = 0
    streak = [len(list(group)) for _, group in groupby(results)]

    for i in streak:
        if i >= MIN_STREAK:
            streak_counter += 1

    logging.debug(streak)
    logging.debug(streak_counter)
    return streak_counter


results = coin_flip_comp(FLIPS_PER_TRIAL)

count_duplicates_comp(results)
