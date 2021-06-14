import copy
import random
from collections import Counter

class Hat:
    def __init__(self, **kwargs) -> None:
        # Key words repeated by the value they reference
        self.contents = list(Counter(kwargs).elements())

    def draw(self, balls: int) -> list:
        """
        Takes some number of balls to draw from the ones that are
        stored in the current class. If the number is too big, it
        returns all balls.
        """

        if balls >= len(self.contents):
            return self.contents

        # Get random values and remove them from the list
        drawn = random.sample(self.contents, k=balls)
        for ball in drawn:
            self.contents.remove(ball)

        return drawn

def experiment(
    hat: object, expected_balls: dict,
    num_balls_drawn: int, num_experiments: int
) -> float:
    """
    Returns the probability of how many times the balls indicated
    were drawn from the hat (number of successes / number of
    times run). Creates a deep copy to avoid reading the same
    data (list of balls).
    """

    success = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)

        drawn_balls = hat_copy.draw(num_balls_drawn)
        keep = True  # False if there are not enough values
        for key, value in expected_balls.items():
            if drawn_balls.count(key) < value:
                keep = False

        if keep:
            success += 1

    return success / num_experiments
