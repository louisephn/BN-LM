import pygame
from random import randint
import sys

pygame.init()

clock = pygame.time.Clock()

blue = (70,130,180)
white = (255, 255, 255)


numbers = [i for i in range(1,11)]
letters = ['A','B','C','D','E','F','G','H','I','J']
size = len(letters)
square_size = 50
height = size * square_size
width = size * square_size
grid_state = [[None for i in range(size)]for k in range(size)]
amount_boat = 4


def display_grid(grid_state):
    screen = pygame.display.set_mode((width, height))
    screen.fill(blue)
    pygame.display.set_caption("Bataille Navale")   
    for i in range (size + 1) :
        pygame.draw.line(screen, white, (i * square_size, 0), (i * square_size, height))
        pygame.draw.line(screen, white, (0, i * square_size), (width, i * square_size))
    pygame.display.update()
    pygame.time.wait(10000)


def place_boat(grid_state, amount_boat):
    for i in range (amount_boat):
        x_boat=randint(0,size)
        y_boat=randint(0,size)
        grid_state[x_boat,y_boat] = 'O'


def battleship_game():
    display_grid(grid_state)
    place_boat(grid_state, amount_boat)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                row = position[1] // square_size
                column = position[0] // square_size
                if grid_state[row][column] == 'O':
                    print("Congratulations ! You touched a boat !")
                    grid_state[row][column] = 'X'
                    if all('O' not in row for row in board):
                        print("Congratulations ! You've sank all boats !")
                        pygame.quit()
                        sys.exit()
                else:
                    print("Waht a pity, you've missed.")
        display_grid(grid_state)
        pygame.display.flip()




