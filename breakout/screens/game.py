import random
import pygame
from ..components.sprite import MySprite
from screens import BaseScreen
#import score here
from ..components import Paddle, Ball, TileGroup, Score
from components import TextBox, text
import time




class GameScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        
        # Initializing scoring variable
        self.score=Score()
        self.multiplier=1
        #Looks at time taken to complete a round, starts here
        self.time_start = time.time()

        #Call score object here
        super().__init__(*args, **kwargs)

        # Create background and set mario location 
        self.background=MySprite()
        self.background.rect.x=300
        self.background.rect.y=300
        
        self.multiplier=1
        

        # Create the paddle
        self.paddle = Paddle(200, 30, (0, 255, 0), limits=self.rect)

        # Create the ball
        self.ball = Ball(limits=self.rect)
        self.ball.speed = 8

        self.ball.angle = random.randint(0, 31416) / 10000

        # Create the tiles from a file 
        self.tiles = TileGroup(tile_width=120, tile_height=30)

        # Put all sprites in the group
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.background)
        self.sprites.add(self.paddle)
        self.sprites.add(self.ball)
    # looks at colissions using this method
    
    def update(self):
        

        level=0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.paddle.move("left")

        if keys[pygame.K_RIGHT]:
            self.paddle.move("right")
        
        self.sprites.update()
        collided = self.ball.collidetiles(self.tiles)
        # print(collided) #can be used to calculate score 

                
        self.tiles_left=int(len(self.tiles)/4)

        if self.tiles_left==0:
            print("Next Level")
            self.tiles = TileGroup(tile_width=120, tile_height=30, level=level)
            level+=1

        #Created scoring system below and multiplier 
        if collided:
            #accessing score in score object
            self.score.score+=(1+self.multiplier)
            self.multiplier+=0.25
        # rendering score on screen
        self.score.text=self.score.font.render(str(self.score.score),True,(0,0,0))

        
        
        caught_the_ball = self.ball.collidepaddle(self.paddle.rect)
        #Multiplier diminishes if the paddle is touched
        if caught_the_ball:
            self.multiplier=1
         
        



        if self.ball.rect.bottom > self.paddle.rect.top and not caught_the_ball:
            self.running = False
            self.next_screen = "game_over"

            # Outputs final score based on multiplierand time taken to complete in the console
            self.time_end = time.time()
            self.elapsed_time_penalty=(self.time_end-self.time_start)/10
            self.final_score=self.score.score/self.elapsed_time_penalty
            print(f'Final Score: {self.final_score}')
            print(f'Tile Length {len(self.tiles)}')    

            #Writing score to a file
            f = open("score.txt", "a")
            posted_score=str(round(self.final_score,2))
            f.write(posted_score+'\n')
            f.close()
            print(posted_score)



            
        
        
        
        




     
        # insert levels here
        
       


    def draw(self):
        self.window.fill((255, 255, 255))
        self.sprites.draw(self.window)
        self.tiles.draw(self.window)
        self.window.blit(self.score.text,(500,500))

    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.running = False
            self.next_screen = "welcome"

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.ball.speed = 10
                self.ball.angle = 1.5
