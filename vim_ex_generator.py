"""Make a text file with random vim practice"""

import os
import random
from turtle import right

# make a maze
width = 72
height = 36

# make a grid of 72 x 72 cells
maze = [[' ' for x in range(width)] for y in range(height)]

# make a pointer (u, v)
runner_u = 0
runner_v = 0

direction = 'right' 

# while u is less than 72 or v is less than 72
while (runner_v < width-1) and (runner_u < height-1):

    # randomly choose to change direction
    # directions: right=0, down=1, etc...
    if random.random() < .15:
        if direction in ['up', 'down']:
            direction = random.choice(['right','left'])
        elif random.random() < .5:
            direction = random.choice(['up','down'])

    # if right, increment v
    if direction == 'right':
        runner_v += 1
    elif direction == 'down':
        runner_u += 1
    elif direction == 'left':
        runner_v -= 1
    elif direction == 'up':
        runner_u -= 1

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

with open('practice.txt', 'w') as outfile:
    outfile.write(maze_string)