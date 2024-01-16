import pygame
from random import randint
import sys

pygame.init()

clock = pygame.time.Clock()

blue = (70,130,180)
white = (255, 255, 255)
red = (255,0,0)
black = (0,0,0)



letters = ['A','B','C','D','E','F','G','H','I','J']
size = len(letters)
numbers = [i for i in range(size+1)]
square_size = 50
height = (size+1) * square_size
width = (size+1) * square_size
grid_state = [[None for i in range(size+1)]for k in range(size+1)]
amount_boat = 4
score = 0

font = pygame.font.Font(None, 36)

def display_grid(grid_state, username, last_move):
    screen = pygame.display.set_mode((width, height+2*square_size))
    screen.fill(blue)
    pygame.display.set_caption("Bataille Navale")

    
    for k in range(size+1):
        pygame.draw.rect(screen, white, (0, k*square_size, square_size, square_size))
        pygame.draw.rect(screen, white, (k * square_size, 0, square_size, square_size)) 
        pygame.draw.rect(screen, white, (k*square_size, height, square_size, square_size))
        pygame.draw.rect(screen, white, (k*square_size, (height+square_size),square_size, square_size)) 

        pygame.draw.line(screen, black, (k*square_size, 0), (k*square_size, square_size))
        pygame.draw.line(screen, black, (0, k*square_size), (square_size, k*square_size))
    
    pygame.draw.line(screen, black, (square_size, 0), (square_size, height))
    pygame.draw.line(screen, black, (0, square_size), (width, square_size))
    
    
    for i, row in enumerate(letters):
        for j, cell in enumerate(row):
            letter_surface = font.render(cell, True, black)
            screen.blit(letter_surface, (j* square_size + square_size // 2 - letter_surface.get_width() // 2, (i+1) * square_size + square_size // 2 - letter_surface.get_height() // 2))
    
    for i in range(size+1):
            number_surface = font.render(str(numbers[i]), True, black)
            screen.blit(number_surface, (i* square_size + square_size // 2 - number_surface.get_width() // 2, j * square_size + square_size // 2 - number_surface.get_height() // 2))
    
    for k in range(1,size+1):
        for j in range(1,size+1):
            if grid_state[k][j] == 'X':
                pygame.draw.line(screen, red, (j * square_size, k * square_size), ((j + 1) * square_size, (k + 1) * square_size), 2)
                pygame.draw.line(screen, red, (j * square_size, (k + 1) * square_size), ((j + 1) * square_size, k * square_size), 2)
            if grid_state[k][j] == '.':
                pygame.draw.rect(screen, black, (j * square_size, k * square_size, square_size, square_size))
    
    for i in range (2,size + 1) :
        pygame.draw.line(screen, white, (i * square_size, square_size), (i * square_size, height))
        pygame.draw.line(screen, white, (square_size, i * square_size), (width, i * square_size))
    pygame.display.update()

    phrase = f"Score : {score} / {amount_boat}"
    score_surface = font.render(phrase, True, black)  
    score_position = score_surface.get_rect(center=(4*width // 5, height + (3/2)*square_size))
    screen.blit(score_surface, score_position) 

    phrase_2 = f"Username : {username}"
    name_surface = font.render(phrase_2, True, black)  
    name_position = name_surface.get_rect(center=( 3*square_size, height + (1/2)*square_size))
    screen.blit(name_surface, name_position)

    sentence_surface =  font.render(last_move, True, black)
    sentence_position = sentence_surface.get_rect(center=( 5*square_size, height + square_size ))
    screen.blit(sentence_surface, sentence_position)



def place_boat(grid_state, amount_boat):
    for i in range (amount_boat):
        x_boat=randint(0,size-1)
        y_boat=randint(0,size-1)
        grid_state[x_boat][y_boat] = 'O'


def battleship_game():

    username = input("Choose your user name")
    last_move = ''
    display_grid(grid_state,username, last_move)
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
                    last_move = 'Congratulations ! You touched a boat !'
                    print("Congratulations ! You touched a boat !")
                    grid_state[row][column] = 'X'
                    if all('O' not in row for row in grid_state):
                        print("Congratulations ! You've sank all boats !")
                        last_move = "Congratulations ! You've sank all boats !"
                        pygame.quit()
                        sys.exit()
                elif grid_state[row][column] == None :
                    grid_state[row][column] = '.'
                    print("What a pity, you've missed.")
                    last_move = "What a pity, you've missed."
        display_grid(grid_state,username,last_move)
        pygame.display.flip()
        pygame.time.wait(1000)





battleship_game()