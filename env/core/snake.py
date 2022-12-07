import numpy as np

from settings.constants import DIRECTIONS, SNAKE_BLOCK

class Snake:
    def __init__(self, head_position, direction_index, length):
        """
        @param head_position: tuple
        @param direction_index: int
        @param length: int
        """
        self.snake_block = SNAKE_BLOCK
        self.current_direction_index = direction_index
        self.alive = True
        self.blocks = [head_position]
        current_position = np.array(head_position)

        for i in range(1, length):
            current_position = current_position - DIRECTIONS[self.current_direction_index]
            self.blocks.append(tuple(current_position))
            
    def step(self, action):

        """
        @param action: int
        @param return tuple, tuple
        """
        if (self.current_direction_index - action) % 2 != 0:
            self.current_direction_index = action

        tail = self.blocks.pop()
        old_head = self.blocks[0]
        new_head = (old_head[0] + DIRECTIONS[self.current_direction_index][0],
                    old_head[1] + DIRECTIONS[self.current_direction_index][1])

        self.blocks = [new_head] + self.blocks

        return new_head, tail