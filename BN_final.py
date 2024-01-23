import pygame
from random import randint
import sys

pygame.init()

clock = pygame.time.Clock()


# colors 
blue = (70, 130, 180)
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)
pink = (249, 66, 158)



letters = ['A','B','C','D','E','F','G','H','I','J']
size = len(letters)
numbers = [i for i in range(size + 1)]
square_size = 50
height = (size + 1) * square_size
width = (size + 1) * square_size
grid_state = [[None for i in range(size + 1)]for k in range(size + 1)] # Matrix containing the state of each of the cells in our grid
amount_boat1 = 4
amount_boat2 = 5
amount_boat3 = 3
amount_boat = amount_boat1 + amount_boat2 + amount_boat3
font = pygame.font.Font(None, 36)

def display_grid(grid_state, username, score, last_move):
    """
    Function handling the display of the game screen:
    displaying the grid along with indexing for orientation in the grid,
    the username, the number of sunken ships, and the comment after each attempt.
    """
    screen = pygame.display.set_mode((width, height + 2 * square_size))
    screen.fill(blue)
    pygame.display.set_caption("Battleship")

    
    for k in range(size + 1): # Creating white borders (top, bottom, and left) and black lines between white cells.
        pygame.draw.rect(screen, white, (0,  k * square_size, square_size, square_size))
        pygame.draw.rect(screen, white, (k * square_size, 0, square_size, square_size)) 
        pygame.draw.rect(screen, white, (k * square_size, height, square_size, square_size))
        pygame.draw.rect(screen, white, (k * square_size, (height + square_size), square_size, square_size)) 

        pygame.draw.line(screen, black, (k * square_size, 0), (k * square_size, square_size))
        pygame.draw.line(screen, black, (0, k * square_size), (square_size, k * square_size))
    
    # Creating black border lines between the frame and the game grid
    pygame.draw.line(screen, black, (square_size, 0), (square_size, height))
    pygame.draw.line(screen, black, (0, square_size), (width, square_size))
    
    # Displaying letters along the border
    for i, row in enumerate(letters):
        for j, cell in enumerate(row):
            letter_surface = font.render(cell, True, black)
            screen.blit(letter_surface, (j * square_size + square_size // 2 - letter_surface.get_width() // 2, (i + 1) * square_size + square_size // 2 - letter_surface.get_height() // 2))
    
    # Displaying numbers along the border
    for i in range(size + 1):
            number_surface = font.render(str(numbers[i]), True, black)
            screen.blit(number_surface, (i * square_size + square_size // 2 - number_surface.get_width() // 2, j * square_size + square_size // 2 - number_surface.get_height() // 2))
    
    # Displaying the state of the grid: hit ships, sunk ships, and missed attempts
    for k in range(1, size + 1):
        for j in range(1, size + 1):
            if grid_state[k][j] == 'X':
                pygame.draw.line(screen, red, (j * square_size, k * square_size), ((j + 1) * square_size, (k + 1) * square_size), 2)
                pygame.draw.line(screen, red, (j * square_size, (k + 1) * square_size), ((j + 1) * square_size, k * square_size), 2)
            elif grid_state[k][j] == '.':
                pygame.draw.rect(screen, black, (j * square_size, k * square_size, square_size, square_size))
            elif grid_state[k][j] == 'T':
                pygame.draw.rect(screen, green, (j * square_size, k * square_size, square_size, square_size))
    
    # Displaying the white lines delineating the grid cells
    for i in range (2,size + 1) :
        pygame.draw.line(screen, white, (i * square_size, square_size), (i * square_size, height))
        pygame.draw.line(screen, white, (square_size, i * square_size), (width, i * square_size))
    pygame.display.update()

    # Displaying the score throughout the game (number of ships sunk / total number of ships)
    phrase = f"Score : {score} / {amount_boat}"
    score_surface = font.render(phrase, True, black)  
    score_position = score_surface.get_rect(center = (4 * width // 5, height + (3/2) * square_size))
    screen.blit(score_surface, score_position) 

    # Displaying the player's name
    phrase_2 = f"Username : {username}"
    name_surface = font.render(phrase_2, True, black)  
    name_position = name_surface.get_rect(center = (3 * square_size, height + (1/2) * square_size))
    screen.blit(name_surface, name_position)

    # Displaying the comment on the last attempt 
    sentence_surface =  font.render(last_move, True, red)
    sentence_position = sentence_surface.get_rect(center = ( 5 * square_size, height + square_size ))
    screen.blit(sentence_surface, sentence_position)



def place_boat(grid_state, amount_boat1, amount_boat2, amount_boat3):
    """
    Function randomly placing the ships on the grid.
    The number of ships of each size can be adjusted.
    Ensuring that no two ships overlap and that they do not exceed the grid boundaries.
    The ships can be oriented in any direction, and ships of size 3 can also have a corner shape.
    """
    for i in range (amount_boat1): # Placement of size 1 ships.
        incorrect_position = True
        while incorrect_position :
            x_boat = randint(1,size - 1)
            y_boat = randint(1,size - 1)
            if grid_state[x_boat][y_boat] == None: # Checking for no overlapping
                incorrect_position = False
        grid_state[x_boat][y_boat] = 'O' # update of the matrix with the new boat
    for i in range (amount_boat2): # Placement of size 2 ships.
        incorrect_position = True
        while incorrect_position :
            x_head = randint(1, size - 2)
            y_head = randint(1, size - 2)
            direction = randint(1,2)
            x_boat = x_head + direction % 2
            y_boat = y_head + direction // 2
            if grid_state[x_head][y_head] == None: # Checking for no overlapping
                if grid_state[x_boat][y_boat] == None :
                    incorrect_position = False
        grid_state[x_head][y_head] = [(x_boat,y_boat)]  # update of the matrix with the new boat
        grid_state[x_boat][y_boat] = [(x_head,y_head)]
    for i in range (amount_boat3): # Placement of size 3 ships.
        incorrect_position = True
        while incorrect_position :
            x_head = randint(1, size - 3)
            y_head = randint(1, size - 3)
            direction = randint(1,2)
            x_boat1 = x_head + direction % 2
            y_boat1 = y_head + direction // 2
            x_boat2 = x_head + 2 * direction % 2
            y_boat2 = y_head + 2 * direction // 2
            if grid_state[x_head][y_head] == None :  # Checking for no overlapping
                if grid_state[x_boat1][y_boat1] == None :
                    if grid_state[x_boat2][y_boat2] == None :
                        incorrect_position = False 
        grid_state[x_head][y_head] = [(x_boat1,y_boat1),(x_boat2,y_boat2)]  # update of the matrix with the new boat
        grid_state[x_boat1][y_boat1] = [(x_head,y_head),(x_boat2,y_boat2)]
        grid_state[x_boat2][y_boat2] = [(x_head,y_head),(x_boat1,y_boat1)]



def battleship_game():
    """
    Our main function, 
    calling upon our auxiliary functions and managing the flow of the game
    """
    score = 0
    username = input("Choose your user name : ")
    last_move = ''
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
                if grid_state[row][column] == 'O': # check if the player touched a size one boat
                    score += 1 # update of the score
                    print("Congratulations ! You have sunk a boat !")
                    last_move = "Congratulations ! You have sunk a boat !"
                    grid_state[row][column] = 'X' # update of the matrix
                    if all('O' not in row for row in grid_state) and all ('T' not in row for row in grid_state ): # check if all the boats have been sunk
                        print("Congratulations ! You've sank all boats !")
                        last_move = "Congratulations ! You've sank all boats !"
                        pygame.quit() 
                        sys.exit() # end the game
                elif type(grid_state[row][column]) == list : # check if the player touched a size two or three boat
                    boat_sunk = True
                    print("Congratulations ! You touched a boat !")
                    last_move = "Congratulations ! You touched a boat !"
                    for i in grid_state[row][column]:
                        if grid_state[i[0]][i[1]] !='T': # check if the boat has been sunk or only touched 
                            boat_sunk = False
                    if boat_sunk :
                        score += 1
                        for i in grid_state[row][column]:
                            grid_state[i[0]][i[1]] = 'X' # update of the matrix
                        grid_state[row][column] = 'X' # update of the matrix
                        print("Congratulations ! You have sunk a boat !")
                        last_move = "Congratulations ! You have sunk a boat !"
                    else:
                        grid_state[row][column] = 'T' # update of the matrix
                elif grid_state[row][column] == None :
                    grid_state[row][column] = '.' # update of the matrix
                    last_move = "What a pity, you've missed."
                    print("What a pity, you've missed.")
        display_grid(grid_state, username, score, last_move) # update of the screen
        pygame.display.flip()
        pygame.time.wait(1000)





battleship_game()


"""
APPENDIX

We began to develop a few small functions that we could have used in our two-player playable version. 
Although this ultimate goal could not be achieved, 
here are some code snippets that correspond to the beginning of our consideration on this matter.

"""



def place_boat_by_the_player(grid_state, amount_boat1, amount_boat2, amount_boat3):
    """
    Function that allows the player to manually place their ships by clicking on the grid.
    The player first places ships of size 1, then size 2, and finally size 3.
    They cannot place two overlapping ships.
    This version does not check whether the player places their ships outside the grid.
    We did not have time to thoroughly test this function.
    """
    boat1_placed = 0
    boat2_placed = 0
    boat3_placed = 0
    while boat1_placed < amount_boat1 :
        print("Place ", amount_boat1 - boat1_placed," size 1 boats" )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                row = position[1] // square_size 
                column = position[0] // square_size 
                if grid_state [row, column] == None:
                    boat1_placed += 1
                    grid_state[row, column] = 'O'
    while boat2_placed < amount_boat2 :
        print("Place ", amount_boat2 - boat2_placed," size 2 boats" )
        boat_case = []
        while len(boat_case) < 2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    row = position[1] // square_size
                    column = position[0] // square_size
                    if grid_state [row, column] == None and (row,column) not in boat_case:
                        boat_case.append((row,column))
        if boat_case[0][0] == boat_case[1][0] and boat_case[0][1] - boat_case[1][1] == 1 :
            grid_state[boat_case[0][0]][boat_case[0][1]] = boat_case[1]
            grid_state[boat_case[1][0]][boat_case[1][1]] = boat_case[0]
            boat2_placed += 1
        elif boat_case[0][1] == boat_case[1][1] and abs(boat_case[0][0] - boat_case[1][0]) == 1 :
            grid_state[boat_case[0][0]][boat_case[0][1]] = boat_case[1]
            grid_state[boat_case[1][0]][boat_case[1][1]] = boat_case[0]
            boat2_placed += 1
    while boat3_placed < amount_boat3 :
        print("Place ", amount_boat3 - boat3_placed," size 3 boats" )
        boat_case=[]
        while len(boat_case) < 3:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    row = position[1] // square_size
                    column = position[0] // square_size
                    if grid_state [row, column] == None and (row,column) not in boat_case :
                        boat_case.append((row,column))
        horizontal = boat_case[0][0] == boat_case[1][0]
        vertical = boat_case[0][1] == boat_case[1][1]
        if horizontal:
            if abs(boat_case[0][1] - boat_case[1][1]) < 2:
                if abs(boat_case[2][1] - boat_case[1][1]) < 2:
                    if abs(boat_case[0][1] - boat_case[2][1]) < 2:
                        grid_state[boat_case[0][0]][boat_case[0][1]] = (boat_case[1],boat_case[2])
                        grid_state[boat_case[1][0]][boat_case[1][1]] = (boat_case[0],boat_case[2])
                        grid_state[boat_case[2][0]][boat_case[2][1]] = (boat_case[0],boat_case[1])
                        boat3_placed +=1
            

def display_grid_double(grid_state, username, score, last_move):
    """
    Function to display two grids simultaneously.
    Eventually, these two grids should allow the player to see both the state of their own grid
    (with the ships they have placed) and the state of their opponent's grid (with the ships they have sunk).
    """

    screen = pygame.display.set_mode((2*width + square_size, height + 2 * square_size))
    screen.fill(blue)
    pygame.display.set_caption("Battleship")

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


"""
And finally, a small code snippet for displaying a timer measuring elapsed time.
Unfortunately, we were unable to integrate it into the rest of our code.


import pygame
import sys
import time

# Initialization of Pygame
pygame.init()

# Definition of constants
width, height = size + 1) * square_size, size + 1) * square_size

# Creation of the window
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chronometer")

# Font
font = pygame.font.Font(None, 36)

# Variables for the timer:
time_start = time.time()
timer_on = True

# Main loop:
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    # Calculate elapsed time
    time_spent = time.time() - time_start

    # Display elapsed time
    text = font.render(f'Time : {time_spent : .1f} s', True, black)
    window.blit(text, (200, 20))

    # Update the screen
    pygame.display.flip()

    # Regulate the loop speed
    pygame.time.Clock().tick(1)

"""