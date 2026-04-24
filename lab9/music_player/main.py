import pygame
import sys
from player import MusicPlayer

pygame.init()
pygame.mixer.init()

WIDTH = 800
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

player = MusicPlayer("lab9/music_player/music")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()

            if event.key == pygame.K_s:
                player.stop()

            if event.key == pygame.K_n:
                player.next_track()

            if event.key == pygame.K_b:
                player.previous_track()

            if event.key == pygame.K_q:
                running = False

    screen.fill((255, 255, 255))

    title_text = font.render("Music Player", True, (0, 0, 0))
    track_text = font.render(f"Current track: {player.get_current_track()}", True, (0, 0, 0))

    if player.is_playing:
        status = "Status: Playing"
    else:
        status = "Status: Stopped"

    status_text = font.render(status, True, (0, 0, 0))
    controls_text = font.render("P - Play | S - Stop | N - Next | B - Previous | Q - Quit", True, (0, 0, 0))

    screen.blit(title_text, (300, 50))
    screen.blit(track_text, (200, 150))
    screen.blit(status_text, (200, 200))
    screen.blit(controls_text, (60, 300))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()