from random import random
import time
import keyboard
from src.utils import clear_screen, check_collision, print_art
from src.game import Game
from src.dino import Dino
from src.cactus import Cactus
from src.config import RESOLUTION, DIFFICULTY, MIN_DISTANCE_BETWEEN_CACTI, CACTUS_SPAWN_CHANCE
from src.arts import title_art, lose_art


def main():
    """
    Main function to start and run the game.
    """
    score = 0
    distance_to_next_cactus = 0
    clear_screen()
    game = Game()
    dino = Dino()

    while True:
        game.update(dino)

        # Check for collision with cactus
        for cactus in game.cactus_list:
            if (cactus.x - cactus.size_x < dino.size_x and
                    game.ground_level - dino.y > game.ground_level - cactus.size_y):
                if check_collision(dino, cactus, game):
                    lose_screen(score)
                    return

        # Randomly add a cactus
        if random() < CACTUS_SPAWN_CHANCE and distance_to_next_cactus <= 0:
            game.cactus_list.append(Cactus())
            distance_to_next_cactus = max(RESOLUTION[1] / game.cactus_speed - score * DIFFICULTY,
                                          dino.size_x * MIN_DISTANCE_BETWEEN_CACTI)

        if keyboard.is_pressed('space') and not dino.jump:
            dino.jump = True
            game.jump()

        if keyboard.is_pressed('esc'):
            return

        game.print_field(dino, score)
        time.sleep(0.1)
        score += 0.1
        distance_to_next_cactus -= 1


def lose_screen(score):
    """
    Display the lose screen and handle restart or exit.
    """
    print()
    clear_screen()
    game = Game()
    dino = Dino()
    dino.dead = True
    dino.print(game)
    print_art(lose_art, "Press Enter to restart or Esc to exit", score)

    while True:
        if keyboard.is_pressed('enter'):
            main()
            return
        if keyboard.is_pressed('esc'):
            return
        time.sleep(0.1)


def demo():
    """
    Display the demo screen and start the game on key press.
    """
    score = 0
    clear_screen()
    game = Game()
    dino = Dino()
    print_art(title_art)

    while True:
        game.update(dino)
        game.print_field(dino, score)

        if keyboard.is_pressed('enter'):
            main()
            return
        if keyboard.is_pressed('esc'):
            return
        time.sleep(0.1)


if __name__ == "__main__":
    demo()
    clear_screen()
