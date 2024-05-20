import os
from src.config import RESOLUTION

def clear_screen():
    """
    Clears the console screen.
    """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def print_at_pos(x, y, text):
    """
    Prints text at specific terminal coordinates.

    Args:
    - x: horizontal coordinate (column)
    - y: vertical coordinate (row)
    - text: text to print
    """
    print(f"\033[{y};{x}H", end='')
    print(text)

def print_art(art, caption="Press Enter to start or Esc to exit", score=0):
    """
    Prints ASCII art centered on the screen with an optional caption and score.

    Args:
    - art: ASCII art to print
    - caption: caption text to print
    - score: score to display
    """
    art_lines = art.split("\n")
    for i, line in enumerate(art_lines):
        # Calculate coordinates to center each line
        x = RESOLUTION[1] // 2 - len(line) // 2
        y = RESOLUTION[0] // 2 - len(art_lines) // 2 + i
        print_at_pos(x, y, line)

    if score is not None:
        score_text = f"Your score: {int(score):05}"
        # Calculate coordinates to display the score
        x = RESOLUTION[1] // 2 - len(score_text) // 2
        y = RESOLUTION[0] // 2 - len(art_lines) // 2 + len(art_lines) + 1
        print_at_pos(x, y, score_text)

    # Calculate coordinates to display the caption
    caption_x = RESOLUTION[1] // 2 - len(caption) // 2
    caption_y = RESOLUTION[0] // 2 - len(art_lines) // 2 + len(art_lines) + 3
    print_at_pos(caption_x, caption_y, caption)

def check_collision(dino, cactus, game):
    """
    Checks for a collision between the dino and a cactus.

    Args:
    - dino: the Dino object
    - cactus: the Cactus object
    - game: the Game object

    Returns:
    - True if a collision is detected, False otherwise
    """
    # Determine the starting coordinates of the dino and cactus
    dino_x_start = 0  # Assume the dino always starts at 0 on the X axis
    cactus_x_start = cactus.x - cactus.size_x

    dino_y_start = game.ground_level - dino.size_y - dino.y
    cactus_y_start = game.ground_level - cactus.size_y

    # Iterate over each character in the dino
    for dy, dino_row in enumerate(dino.get()):
        for dx, dino_char in enumerate(dino_row):
            if dino_char != " ":
                # If the character is not a space, get its absolute coordinates
                dino_abs_x = dino_x_start + dx
                dino_abs_y = dino_y_start + dy

                # Check each character in the cactus
                for cy, cactus_row in enumerate(cactus.type):
                    for cx, cactus_char in enumerate(cactus_row):
                        if cactus_char != " ":
                            # If the cactus character is not a space, get its absolute coordinates
                            cactus_abs_x = cactus_x_start + cx
                            cactus_abs_y = cactus_y_start + cy

                            # Check for a collision
                            if dino_abs_x == cactus_abs_x and dino_abs_y == cactus_abs_y:
                                return True  # Collision detected
    return False  # No collision detected
