import pygame
from pygame.locals import *
import numpy as np
from random import randint as ri
pygame.init()

GAME_RES = WIDTH, HEIGHT = 800, 800
FPS = 60
GAME_TITLE = 'PYGAME OF LIFE'

window = pygame.display.set_mode(GAME_RES, HWACCEL|HWSURFACE|DOUBLEBUF)
pygame.display.set_caption(GAME_TITLE)
clock = pygame.time.Clock()

# Game Values

background_color = (0, 0, 0) # RGB value

num_cell_row = 40
num_cell_col = 40
dim_cell = WIDTH // num_cell_row
FPS = 24
interval = 1 / FPS

matrix = None

def create_matrix():
    global matrix
    matrix = np.random.randint(2, size=(num_cell_row, num_cell_col))

def parse_matrix():
    copied_matrix = np.copy(matrix)

    for x in range(num_cell_row):
        for y in range(num_cell_col):
            num_of_near_cells = 0

            try:
                num_of_near_cells += copied_matrix[x-1][y-1]
            except: pass

            try:
                num_of_near_cells += copied_matrix[x][y-1]
            except: pass

            try:
                num_of_near_cells += copied_matrix[x+1][y-1]
            except: pass

            try:
                num_of_near_cells += copied_matrix[x-1][y]
            except: pass

            try:
                num_of_near_cells += copied_matrix[x+1][y]
            except: pass

            try:
                num_of_near_cells += copied_matrix[x-1][y+1]
            except: pass

            try:
                num_of_near_cells += copied_matrix[x][y+1]
            except: pass

            try:
                num_of_near_cells += copied_matrix[x+1][y+1]
            except: pass

            if num_of_near_cells < 2 or num_of_near_cells > 3:
                matrix[x][y] = 0
            elif num_of_near_cells == 3 and copied_matrix[x][y] == 0:
                matrix[x][y] = 1



def draw_matrix():
    parse_matrix()

    for x in range(num_cell_row):
        for y in range(num_cell_col):
            if matrix[x][y] == 1:
                pygame.draw.rect(window, (0, 255, 0), (x * dim_cell, y * dim_cell, dim_cell, dim_cell))
                
# End of Game Values

create_matrix()

# Game loop
game_ended = False
while not game_ended:

    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            game_ended  = True
            break
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game_ended  = True
                break

    # Game logic

    # Display update
    pygame.Surface.fill(window, background_color)
    draw_matrix()


    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
exit(0)
