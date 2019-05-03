import unittest

from omission import app as frog
from omission.common.game_enums import GameMode, GameModeClass

# https://stackoverflow.com/questions/18668947/how-do-i-set-sys-argv-so-i-can-unit-test-it

class TestTest(unittest.TestCase):
    def setUp(self):
        self.assertTrue(True)
 
    def test_app(self):
        frog.run()
        self.assertTrue(True)

    def test_GameMode(self):
        #Function Inside of the game_enums.py file  called GameMode
        self.assertTrue(GameMode() == "GameMode function")


    def test_GameModeClass(self):
        #Class Insite of the game_enums.py file  called GameModeClass
        x = GameModeClass()
        self.assertTrue(x.run() == "GameModeClass.Run")


if __name__ == '__main__':
    unittest.main()