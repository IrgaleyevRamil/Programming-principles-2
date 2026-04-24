import pygame
import sys
from clock import MickeyClock

pygame.init()

WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

background = pygame.image.load("lab9/Mickeys_clock/images/mickeyclock.jpeg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

clock_object = MickeyClock((WIDTH // 2, HEIGHT // 2))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    clock_object.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()