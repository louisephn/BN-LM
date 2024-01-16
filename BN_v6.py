import pygame
from random import randint
import sys
import time

pygame.init()

clock = pygame.time.Clock()

blue = (70, 130, 180)
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)
pink = (238,196,201)



letters = ['A','B','C','D','E','F','G','H','I','J']
size = len(letters)
numbers = [i for i in range(size + 1)]
square_size = 50
height = (size + 1) * square_size
width = (size + 1) * square_size
grid_state = [[None for i in range(size + 1)]for k in range(size + 1)]
amount_boat1 = 4
amount_boat2 = 5
amount_boat3 = 3
amount_boat = amount_boat1 + amount_boat2 + amount_boat3
font = pygame.font.Font(None, 36)

def display_grid(grid_state, username, score, last_move):
    screen = pygame.display.set_mode((2*width + square_size, height + 2 * square_size))
    screen.fill(blue)
    pygame.display.set_caption("Bataille Navale")

    for k in range(size+1):
        pygame.draw.rect(screen, white, (0, k*square_size, square_size, square_size))
        pygame.draw.rect(screen, white, (k * square_size, 0, square_size, square_size)) 
        pygame.draw.rect(screen, white, (k*square_size, height, square_size, square_size))
        pygame.draw.rect(screen, white, (k*square_size, (height+square_size),square_size, square_size)) 

        pygame.draw.line(screen, black, (k*square_size, 0), (k*square_size, square_size))
        pygame.draw.line(screen, black, (0, k*square_size), (square_size, k*square_size))

        pygame.draw.rect(screen, white, (width+square_size, k*square_size, square_size, square_size))
        pygame.draw.line(screen, black, (width+square_size, k*square_size), (width + 2*square_size, k*square_size))

    for k in range(size+1, 2*size+3):
        pygame.draw.rect(screen, white, (k * square_size, 0, square_size, square_size)) 
        pygame.draw.rect(screen, white, (k*square_size, height, square_size, square_size))
        pygame.draw.rect(screen, white, (k*square_size, (height+square_size),square_size, square_size)) 
        pygame.draw.line(screen, black, (k*square_size, 0), (k*square_size, square_size))
        
        

    pygame.draw.line(screen, black, (square_size, 0), (square_size, height))
    pygame.draw.line(screen, black, (0, square_size), (width, square_size))
    pygame.draw.line(screen, black, (width, 0), (width, height))
    pygame.draw.line(screen, black, (width+square_size, 0), (width+ square_size, height))
    pygame.draw.line(screen, black, (width+2*square_size, 0), (width+ 2*square_size, height))
    pygame.draw.line(screen, black, (width+ square_size, square_size), (2*width+3*square_size, square_size))
    pygame.draw.rect(screen, pink, (width, 0, square_size, height))
    
    
    for i, row in enumerate(letters):
        for j, cell in enumerate(row):
            letter_surface = font.render(cell, True, black)
            screen.blit(letter_surface, (j* square_size + square_size // 2 - letter_surface.get_width() // 2, (i + 1) * square_size + square_size // 2 - letter_surface.get_height() // 2))
            screen.blit(letter_surface, (width + square_size + j* square_size + square_size // 2 - letter_surface.get_width() // 2, (i + 1) * square_size + square_size // 2 - letter_surface.get_height() // 2))

    for i in range(size+1):
            number_surface = font.render(str(numbers[i]), True, black)
            screen.blit(number_surface, (i* square_size + square_size // 2 - number_surface.get_width() // 2, j * square_size + square_size // 2 - number_surface.get_height() // 2))
            screen.blit(number_surface, (width + square_size + i* square_size + square_size // 2 - number_surface.get_width() // 2, j * square_size + square_size // 2 - number_surface.get_height() // 2))


    for k in range(1,size+1):
        for j in range(1,size+1):
            if grid_state[k][j] == 'X':
                pygame.draw.line(screen, red, (j * square_size, k * square_size), ((j + 1) * square_size, (k + 1) * square_size), 2)
                pygame.draw.line(screen, red, (j * square_size, (k + 1) * square_size), ((j + 1) * square_size, k * square_size), 2)
            elif grid_state[k][j] == '.':
                pygame.draw.rect(screen, black, (j * square_size, k * square_size, square_size, square_size))
            elif grid_state[k][j] == 'T':
                pygame.draw.rect(screen, green, (j * square_size, k * square_size, square_size, square_size))
    
    for i in range (2,size +1) :
        pygame.draw.line(screen, white, (i * square_size, square_size), (i * square_size, height))
        pygame.draw.line(screen, white, (square_size, i * square_size), (width, i * square_size))
        pygame.draw.line(screen, white, (width + 2*square_size, i * square_size), (2*width+3*square_size, i * square_size))

    for i in range (size +4,2*size + 3) :
        pygame.draw.line(screen, white, (i * square_size, square_size), (i * square_size, height))
        
    pygame.display.update()

    phrase = f"Score : {score} / {amount_boat}"
    score_surface = font.render(phrase, True, black)  
    score_position = score_surface.get_rect(center = (8  * width // 5, height + (3/2) * square_size))
    screen.blit(score_surface, score_position) 

    phrase_2 = f"Username : {username}"
    name_surface = font.render(phrase_2, True, black)  
    name_position = name_surface.get_rect(center = ( 3*square_size, height + (1/2) * square_size))
    screen.blit(name_surface, name_position)

    sentence_surface =  font.render(last_move, True, red)
    sentence_position = sentence_surface.get_rect(center = ( width + 6 * square_size, height + square_size ))
    screen.blit(sentence_surface, sentence_position)

def place_boat(grid_state, amount_boat1, amount_boat2, amount_boat3):
    for i in range (amount_boat1):
        x_boat = randint(1,size - 1)
        y_boat = randint(1,size - 1)
        grid_state[x_boat][y_boat] = 'O'
    for i in range (amount_boat2):
        incorrect_position = True
        while incorrect_position :
            x_head = randint(1, size - 2)
            y_head = randint(1, size - 2)
            direction = randint(1,2)
            x_boat = x_head + direction % 2
            y_boat = y_head + direction // 2
            if grid_state[x_head][y_head] == None:
                if grid_state[x_boat][y_boat] == None :
                    incorrect_position = False
        grid_state[x_head][y_head] = [(x_boat,y_boat)]
        grid_state[x_boat][y_boat] = [(x_head,y_head)]
    for i in range (amount_boat3):
        incorrect_position = True
        while incorrect_position :
            x_head = randint(1, size - 3)
            y_head = randint(1, size - 3)
            direction = randint(1,2)
            x_boat1 = x_head + direction % 2
            y_boat1 = y_head + direction // 2
            x_boat2 = x_head + 2 * direction % 2
            y_boat2 = y_head + 2 * direction // 2
            if grid_state[x_head][y_head] == None :
                if grid_state[x_boat1][y_boat1] == None :
                    if grid_state[x_boat2][y_boat2] == None :
                        incorrect_position = False 
        grid_state[x_head][y_head] = [(x_boat1,y_boat1),(x_boat2,y_boat2)]
        grid_state[x_boat1][y_boat1] = [(x_head,y_head),(x_boat2,y_boat2)]
        grid_state[x_boat2][y_boat2] = [(x_head,y_head),(x_boat1,y_boat1)]



def battleship_game():
    score = 0
    username = input("Choose your user name : ")
    last_move=''
    
    display_grid(grid_state,username, score, last_move)
    place_boat(grid_state, amount_boat1, amount_boat2, amount_boat3)

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
                    score += 1
                    print("Congratulations ! You touched a boat !")
                    last_move = "Congratulations ! You touched a boat !"
                    grid_state[row][column] = 'X'
                    if all('O' not in row for row in grid_state) and all ('T' not in row for row in grid_state ):
                        print("Congratulations ! You've sank all boats !")
                        last_move = "Congratulations ! You've sank all boats !"
                        pygame.quit()
                        sys.exit()
                elif type(grid_state[row][column]) == list :
                    boat_sinked = True
                    for i in grid_state[row][column]:
                        if grid_state[i[0]][i[1]] !='T':
                            boat_sinked = False
                    if boat_sinked :
                        score += 1
                        for i in grid_state[row][column]:
                            grid_state[i[0]][i[1]] = 'X'
                        grid_state[row][column] = 'X'
                    else:
                        grid_state[row][column] = 'T'
                elif grid_state[row][column] == None :
                    grid_state[row][column] = '.'
                    last_move = "What a pity, you've missed."
                    print("What a pity, you've missed.")
        display_grid(grid_state,username, score, last_move)

    

        pygame.display.flip()
    
        pygame.time.wait(1000)




battleship_game()