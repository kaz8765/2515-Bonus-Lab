import pygame
from .tile import Tile


class TileGroup(pygame.sprite.Group):
    def __init__(self, tile_width=100, tile_height=30,level= None):
        # To undo delete bottom 2 lines and remove level parameter above
        # with open("file"+level+".txt"):
        #     self.tiles.add(Tile())

        
        super().__init__()

        for i in range(4):
            for i in range(8):
                counter=0
                spacing=2
                tile=Tile(width=tile_width, height=tile_height)
                tile.move_to(i*100, 50)
                self.add(tile) 
            for i in range(7):
                counter=0
                spacing=2
                tile=Tile(width=tile_width, height=tile_height)
                tile.move_to(i*100+50, 100)
                self.add(tile)

            for i in range(6):
                counter=0
                spacing=2
                tile=Tile(width=tile_width, height=tile_height)
                tile.move_to(i*100+100, 150)
                self.add(tile)
        
        
        # tile = Tile(width=tile_width, height=tile_height)
        # tile2 = Tile(width=tile_width, height=tile_height)

        # tile.move_to(400, 400)
        # tile.move_to(200,200)
        # self.add(tile)
        # self.add(tile2)
