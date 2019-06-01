import pygame

pygame.init()

#----------Collision detection
# Determine if there is a collision between two rectangle objects.
def RectangleRectangleCollision(x1,y1,l1,h1, x2,y2,l2,h2):
    isCollision = False

    #Check Top left
    if x1 <= (x2 + l2) and x1 >= (x2):

        if y1 >= y2 and y1 <= (y2 + h2):
            isCollision = True

    # Check top right
    if (x1 + l1)<= (x2 + l2) and (x1 + l1) >= (x2):

        if y1  >= y2 and y1 <= (y2 + h2):
            isCollision = True

    # Check bottom left
    if x1 <= (x2 + l2) and x1 >= (x2):
        if (y1 + h1) >= y2 and (y1 + h1) <= (y2 + h2):
            isCollision = True

    # Check bottom right
    if (x1 + l1) <= (x2 + l2) and (x1 + l1) >= (x2):
        if (y1 + h1) >= y2 and (y1 + h1) <= (y2 + h2):
            isCollision = True

    return isCollision



#---------------Main

#Create a display
gameDisplay = pygame.display.set_mode((500,500))
pygame.display.set_caption("Animated Rectangle")
clock = pygame.time.Clock()

#Global Variables
isRunning = True
RecX  = 30
RecY = 30
int = 0
pressedDown = False

def paint():
    gameDisplay.fill((0,0,0))
    pygame.draw.rect(gameDisplay, (0, 128, 255), pygame.Rect(RecX,RecY, 60,60))
    pygame.draw.rect(gameDisplay, (0, 128, 255), pygame.Rect(200, 200, 60, 60))

    #check if there is an intersection.
    if RectangleRectangleCollision(RecX, RecY,60,60,200,200,60,60):
        print("Collision" + str(RecX))
        pygame.draw.rect(gameDisplay, (255, 0, 144), pygame.Rect(RecX, RecY, 60, 60))
        pygame.draw.rect(gameDisplay, (255, 0, 144), pygame.Rect(200, 200, 60, 60))

    pygame.display.flip()
    clock.tick(100)

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        paint()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            RecX += 9
            paint()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            RecX -= 9
            paint()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            RecY -= 9
            paint()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            RecY += 9
            paint()
