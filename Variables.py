import pygame
import ctypes
import os
import queue
import sys
import random

import Main
import Functions
import Screens


pygame.init()


# getting the size of user's screen
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)
scaled_screen_height = int(screensize[1] * .9 * .75)

# setting the size of snake and fields.
scale_factor = 2                                    # can be changed to full number. the bigger num - the smaller snake
body_size = int(scaled_screen_height / 12 / scale_factor)
block_size = body_size * scale_factor               #: base variable for setting all the sizes - important one!

# creating the game window
game_width, game_height = 12 * block_size, 16 * block_size  #: size of the game - adapted to background image
icon = pygame.image.load('media/heads/head_down.jpg')
pygame.display.set_caption('Snake')
pygame.display.set_icon(icon)
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (int((screensize[0] - 12 * block_size) / 2), 32)

# all images in the game
screen = pygame.display.set_mode((game_width, game_height))
surface = pygame.image.load("media/screens/background_800.png").convert()
surface = pygame.transform.scale(surface, (block_size*12, block_size*16))
head = Functions.load_img('media/heads/head_down.png', 1.5)
head_eat = Functions.load_img('media/heads/head_eat_down.png', 1.5)
head_dead = Functions.load_img('media/heads/head_down_dead.png', 1.5)
food = Functions.load_img('media/food/mouse.png', 1.2)
lost = pygame.image.load("media/screens/lost.png").convert()
lost = pygame.transform.scale(lost, (block_size*6, block_size*6))
welcome = pygame.image.load("media/screens/welcome.png").convert()
welcome = pygame.transform.scale(welcome, (block_size*6, block_size*6))

# movement constants
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
PAUSE = (0, 0)

# colors
dark_gray = (30, 30, 30)
black = (0, 0, 0)
orange = (219, 106, 15)

# sad variables
is_eaten = False
is_dead = False

# eaten mouses
points = 0
high_score = list()
score_multi = 1

# fonts
large_text = pygame.font.SysFont('Calibri', int(block_size*2), True, False)
normal_text = pygame.font.SysFont('Calibri', int(block_size*0.8), True, False)
small_text = pygame.font.SysFont('Calibri', int(block_size*0.4), True, False)

# time
clock = pygame.time.Clock()
fps = 10 # frames per second

screen.blit(surface, [0, 0])

# queue with movements
q = queue.Queue()
x_tmp = 1
y_tmp = 0

starting = True
resume_dir = RIGHT
