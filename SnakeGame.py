import pygame
import time
import random
pygame.mixer.init()
pygame.mixer.music.load(r'C:\Users\Ujjawal\Pictures\Screenshots\Kya baat ay.mp3')
pygame.mixer.music.play()

pygame.init()

blue=(0,0,255)
green=(0,255,0)
red=(255,0,0)
white=(255,255,255)
black=(0,0,0)

gameWidth=1000
gameHeight=600
block=20
FPS=15

gameWindow=pygame.display.set_mode((gameWidth,gameHeight))
pygame.display.set_caption('Ujjawal -- Snake Game')
pygame.display.update()

clk=pygame.time.Clock()
font=pygame.font.SysFont(None,54)

def snake(block,snakelist):
        for x,y in snakelist:
                pygame.draw.rect(gameWindow,blue,[x,y,block,block])
                
def message_to_screen(msg,color,x,y):
        screen_text=font.render(msg,True,color)
        gameWindow.blit(screen_text,[x,y])

def welcome_screen():
        gameClose=False
        while not gameClose:
                homeImage=pygame.image.load(r"C:\Users\Ujjawal\Pictures\Camera Roll\SnakeHomescreen.jpg").convert()
                gameWindow.blit(homeImage,[0,0])
                message_to_screen("Welcome to the game of Snakes",blue,gameWidth/7,gameHeight/2.5)
                message_to_screen("Press space key to play",blue,gameWidth/7,gameHeight/2)
                pygame.display.update()
                for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                                gameClose=True
                        if event.type==pygame.KEYDOWN:
                                if event.key==pygame.K_SPACE:
                                        loop()

def loop():
        start_x=gameWidth/2
        start_y=gameHeight/2
        update_x=0
        update_y=0
        score=0

        snakeList=[]
        snakelength=1
        
        with open("new.py",'r') as rf:
                highscore=rf.read()

        rAppleX=round(random.randrange(0,gameWidth-block)/20.0)*20.0
        rAppleY=round(random.randrange(0,gameHeight-block)/20.0)*20.0 

        gameClose=False
        gameOver=False

        while not gameClose:
                while gameOver==True:
                        with open("new.py",'w') as wf:
                                wf.write(str(highscore))
                        gameOverImage=pygame.image.load(r"C:\Users\Ujjawal\Pictures\Camera Roll\snake game over.jpg").convert()
                        gameWindow.blit(gameOverImage,[0,0])
                        message_to_screen("You lose!! Press r for replay and q for quit",red,gameWidth/7.5,gameHeight/1.5)
                        pygame.display.update()
                        for event in pygame.event.get():
                                if event.type==pygame.QUIT:
                                        gameClose=True
                                        gameOver=False                                        
                                if event.type==pygame.KEYDOWN:
                                        if event.key==pygame.K_r:
                                                welcome_screen()
                                        if event.key==pygame.K_q:
                                                gameClose=True
                                                gameOver=False
                for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                                gameClose=True
                        if event.type==pygame.KEYDOWN:
                                if event.key==pygame.K_LEFT:
                                        update_x=-block
                                        update_y=0
                                if event.key==pygame.K_RIGHT:
                                        update_x=+block
                                        update_y=0
                                if event.key==pygame.K_UP:
                                        update_y=-block
                                        update_x=0
                                if event.key==pygame.K_DOWN:
                                        update_y=+block
                                        update_x=0    
                        if event.type==pygame.KEYUP:
                                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                                        update_x=0  
                                if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                                        update_y=0    
               
                if start_x>=gameWidth or start_x<0 or start_y>=gameHeight or start_y<0:
                        gameOver=True

                if start_x==rAppleX and start_y==rAppleY:
                        rAppleX=round(random.randrange(0,gameWidth-block)/20.0)*20.0
                        rAppleY=round(random.randrange(0,gameHeight-block)/20.0)*20.0
                        score+=10                         
                        snakelength+=1
                        if score>int(highscore):
                                highscore=score
                   

                start_x+=update_x
                start_y+=update_y
                
                backgroundImage=pygame.image.load(r"C:\Users\Ujjawal\Pictures\Camera Roll\snakeGame.jpg").convert()
                gameWindow.blit(backgroundImage,[0,0])
                message_to_screen("Score is : " + str(score) + "  Highscore is : " + str(highscore),red,5,5)
                pygame.draw.rect(gameWindow,red,[rAppleX,rAppleY,block,block])
                pygame.display.update()
                with open("new.py") as rf:
                        rf.read(int(highscore))

                snakeHead=[]
                snakeHead.append(start_x)
                snakeHead.append(start_y)
                snakeList.append(snakeHead)

                if len(snakeList)>snakelength:
                        del snakeList[0]      
                if snakeHead in snakeList[:-1]:
                        gameOver=True      
              
                snake(block,snakeList)
                pygame.display.update()
                                             
                clk.tick(FPS)               
        pygame.quit()
        quit()

welcome_screen()
