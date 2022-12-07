import numpy as np
import random

from settings.constants import DIRECTIONS, SNAKE_SIZE, DEAD_REWARD, MOVE_REWARD, EAT_REWARD, FOOD_BLOCK, WALL
from env.core.snake import Snake


class World(object):
    def __init__(self, size, custom, start_position, start_direction_index, food_position):
        """
        @param size: tuple
        @param custom: bool
        @param start_position: tuple
        @param start_direction_index: int
        @param food_position: tuple
        """
        pass

    def init_snake(self):
        """
        Initialize a snake
        """
        pass

    def init_food(self):
        """
        Initialize a piece of food
        """
        pass

    def get_observation(self):
        """
        Get observation of current world state
        """
        pass

    def move_snake(self, action):
        """
        Action executing
        """
        pass