import pygame


class MySprite(pygame.sprite.Sprite):
    """Custom Sprite class with added features"""
    # Loading images here
    base_image = pygame.image.load("mario.png")

    
    def __init__(self, limits=None):
        """If limits is provided (rect), then the sprite will always stay within the limits"""
        super().__init__()
        self.limits = limits
        # Have to do lines below to load image 
        self.image = pygame.transform.scale(self.base_image, (250, 250))
        self.rect = self.image.get_rect()

    def check_limits(self):
        """Make the object stay within the defined limits"""
        if not self.limits:
            return

        if self.rect.x < self.limits.left:
            self.rect.x = self.limits.left

        if self.rect.x + self.rect.width > self.limits.right:
            self.rect.x = self.limits.right - self.rect.width

    def move(self, direction):
        """Moves the object left or right"""
        if direction == "right":
            self.rect.x += 10
        elif direction == "left":
            self.rect.x -= 10

        self.check_limits()

    def move_to(self, x, y):
        """Moves the object to a specified location"""
        self.rect.x = x
        self.rect.y = y
        self.check_limits()
