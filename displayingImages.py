import pygame
pygame.init()

d_dims=d_width,d_height=1920,1080

gameDisplay = pygame.display.set_mode(d_dims)
pygame.display.set_caption("Racer")

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed= False
carImg = pygame.image.load("racecar.png")
roadImg = pygame.image.load("road.jpg")

def car(x,y):
    gameDisplay.blit(carImg, (x,y))
x = d_width*0.45
y = d_height*.8

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        
    gameDisplay.fill(white)
    car(x,y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()