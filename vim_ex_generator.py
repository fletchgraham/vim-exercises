"""Make a text file with random vim practice"""

import os
import random

# make a maze
width = 72
height = 36

# make a grid of 72 x 72 cells
maze = [[' ' for x in range(width)] for y in range(height)]

# make a pointer (u, v)
runner_u = 0
runner_v = 0

direction = 0

# while u is less than 72 or v is less than 72
while (runner_u < width-1) and (runner_v < height-1):

    # randomly choose to change direction
    # directions: right=0, down=1, etc...
    direction = random.randint(0, 4)

    # if right, increment v
    if direction == 0:
        runner_v += 1
    elif direction == 1:
        runner_u -= 1
    elif direction == 2:
        runner_v -= 1
    elif direction == 3:
        runner_u += 1

    if runner_u < 0:
        runner_u = 0
    if runner_v < 0:
        runner_v = 0

    maze[runner_u][runner_v] = '#'

# join the row lists by '', join the wholey thing by newline
maze_string = ''

for row in maze:
    r = ''.join(row) + '\n'
    maze_string += r

# print the string
print(maze_string)