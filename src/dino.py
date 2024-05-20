import numpy as np


class Dino:
    """
    Class representing the dinosaur character in the game.
    """

    # States of the dino represented as ASCII art
    state_1 = ("        ╔═══════╗\n"
               "        ║ ●   ..║\n"
               "╔╗     ╔╝    ╔══╝\n"
               "║╚╗   ╔╝   . ╠═╗ \n"
               "╚╗╚═══╝ .   ╔╝   \n"
               " ╚══╗    ╔══╝    \n"
               "    ╚╦══╦╝       \n"
               "     ║  ║        \n"
               "     ╚  ╚        ")
    np_state_1 = np.array([list(row) for row in state_1.split("\n") if row])

    state_2 = ("        ╔═══════╗\n"
               "        ║ ●   ..║\n"
               "╔╗     ╔╝    ╔══╝\n"
               "║╚╗   ╔╝   . ╠═╗ \n"
               "╚╗╚═══╝ .   ╔╝   \n"
               " ╚══╗    ╔══╝    \n"
               "    ╚╦══╦╝       \n"
               "     ║  ╚        \n"
               "     ╚           ")
    np_state_2 = np.array([list(row) for row in state_2.split("\n") if row])

    state_3 = ("        ╔═══════╗\n"
               "        ║ ●   ..║\n"
               "╔╗     ╔╝    ╔══╝\n"
               "║╚╗   ╔╝   . ╠═╗ \n"
               "╚╗╚═══╝ .   ╔╝   \n"
               " ╚══╗    ╔══╝    \n"
               "    ╚╦══╦╝       \n"
               "     ╚  ║        \n"
               "        ╚        ")
    np_state_3 = np.array([list(row) for row in state_3.split("\n") if row])

    state_jump = ("        ╔═══════╗\n"
                  "        ║ -   ..║\n"
                  "╔╗     ╔╝    ╔══╝\n"
                  "║╚╗   ╔╝   . ╠═╝ \n"
                  "╚╗╚═══╝ .   ╔╝   \n"
                  " ╚══╗    ╔══╝    \n"
                  "    ╚╦══╦╝       \n"
                  "    ═╝ ═╝        \n"
                  "                 ")
    np_state_jump = np.array([list(row) for row in state_jump.split("\n") if row])

    state_dead = ("        ╔═══════╗\n"
                  "        ║ X   ..║\n"
                  "       ╔╝    ╔══╝\n"
                  "      ╔╝   . ╠═╗ \n"
                  "  ╔═══╝ .   ╔╝   \n"
                  "  ║╔╗    ╔══╝    \n"
                  "  ║║╚╦══╦╝       \n"
                  "  ╚╝═╝  ╚═       \n"
                  "                 ")
    np_state_dead = np.array([list(row) for row in state_dead.split("\n") if row])

    def __init__(self):
        """
        Initializes the dino character with default values.
        """
        self.y = 0
        self.animation = [self.np_state_1, self.np_state_2, self.np_state_3]
        self.jump = False
        self.dead = False
        self.current_state = -1
        self.size_x = self.animation[0].shape[1]
        self.size_y = self.animation[0].shape[0]
        self.blink_timer = 0

    def get(self):
        """
        Returns the current state of the dino based on its condition (jumping, dead, or normal).
        """
        if self.jump:
            return self.np_state_jump
        elif self.dead:
            return self.np_state_dead
        else:
            if self.current_state < len(self.animation) - 1:
                self.current_state += 1
            else:
                self.current_state = 0

            result = self.animation[self.current_state].copy()
            # If timer is between 20 and 22, we blink the dino
            if self.blink_timer == 22:
                # Reset the timer
                self.blink_timer = 0
            elif self.blink_timer >= 20:
                # Replace "○" by "."
                result = np.where(result == "●", ".", result)
            self.blink_timer += 1
        return result

    def print(self, game):
        """
        Prints the dino on the game field at its current position.
        """
        dino_frame = self.get()
        for i in range(dino_frame.shape[0]):
            print(f"\033[{game.ground_level - self.size_y - self.y + i};0H", end='')
            print("".join(dino_frame[i]), end='')
