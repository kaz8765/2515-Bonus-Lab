import pygame
from .tile import Tile


class TileGroup(pygame.sprite.Group,):
    def __init__(self, tile_width=100, tile_height=30,level= None):

        
        
        super().__init__()

        if level==None:

        # Creating multiple levels here by using looping and also using files

            for i in range(4):
                for i in range(8):
                    
                    tile=Tile(width=tile_width, height=tile_height)
                    tile.move_to(i*100, 50)
                    self.add(tile) 
                for i in range(7):
                    
                    tile=Tile(width=tile_width, height=tile_height)
                    tile.move_to(i*100+50, 100)
                    self.add(tile)

                for i in range(6):
                    
                    tile=Tile(width=tile_width, height=tile_height)
                    tile.move_to(i*100+100, 150)
                    self.add(tile)
        # Using Files
        if level !=None:
            self.stage="file"
            self.stage+=str(level)
            self.stage+=".txt"
            
            with open(self.stage, "r") as f:
                lines = f.readlines()
                height=0
            for i in range(len(lines)):
                height+=0.5

                line=lines[i].strip('\n')
                counter=1
                for char in range(len(line)):
                    if line[char]=='x':
                        tile=Tile(width=tile_width, height=tile_height)
                        tile.move_to(counter*100, 50*height)
                        self.add(tile) 
                        counter+=1
                        print('tile')
                    if line[char]==' ':
                        counter+=0.5
