"""随机漫步"""
from random import choice

import matplotlib.pyplot as plt

class RandomWalk():
    """随机漫步类
    """

    def __init__(self, num_points=5000) -> None:

        self.num_points = num_points

        # 初始位置
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """随机漫步方法：生成两组随机数列
        """

        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_distance * x_direction

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_distance * y_direction

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

if __name__ == "__main__":
    while True:
        rw = RandomWalk(5000)
        rw.fill_walk()

        plt.figure(dpi=128, figsize=(10, 6))

        point_numbers = list(range(rw.num_points))
        plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
            cmap=plt.cm.Blues, edgecolors='none', s=1)

        # 突出起点与终点
        plt.scatter(0, 0, c='green', edgecolors='none', s=100)
        plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',s=100)
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)

        plt.show()

        keep_running = input("Make another walk?(y/n): ")
        if keep_running == "n":
            break
