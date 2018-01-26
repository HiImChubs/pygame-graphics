# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make stars and make a picket fence.


# Imports
import pygame
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Sunny Day"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
GREEN = (0, 175, 0)
DARK_GREEN = (0, 104, 0)
DARK_BLUE = (50, 74, 211)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
YELLOW = (255, 255, 175)
BROWN = (99, 57, 15)
BLACK = (0, 0, 0)
LIGHT_GREY = (90, 90, 90)

def draw_cloud(x, y, color):
    pygame.draw.ellipse(screen, color, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, color, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, color, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, color, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, color, [x + 20, y + 20, 60, 40])


stars = []
for i in range(200):
    x = random.randrange(0, 800)
    y = random.randrange(0, 400)
    r = random.randrange(1, 4)
    s = [x, y, r, r]
    stars.append(s)

# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

    # Game logic

             
    # Drawing code
    ''' sky '''
    screen.fill(BLUE)

    ''' sun '''
    pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])

    ''' clouds '''
    draw_cloud(50, 150, LIGHT_GREY)
    draw_cloud(250, 75, LIGHT_GREY)
    draw_cloud(350, 125, LIGHT_GREY)
    draw_cloud(450, 175, LIGHT_GREY)
    draw_cloud(650, 100, LIGHT_GREY)

    ''' grass '''
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],[x+10, y+40], [x, y+40], [x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)


    ''' stars '''
    for s in stars:
        pygame.draw.ellipse(screen, DARK_BLUE, s)

    '''draw house'''
    pygame.draw.rect(screen, BROWN, [550, 300, 200, 150])
    pygame.draw.polygon(screen, LIGHT_GREY, [[650, 220], [530, 300], [770, 300]])
    pygame.draw.rect(screen, BLACK, [600, 400, 50, 50])

    '''draw tree'''
    pygame.draw.rect(screen, BROWN, [227, 300, 20, 200])
    pygame.draw.ellipse(screen, DARK_GREEN, [200, 295, 75, 150])
    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
