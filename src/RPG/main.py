import sys
import os

from application import Application

# important
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)


if __name__ == "__main__":
	Application()	