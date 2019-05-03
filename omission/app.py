
from omission.common.game_enums import GameMode, GameModeClass


class app():
    'app'

    def __init__(self):
        'init app'
        print("app.Init")

    def run(self):
        'run'
        print("app.Run")

def run():
    print("run function")
    x = GameModeClass()
    print(x.run())
