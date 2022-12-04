import pygame




class Score():
    def __init__(self, score=0):
        self.font = pygame.font.SysFont('comicsans', 30)
        self.score = score
        self.text = self.font.render(str(self.score), True, (255, 255, 255))