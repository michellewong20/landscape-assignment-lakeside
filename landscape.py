from cmath import rect
from turtle import width
import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
# -------------------------
# Initialize global variables

circle_x = 50
circle_y = 50
circle_x_speed = 3

wave = (236, 246, 253)

bush_x = 420
bush_y = 400

cloud_x = 150
cloud_y = 100

cloud_x_2 = 20
cloud_y_2 = 30

cloud_x_3 = 200
cloud_y_3 = 10

cloud_x_4 = 5
cloud_y_4 = 90

sun_x = 30
sun_y = 30

tree_x = 550
tree_y = 200

tree_x_2 = 450
tree_y_2 = 200

tree_x_3 = 470
tree_y_3 = 250

rock_x = 350
rock_y = 350

wave_x = 100
wave_y = 100
wave_x_speed = 1

wave_x = 244
wave_y = 380


#--------------------------
running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here
    # if the ball goes beyond the width
    
    if cloud_x > WIDTH:
        cloud_x *= 1
    
    cloud_x += circle_x_speed #speed
    cloud_y += 0

    if cloud_x_2 > WIDTH:
        cloud_x_2 *= 1
    
    cloud_x_2 += circle_x_speed #speed
    cloud_y_2 += 0

    if cloud_x_3 > WIDTH:
        cloud_x_3 *= 1
    
    cloud_x_3 += circle_x_speed #speed
    cloud_y_3 += 0

    if cloud_x_4 > WIDTH:
        cloud_x_4 *= 1
    
    cloud_x_4 += circle_x_speed #speed
    cloud_y_4 += 0
    # DRAWING
    screen.fill((123, 193, 255))  # always the first drawing command

    # lake
    pygame.draw.rect(screen, (0, 86, 207), (0, 340, 400, 250))

    
    # rectangle
    pygame.draw.rect(screen, (46, 135, 46), (340, 340, 600, 990))
   
    
    # ellipse
   
    #tree
    pygame.draw.rect(screen, (69, 30, 6), (tree_x, tree_y, 40, 150))  # trunk
    pygame.draw.circle(screen, (22, 71, 18), (tree_x + 25, tree_y), 60, 200)  # leaves

    pygame.draw.rect(screen, (69, 30, 6), (tree_x_2, tree_y_2, 40, 150))  # trunk
    pygame.draw.circle(screen, (60, 91, 27), (tree_x_2 + 25, tree_y_2), 60, 200)  # leaves
    # Bush
    pygame.draw.circle(screen, (7, 77, 0), (bush_x, bush_y - 2), 30)
    pygame.draw.circle(screen, (7, 77, 0), (bush_x + 26, bush_y), 25)
    pygame.draw.circle(screen, (7, 77, 0), (bush_x - 20, bush_y + 2), 25)
    
    pygame.draw.circle(screen, (7, 77, 0), (bush_x + 40, bush_y + 60), 30)
    pygame.draw.circle(screen, (7, 77, 0), (bush_x + 75, bush_y + 70), 25)
    pygame.draw.circle(screen, (7, 77, 0), (bush_x + 5, bush_y + 70), 25)

    pygame.draw.rect(screen, (69, 30, 6), (tree_x_3, tree_y_3, 40, 150))  # trunk
    pygame.draw.circle(screen, (22, 71, 18), (tree_x_3 + 25, tree_y_3), 60, 200)

    pygame.draw.rect(screen, (96, 54, 6), (tree_x_3 + 70, tree_y_3 + 30, 40, 150))  # trunk
    pygame.draw.circle(screen, (31, 105, 20), (tree_x_3 + 95, tree_y_3 + 30), 60, 200)

    pygame.draw.rect(screen, (86, 31, 3), (tree_x_3 + 100, tree_y_3 + 70, 40, 150))  # trunk
    pygame.draw.circle(screen, (79, 116, 41), (tree_x_3 + 115, tree_y_3 + 70), 60, 200)
    #clouds
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x, cloud_y), 35)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x + 26, cloud_y), 25)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x - 25, cloud_y - 16), 25)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x - 20, cloud_y - 15), 30)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x - 15, cloud_y), 30)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x - 40, cloud_y), 30)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x - 70, cloud_y + 5), 20)

    # cloud 2
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x_2, cloud_y_2), 35)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x_2 + 26, cloud_y_2), 25)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x_2 - 25, cloud_y_2 - 16), 25)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x_2 - 20, cloud_y_2 - 15), 30)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x_2 - 15, cloud_y_2), 30)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x_2 - 40, cloud_y_2), 30)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x_2 - 70, cloud_y_2 + 5), 20)

    #clouds 3
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x_3, cloud_y_3), 35)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x_3 + 26, cloud_y_3), 25)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x_3 - 25, cloud_y_3 - 16), 25)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x_3 - 20, cloud_y_3 - 15), 30)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x_3 - 15, cloud_y_3), 30)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x_3 - 40, cloud_y_3), 30)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x_3 - 70, cloud_y_3 + 5), 20)
    
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x_4, cloud_y_4), 35)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x_4 + 26, cloud_y_4), 25)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x_4 - 25, cloud_y_4 - 16), 25)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x_4 - 20, cloud_y_4 - 15), 30)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x_4 - 15, cloud_y_4), 30)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x_4 - 40, cloud_y_4), 30)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x_4 - 70, cloud_y_4 + 5), 20)
    # arc

    #sun
    pygame.draw.circle(screen, (255, 248, 56), (sun_x, sun_y), 60)

    #rock
    pygame.draw.circle(screen, (93, 93, 93), (rock_x, rock_y), 15)
    pygame.draw.circle(screen, (74, 73, 72), (rock_x + 1, rock_y + 10), 17)
    pygame.draw.circle(screen, (56, 56, 56), (rock_x + 2, rock_y + 20), 17)
    pygame.draw.circle(screen, (93, 93, 93), (rock_x + 3, rock_y + 30), 15)
    pygame.draw.circle(screen, (52, 52, 52), (rock_x + 1, rock_y + 40), 17)
    pygame.draw.circle(screen, (56, 56, 56), (rock_x, rock_y + 50), 15)
    pygame.draw.circle(screen, (52, 52, 52), (rock_x + 1, rock_y + 60), 16)
    pygame.draw.circle(screen, (93, 93, 93), (rock_x, rock_y + 70), 17)
    pygame.draw.circle(screen, (56, 56, 56), (rock_x, rock_y + 80), 19)
    pygame.draw.circle(screen, (93, 93, 93), (rock_x, rock_y + 95), 15)
    pygame.draw.circle(screen, (52, 52, 52), (rock_x, rock_y + 110), 19)
    pygame.draw.circle(screen, (56, 56, 56), (rock_x - 1, rock_y + 120), 18)
    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()