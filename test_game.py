import unittest
import sys
from io import StringIO
from src.dino import Dino
from src.cactus import Cactus
from src.game import Game
from src.utils import check_collision, clear_screen, print_at_pos, print_art
from src.config import RESOLUTION


class TestDino(unittest.TestCase):

    def setUp(self):
        # Redirect output
        self.held_stdout = StringIO()
        sys.stdout = self.held_stdout

    def tearDown(self):
        # Restore standard output
        sys.stdout = sys.__stdout__

    def test_dino_initial_state(self):
        dino = Dino()
        self.assertEqual(dino.y, 0)
        self.assertFalse(dino.jump)
        self.assertFalse(dino.dead)
        self.assertEqual(dino.size_x, dino.np_state_1.shape[1])
        self.assertEqual(dino.size_y, dino.np_state_1.shape[0])

    def test_dino_jump_state(self):
        dino = Dino()
        dino.jump = True
        self.assertTrue((dino.get() == dino.np_state_jump).all())

    def test_dino_dead_state(self):
        dino = Dino()
        dino.dead = True
        self.assertTrue((dino.get() == dino.np_state_dead).all())

    def test_dino_animation(self):
        dino = Dino()
        initial_state = dino.get()
        next_state = dino.get()
        self.assertFalse((initial_state == next_state).all())


class TestCactus(unittest.TestCase):

    def setUp(self):
        # Redirect output
        self.held_stdout = StringIO()
        sys.stdout = self.held_stdout

    def tearDown(self):
        # Restore standard output
        sys.stdout = sys.__stdout__

    def test_cactus_initial_state(self):
        cactus = Cactus()
        self.assertEqual(cactus.x, RESOLUTION[1] - 1)
        self.assertGreater(cactus.size_x, 0)  # Ensure size is greater than 0
        self.assertGreater(cactus.size_y, 0)  # Ensure size is greater than 0


class TestGame(unittest.TestCase):

    def setUp(self):
        # Redirect output
        self.held_stdout = StringIO()
        sys.stdout = self.held_stdout

        self.game = Game()
        self.dino = Dino()

    def tearDown(self):
        # Restore standard output
        sys.stdout = sys.__stdout__

    def test_game_initial_state(self):
        self.assertEqual(self.game.ground_level, RESOLUTION[0])
        self.assertEqual(len(self.game.cactus_list), 0)

    def test_game_jump(self):
        self.game.jump()
        self.assertGreater(len(self.game.action_bus), 0)

    def test_game_update(self):
        initial_y = self.dino.y
        self.game.jump()
        self.game.update(self.dino)
        self.assertNotEqual(self.dino.y, initial_y)


class TestUtils(unittest.TestCase):

    def setUp(self):
        # Redirect output
        self.held_stdout = StringIO()
        sys.stdout = self.held_stdout

    def tearDown(self):
        # Restore standard output
        sys.stdout = sys.__stdout__

    def test_clear_screen(self):
        try:
            clear_screen()
        except Exception as e:
            self.fail(f"clear_screen() raised an exception {e}")

    def test_print_at_pos(self):
        try:
            print_at_pos(10, 10, "Test")
        except Exception as e:
            self.fail(f"print_at_pos() raised an exception {e}")

    def test_print_art(self):
        try:
            print_art("Test art")
        except Exception as e:
            self.fail(f"print_art() raised an exception {e}")

    def test_check_collision(self):
        game = Game()
        dino = Dino()
        cactus = Cactus()

        # Set sizes from dino and cactus states
        dino.size_x = dino.np_state_1.shape[1]
        dino.size_y = dino.np_state_1.shape[0]
        cactus.size_x = cactus.type.shape[1]
        cactus.size_y = cactus.type.shape[0]

        # Place cactus in the path of the dino
        cactus.x = dino.size_x // 2
        dino.y = 0

        # Ensure dino is on the ground
        self.assertEqual(dino.y, 0)

        # Ensure cactus is positioned to collide with dino
        self.assertTrue(check_collision(dino, cactus, game))

        # Adjust cactus position to miss the dino
        cactus.x = dino.size_x + cactus.size_x + 1  # Move cactus outside the dino's range

        # Ensure no collision
        self.assertFalse(check_collision(dino, cactus, game))


if __name__ == '__main__':
    unittest.main()
