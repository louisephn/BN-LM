import pygame
import random

pygame.init()

clock = pygame.time.Clock()

bleu = (70,130,180)

numbers = [i for i in range(1,11)]
letters = ['A','B','C','D','E','F','G','H','I','J']
height = len(letters)
width = len(numbers)

screen = pygame.display.set_mode((width, height))


