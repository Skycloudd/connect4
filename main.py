#!/usr/bin/env python3

from game import Game
import colorama


def main():
    colorama.init()

    game = Game()
    game.play()


if __name__ == "__main__":
    main()
