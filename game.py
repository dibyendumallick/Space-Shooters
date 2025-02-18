import pygame
import random
import math
# Initialize the pygame
pygame.init()

# Initialize the display  height=600 , width= 800 
screen = pygame.display.set_mode((800, 600))

#background image
background=pygame.image.load('C:\\Users\\DIBYENDU\\Desktop\\python\\pygame\\beautiful-view-stars-night-sky.jpg')


#title and Icon
pygame.display.set_caption("Space Shooters")
icon=pygame.image.load('C:\\Users\\DIBYENDU\\Desktop\\python\\pygame\\images.png')
pygame.display.set_icon(icon) 

#------------------------------------------------------------------------
#player
playerImage=pygame.image.load('C:\\Users\\DIBYENDU\\Desktop\\python\\pygame\\arcade-game (1).png')

#position of player (X and Y cooordinates)
playerX=350
playerY=500
playerX_change=0

def player(x,y):
    screen.blit(playerImage, (x, y)) #blit meaning draw.This means we are drawing the image of the player in the screen
    
#-----------------------------------------------------------------------    
#enemy
#---------------------------
#multiple enemy
enemyImage=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=6

for i in range(num_of_enemies):
    enemyImage.append(pygame.image.load('C:\\Users\\DIBYENDU\\Desktop\\python\\pygame\\alien.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)

def enemy(x,y):
     screen.blit(enemyImage[i],(x,y))
     
#score

score_val=0
font=pygame.font.Font('freesansbold.ttf',32)

textX=10
textY=10

def showScore(x,y):
    score=font.render("Score : " + str(score_val), True, (255,255,255))
    screen.blit(score,(x,y))

#----------------------------------------------------------------------
#bullet
#Ready-You can't see the bullet on the screen
#fire-The bullet is currently moving
bulletImage=pygame.image.load('C:\\Users\\DIBYENDU\\Desktop\\python\\pygame\\bullet.png')
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=0.5
bullet_State="ready"
   
def fire_bullet(x, y):
    global bullet_State
    bullet_State = "fire"
    screen.blit(bulletImage, (x + 16, y + 10))  # give the position of the bullet from the spaceship
#----------------------------------------------------------------------  
#collision
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance<27:
        return True
    else:
        return False   
#--------------------------------------------------------------------
#infinite game loop(it says that the game should not stop)/Event loop
running = True
while running:
    #background color for pygame board by r g b.The parenthesis takes r g b
    screen.fill((0,0,0))
    #background Image
    screen.blit(background,(0,0))
    
    #iterate through all the event function,unless you get the quit button 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #if key is pressed,check whether is right or left
        if event.type ==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-0.3
                
            if event.key==pygame.K_RIGHT:
                playerX_change=+0.3
                
            if event.key == pygame.K_SPACE:
                 if bullet_State == "ready":
                  bulletX = playerX  # Get the current x coordinate of the spaceship
                  fire_bullet(bulletX, bulletY)
                
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change=0


    #player movement            
    playerX=playerX+playerX_change
    #boundaries of spaceship
    if playerX <=0:
        playerX = 0
    elif playerX >=736:
        playerX = 736    
    #player moving
    player(playerX,playerY)
    
    
        
    #enemy movement
    for i in range(num_of_enemies):
        enemyX[i]=enemyX[i]+enemyX_change[i]
        #boundaries of enemy
        if enemyX[i] <=0:
            enemyX_change[i] = 0.3
            enemyY[i]=enemyY[i]+enemyY_change[i]
        elif enemyX[i] >=736:
            enemyX_change[i]= -0.3
            enemyY[i]=enemyY[i]+enemyY_change[i]    
        #enemy moving
        
        
        #collision
        collision=isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bulletY=480
            bullet_State="ready"
            score_val=score_val+1
            enemyX[i]=random.randint(0,800)
            enemyY[i]=random.randint(50,150)
        enemy(enemyX[i],enemyY[i])  
    
   # bullet movement
    if bullet_State is "fire":
        bulletY=bulletY-bulletY_change
        fire_bullet(bulletX,bulletY)
        
    if bulletY<=0:
        bulletY=480
        bullet_State="ready"
        
    
    showScore(textX,textY)
    
    #player moving
    player(playerX,playerY)
    
    #display update
    pygame.display.update()
     
    
pygame.quit()

