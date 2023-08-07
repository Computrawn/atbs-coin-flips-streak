import random
import logging
from constants import NUMBER_OF_TRIALS, FLIPS_PER_TRIAL, MIN_STREAK

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
# logging.disable(logging.CRITICAL)  # Note out to enable logging.

results, streak, heads, tails = [], [], 0, 0

for _ in range(FLIPS_PER_TRIAL):
    if random.randint(0, 1):
        results.append("H")
    else:
        results.append("T")

test_string = "".join(results)

if "H" * 6 in test_string:
    print("heads streak")
if "T" * 6 in test_string:
    print("tails streak")

logging.debug(test_string)
