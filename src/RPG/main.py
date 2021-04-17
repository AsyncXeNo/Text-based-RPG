import sys
import os

from game import Game

# important
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)

# game
game = Game()

if __name__ == "__main__":
	game.run()	
