"""
This module was autogenerated by gale.
"""
import settings
from src.Fokitoway import Fokitoway

if __name__ == '__main__':
    game = Fokitoway(
        "Fokitoway",
        settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT,
        settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT
    )
    game.exec()