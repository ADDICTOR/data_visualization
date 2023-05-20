# 上帝也会掷骰子
from random import randint
import pygal

class Dice():
    """骰子类"""

    def __init__(self, num_sides=6) -> None:
        """6面骰"""
        self.num_sides = num_sides

    def roll(self):
        """掷骰子"""
        return randint(1, self.num_sides)


if __name__ == "__main__":
    dice_1 = Dice(6)
    dice_2 = Dice(10)

    results = []
    for n in range(1000000):
        result = dice_1.roll() + dice_2.roll()
        results.append(result)

    frequencies = []
    max_result = dice_1.num_sides + dice_2.num_sides
    for value in range(2, max_result + 1):
        frequency = results.count(value)
        frequencies.append(frequency)

    # print(frequencies)
    hist = pygal.Bar()

    hist.title = "Results of rolling two D6 1000 times"
    hist.x_labels = list(range(2,17))
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"

    hist.add("D6 + D10", frequencies)
    hist.render_to_file('./images/two_dice_visual.svg')