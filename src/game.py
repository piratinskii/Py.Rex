import numpy as np
import random
from src.config import RESOLUTION


class Game:
    """
    Class representing the game state and logic.
    """

    # Art for the moon
    moon = ("▓▓██    \n"
            "  ▓▓██  \n"
            "   ▒▓▓██\n"
            "   ▒▓▓██\n"
            "  ▓▓██  \n"
            "▓▓██    ")
    np_moon = np.array([list(row) for row in moon.split("\n") if row])

    def __init__(self):
        self.action_bus = []
        self.cactus_list = []
        self.cactus_speed = 2
        self.ground_level = RESOLUTION[0]

        # Initialize screen with stars and the moon
        self.initialize_sky()

    def initialize_sky(self):
        """
        Initializes the sky with stars and the moon.
        """
        print(f"\033[{RESOLUTION[0]};0H", end='')
        print("▀" * RESOLUTION[1], end="")

        for _ in range(100):
            x = random.randint(0, RESOLUTION[1] - 1)
            y = random.randint(0, RESOLUTION[0] - 6)
            if x < 20 and y > RESOLUTION[0] - 21:
                continue
            color = random.choice([30, 37, 90, 97])
            print(f"\033[{y};{x}H", end='')
            print(f"\033[{color}m" + random.choice([".", "●", "*"]) + "\033[0m", end='')

        for i in range(self.np_moon.shape[0]):
            print(f"\033[{5 + i};{RESOLUTION[1] - self.np_moon.shape[1] - 5}H", end='')
            print("".join(self.np_moon[i]), end='')

    def print_field(self, dino, score):
        """
        Prints the game field including the score, dino, and cacti.
        """
        print("\033[?25l", end='')
        print(f"\033[0;0H", end='')
        formatted_score = f"Score: {int(score):05}"
        formatted_line = f"{formatted_score:>{RESOLUTION[1]}}"
        print(formatted_line)

        for cactus in self.cactus_list:
            cactus_frame = cactus.type
            for i in range(cactus_frame.shape[0]):
                print(f"\033[{self.ground_level - cactus.size_y + i};{cactus.x - cactus.size_x}H", end='')
                print("\033[32m" + "".join(cactus_frame[i]) + "\033[0m")

        dino.print(self)

    def jump(self):
        """
        Initiates the dino's jump by adding jump actions to the action bus.
        """
        self.action_bus.extend([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 0])

    def update(self, dino):
        """
        Updates the game state, including the dino's position and the cacti.
        """
        if self.action_bus:
            action = self.action_bus.pop(0)
            if action == 0:
                dino.jump = False

            for i in range(dino.size_y):
                print(f"\033[{self.ground_level - dino.size_y - dino.y + i};0H", end='')
                print(" " * dino.size_x, end='')

            dino.y = action
            dino.print(self)

        for cactus in self.cactus_list:
            for i in range(cactus.size_y):
                print(f"\033[{self.ground_level - cactus.size_y + i};{cactus.x - self.cactus_speed}H", end='')
                print(" " * self.cactus_speed, end='')

            cactus.x -= self.cactus_speed
            if cactus.x - cactus.size_x <= 0:
                for i in range(cactus.size_y):
                    print(f"\033[{self.ground_level - cactus.size_y + i};0H", end='')
                    print(" " * cactus.size_x, end='')
                self.cactus_list.remove(cactus)
