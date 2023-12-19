import pygame
import random

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


screen = pygame.display.set_mode((width, height))
screen.fill(blue)

pygame.display.set_caption("Bataille Navale")

for i in range (size+1) :
    pygame.draw.line(screen, white, (i * square_size, 0), (i * square_size, height))
    pygame.draw.line(screen, white, (0, i * square_size), (width, i * square_size))

pygame.display.update()
pygame.time.wait(10000)





