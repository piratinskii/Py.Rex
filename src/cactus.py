import random
import numpy as np
from src.config import RESOLUTION


class Cactus:
    """
    Class representing a cactus obstacle in the game.
    """
    # Cactus types represented as ASCII art
    type_1 = ("╔╗  \n"
              "╣║╔╗\n"
              "║╚╝╠\n"
              "╣╔═╝\n"
              "║║  ")
    np_type_1 = np.array([list(row) for row in type_1.split("\n") if row])

    type_2 = ("  ╔╗\n"
              "╔╗║╠\n"
              "╣╚╝║\n"
              "╚═╗╠\n"
              "  ║║")
    np_type_2 = np.array([list(row) for row in type_2.split("\n") if row])

    type_3 = ("  ╔╗  \n"
              "╔╗╣║╔╗\n"
              "╣╚╝╚╝╠\n"
              "╚═╗╔═╝\n"
              "  ╣║  ")
    np_type_3 = np.array([list(row) for row in type_3.split("\n") if row])

    type_4 = ("╔╗\n"
              "╣║\n"
              "║╠\n"
              "║║")
    np_type_4 = np.array([list(row) for row in type_4.split("\n") if row])

    # List of all cactus types
    types = [np_type_1, np_type_2, np_type_3, np_type_4]

    def __init__(self):
        """
        Initializes a cactus object with random type and initial position.
        """
        self.type = random.choice(self.types)
        self.x = RESOLUTION[1] - 1
        self.size_x = self.type.shape[1]
        self.size_y = self.type.shape[0]
