import pygame
pygame.init()
pygame.display.set_caption("graphical for loops")
screen = pygame.display.set_mode((700, 500))


while(1):

    for i in range(10):
        for j in range(7):
            pygame.draw.rect(screen, (200, 0, 100), (i*70, j*70, 20, 20),1)



    pygame.display.flip()

pygame.quit
