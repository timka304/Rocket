import pygame
from pygame.locals import *
import time

pygame.init()

pygame.font.init()

screen = pygame.display.set_mode((600, 600))
player_x = 200
player_y = 200

rocket = pygame.image.load("images/rocket.png")
background = pygame.image.load("images/sky.png")

while True:
    screen.blit(background, (0,0))
    screen.blit(rocket, (player_x, player_y))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and player_y > 0:
                player_y -= 20
                pygame.display.update()
            if event.key == pygame.K_s and player_y < 450:
                player_y += 20
                pygame.display.update()
            if event.key == pygame.K_a and player_x > 0:
                player_x -= 20
                pygame.display.update()
            if event.key == pygame.K_d and player_x < 450:
                player_x += 20
                pygame.display.update()
    
    pygame.display.update()
            