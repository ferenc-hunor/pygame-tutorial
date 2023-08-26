import pygame

WIDTH, HEIGHT = 600, 300
BLUE = (0, 0, 255)
BG_COLOR = (127, 127, 127)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
rect_pos_x = 10
rect_pos_y = 20

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill(BG_COLOR)
    pygame.display.update()

pygame.quit()
