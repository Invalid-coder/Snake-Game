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
        # for custom init
        self.custom = custom
        self.start_position = start_position
        self.start_direction_index = start_direction_index
        self.food_position = food_position
        self.current_available_food_positions = None
        # rewards
        self.DEAD_REWARD = DEAD_REWARD
        self.MOVE_REWARD = MOVE_REWARD
        self.EAT_REWARD = EAT_REWARD
        self.FOOD = FOOD_BLOCK
        self.WALL = WALL
        self.DIRECTIONS = DIRECTIONS
        # Init a numpy ndarray with zeros of predefined size - that will be the initial World
        self.size = size
        self.world = np.zeros(size)
        # Fill in the indexes gaps to add walls along the World's boundaries
        self.world[0,:] = self.WALL
        self.world[-1,:] = self.WALL
        self.world[:, 0] = self.WALL
        self.world[:, -1] = self.WALL
        # Get available positions for placing food
        # Food should not to be spawned in the Walls
        self.available_food_positions = set(zip(*np.where(self.world == 0)))
        # Init snake
        self.snake = self.init_snake()
        # Set food
        self.init_food()

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