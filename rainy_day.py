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
refresh_rate = 60

# Colors
GREEN = (0, 175, 0)
WHITE = (255, 255, 255)
BLUE = (0, 55, 255)
YELLOW = (255, 255, 175)
RAIN_BLUE = (148, 162, 183)
GREY = (150, 150, 150)

# Make Stars
''' Make Stars'''
stars = []
for i in range(400):
    x = random.randrange(0, 800)
    y = random.randrange(0, 800)
    r = random.randrange(1, 5)
    s = [x, y, r, r]
    stars.append(s)

# Make clouds
num_clouds = 30
clouds = []
for i in range(num_clouds):
    x = random.randrange(0, 1600)
    y = random.randrange(-50, 200)
    loc = [x, y]
    clouds.append(loc)

def draw_cloud(loc):
    x = loc[0]
    y = loc[1]
    
    pygame.draw.ellipse(screen, GREY, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, GREY, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, GREY, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, GREY, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, GREY, [x + 20, y + 20, 60, 40])

   
# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

    # Game logic
    for c in clouds:
        c[0] += 1

        if c[0] > 900:
           c[0] = random.randrange(-1600, -100)
           c[1] = random.randrange(-50, 10)
           
    for s in stars:
        s[1] += 3
        s[0] += 1

        if s[1] > 600:
           s[1] = random.randrange(-100, 0)
           s[0] = random.randrange(-200, 800)
           
    # Drawing code
    ''' sky '''
    screen.fill(RAIN_BLUE)

    ''' sun '''
    pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])


    ''' grass '''
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])
    
    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)


    
    '''rain'''
    for s in stars:
        pygame.draw.ellipse(screen, BLUE, s)


    ''' clouds '''
    for c in clouds:
        draw_cloud(c)


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
