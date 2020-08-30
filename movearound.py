import pygame

pygame.init()

disp_width=800
disp_height=600

gameDisplay = pygame.display.set_mode((disp_width,disp_height))
pygame.display.set_caption("Racey")

black=(0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed =False
carImg = pygame.image.load("racecar.png")


def car(x,y):
    gameDisplay.blit(carImg,(x,y))

x = (disp_width*.45)
y = (disp_height * .8)
x_change = 0
y_change = 0
car_speed = 0

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            if event.key == pygame.K_RIGHT:
                x_change = 5
            if event.key == pygame.K_UP:
                y_change = -5
            if event.key == pygame.K_DOWN:
                y_change = 5
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN]:
                x_change = 0
                y_change = 0
    x+=x_change
    y+=y_change
    gameDisplay.fill(white)
    car(x,y)

    pygame.display.update()
    clock.tick(90)

pygame.quit()
quit()