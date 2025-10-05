import pygame 

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("drawing shapes")

running = True

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(((0,0,0))) # RGB - Black background 

    #colors 
    red = (255,0,0)
    green =(0,255,0)
    blue =(0,0,255)
    white =(255,255,255)

    #draw a red rectangle (x,y, width, height)
    pygame.draw.rect(screen,red,(50,50,200,100))

    #draw a green circle (x,y), radius 
    pygame.draw.circle(screen, green,(400,300),60)

    #darw a blue line (start_x, start_y) to (end_x,end_y)
    pygame.draw.line(screen,blue,(600,100),(750,200),5)
    

    pygame.display.update()

pygame.quit()