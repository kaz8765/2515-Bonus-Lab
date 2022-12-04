import random
import pygame
from ..components.sprite import MySprite
from screens import BaseScreen
#import score here 
from ..components import Paddle, Ball, TileGroup
from components import TextBox, text


class GameScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #Call score object here from justin's screen
        # Create background and set mario location 
        self.background=MySprite()
        self.background.rect.x=300
        self.background.rect.y=300

        self.new_window = pygame.display.set_mode((800, 800))
        surf = pygame.Surface((100, 100))
        surf.fill((0, 0, 0))
        self.new_window.blit(surf, (50, 50))

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

        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.paddle.move("left")

        if keys[pygame.K_RIGHT]:
            self.paddle.move("right")
        
        self.sprites.update()
        collided = self.ball.collidetiles(self.tiles)
        print(collided) #can calculate score 
        
        

        # window = pygame.display.set_mode((700, 700))
        # window.fill((100, 255, 255))

        # self.score=0
        # self.score_font=pygame.font.SysFont("comicsans", 50)
        # self.text=self.score_font.render(str(self.score), True,(255,255,255))


       


        caught_the_ball = self.ball.collidepaddle(self.paddle.rect)

        if self.ball.rect.bottom > self.paddle.rect.top and not caught_the_ball:
            self.running = False
            self.next_screen = "game_over"
        # insert levels here
        print(len(self.tiles))
        #pygame render text in draw method 

        


    def draw(self):
        self.window.fill((255, 255, 255))
        self.sprites.draw(self.window)
        self.tiles.draw(self.window)


    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.running = False
            self.next_screen = "welcome"

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.ball.speed = 10
                self.ball.angle = 1.5
