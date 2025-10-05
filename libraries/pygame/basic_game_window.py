import pygame
pygame.init()# initialize all pygame modules 

screen = pygame.display.set_mode((800, 600))#creats the game window 
pygame.display.set_caption("my first game")#sets the window title 

running = True
while running:
    for event in pygame.event.get():#gets all events (e.g. keypress,quit)
        if event.type == pygame.QUIT:#checks if the window is closed 
            running = False

pygame.quit()#properly shuts down pygame 