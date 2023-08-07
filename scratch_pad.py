from itertools import groupby
import random
import logging
from constants import NUMBER_OF_TRIALS, NUMBER_OF_FLIPS, STREAK_MINIMUM

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
# logging.disable(logging.CRITICAL)  # Note out to enable logging.


def flip_coin(number: int) -> list:
    results = [random.choice(["H", "T"]) for _ in range(number)]
    # Non-list-comprehension versoin for comparison
    # results = []
    # for _ in range(number):
    #     results.append(random.choice(["H", "T"]))
    # logging.debug(results)

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

    # logging.debug(streak)
    # logging.debug(streak_counter)

    return streak_counter


def count_streaks():
    streak_total = 0

    for _ in range(NUMBER_OF_TRIALS):
        results = flip_coin(NUMBER_OF_FLIPS)
        if count_duplicates(results) > 0:
            streak_total += 1

    logging.debug(streak_total)

    return streak_total


def main():
    total = count_streaks()
    percentage = total / 100
    print(f"Chance of streak of {STREAK_MINIMUM}: {percentage}%")


if __name__ == "__main__":
    main()
