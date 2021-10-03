import pygame

pygame.init()

screen_width = 50*10 + 50
screen_height = 50*20 + 20

unit_side = 50 #the size of the individual blocks making the other usable blocks

game_width = 50*10
game_height = 50*20

screen = pygame.display.set_mode((screen_width, screen_height))#the actual game area is the 50*10 and 50*20
screen.fill((255, 255, 255))


def draw_lines():
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(25, 10, game_width, game_height), 3)
    start_y = 10
    start_x = 25
    for i in range(9):
        pygame.draw.line(screen, (0,0,0), (start_x + unit_side*(i+1), start_y), (start_x + unit_side*(i+1),start_y + game_height ), 3)
    for i in range(19):
        pygame.draw.line(screen, (0,0,0), (start_x, start_y + unit_side*(i+1)), (start_x + game_width, start_y + unit_side*(i+1)), 3)



draw_lines()
running = True
while running:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

