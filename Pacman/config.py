import pygame
import os

window = {
    'size': (550,300),
    'color': (52, 52, 47),
}

food = {
    'radius': 4,
    'width': 0,
    'color': (225, 225, 96),
}

maze = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,1],
    [1,2,1,2,1,1,2,2,2,2,2,2,1,1,2,1,2,1],
    [1,2,1,2,1,1,2,1,2,2,1,2,1,1,2,1,2,1],
    [1,2,1,2,2,2,2,1,2,2,1,2,1,1,2,1,2,1],
    [1,2,1,1,1,1,2,1,1,1,1,2,1,1,1,1,2,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]   
rowlen = len(maze)
collen = len(maze[0])

# Path
IMAGE_DIR = f"D:\Programming\Python\Teky\Pygame\Pacman\Images"
