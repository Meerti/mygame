import pygame


sc = pygame.display.set_mode((700, 500))
background = (128, 128, 128)
clock = pygame.time.Clock()
FPS = 60
class rocket():
    def __init__(self, w, h, color, x, y):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
    def draw(self):
        pygame.draw.rect(sc, self.color, self.rect)








game = True
while game:
    sc.fill(background)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    pygame.display.update()
    clock.tick(FPS)

    
