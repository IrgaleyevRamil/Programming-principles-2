import pygame
import random
import sys
import math
import os

pygame.init()
pygame.mixer.init()

WIDTH = 500
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

clock = pygame.time.Clock()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
coin_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "sounds", "eat.wav"))
game_over_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "sounds", "game_over.wav"))

GREEN = (35, 130, 55)
DARK_GREEN = (20, 95, 35)
ROAD = (42, 42, 42)
ROAD_DARK = (32, 32, 32)
WHITE = (240, 240, 240)
YELLOW = (255, 215, 0)
BLACK = (10, 10, 10)
BLUE = (20, 100, 240)
RED = (220, 40, 40)
ORANGE = (240, 130, 30)
PURPLE = (150, 70, 220)
GRAY = (120, 120, 120)
BUTTON = (45, 45, 45)
BUTTON_HOVER = (70, 70, 70)

font = pygame.font.SysFont("Arial", 30, bold=True)
big_font = pygame.font.SysFont("Arial", 52, bold=True)
menu_font = pygame.font.SysFont("Arial", 34, bold=True)

road_left = 80
road_right = 420
road_width = road_right - road_left

player_width = 58
player_height = 98
enemy_width = 58
enemy_height = 98
coin_radius = 15

line_offset = 0
coin_angle = 0
enemy_speed = 6

trees = []


def create_trees():
    result = []

    for i in range(18):
        side = random.choice(["left", "right"])

        if side == "left":
            x = random.randint(10, road_left - 25)
        else:
            x = random.randint(road_right + 25, WIDTH - 20)

        y = random.randint(0, HEIGHT)
        size = random.randint(14, 25)
        result.append([x, y, size])

    return result


def draw_background():
    screen.fill(GREEN)

    for x in range(0, WIDTH, 35):
        pygame.draw.line(screen, DARK_GREEN, (x, 0), (x - 80, HEIGHT), 2)

    for tree in trees:
        x, y, size = tree

        pygame.draw.circle(screen, (80, 55, 25), (x, y + size // 2), size // 3)
        pygame.draw.circle(screen, DARK_GREEN, (x, y), size)
        pygame.draw.circle(screen, (25, 115, 40), (x - size // 2, y + 5), size // 2)
        pygame.draw.circle(screen, (45, 150, 55), (x + size // 2, y + 4), size // 2)

        tree[1] += enemy_speed

        if tree[1] > HEIGHT + 40:
            tree[1] = random.randint(-120, -30)

            if x < road_left:
                tree[0] = random.randint(10, road_left - 25)
            else:
                tree[0] = random.randint(road_right + 25, WIDTH - 20)


def draw_road():
    pygame.draw.rect(screen, ROAD, (road_left, 0, road_width, HEIGHT))
    pygame.draw.rect(screen, ROAD_DARK, (road_left + 18, 0, road_width - 36, HEIGHT))

    for i in range(0, HEIGHT, 40):
        pygame.draw.line(screen, (55, 55, 55), (road_left + 20, i), (road_right - 20, i + 20), 1)

    pygame.draw.rect(screen, (180, 180, 180), (road_left - 8, 0, 8, HEIGHT))
    pygame.draw.rect(screen, (180, 180, 180), (road_right, 0, 8, HEIGHT))

    for y in range(-40, HEIGHT, 60):
        color = RED if (y // 60) % 2 == 0 else WHITE
        pygame.draw.rect(screen, color, (road_left - 22, y + line_offset, 14, 35))
        pygame.draw.rect(screen, color, (road_right + 8, y + line_offset, 14, 35))

    pygame.draw.line(screen, YELLOW, (road_left + 15, 0), (road_left + 15, HEIGHT), 4)
    pygame.draw.line(screen, YELLOW, (road_right - 15, 0), (road_right - 15, HEIGHT), 4)

    lane1 = road_left + road_width // 3
    lane2 = road_left + road_width * 2 // 3

    for y in range(-100, HEIGHT, 100):
        pygame.draw.rect(screen, WHITE, (lane1 - 4, y + line_offset, 8, 55), border_radius=3)
        pygame.draw.rect(screen, WHITE, (lane2 - 4, y + line_offset, 8, 55), border_radius=3)


def draw_car(x, y, color):
    shadow = pygame.Surface((player_width + 12, player_height + 12), pygame.SRCALPHA)
    pygame.draw.ellipse(shadow, (0, 0, 0, 90), (0, 0, player_width + 12, player_height + 12))
    screen.blit(shadow, (x - 3, y + 8))

    pygame.draw.rect(screen, color, (x + 4, y + 12, player_width - 8, player_height - 18), border_radius=16)
    pygame.draw.rect(screen, color, (x, y + 30, player_width, player_height - 45), border_radius=12)

    pygame.draw.rect(screen, (15, 20, 30), (x + 12, y + 22, player_width - 24, 18), border_radius=5)
    pygame.draw.rect(screen, (15, 20, 30), (x + 12, y + 63, player_width - 24, 22), border_radius=5)

    pygame.draw.rect(screen, (230, 230, 230), (x + 24, y + 10, 5, player_height - 18), border_radius=2)
    pygame.draw.rect(screen, (230, 230, 230), (x + 32, y + 10, 5, player_height - 18), border_radius=2)

    pygame.draw.circle(screen, BLACK, (x + 5, y + 34), 7)
    pygame.draw.circle(screen, BLACK, (x + player_width - 5, y + 34), 7)
    pygame.draw.circle(screen, BLACK, (x + 5, y + 75), 7)
    pygame.draw.circle(screen, BLACK, (x + player_width - 5, y + 75), 7)

    pygame.draw.circle(screen, (255, 245, 150), (x + 14, y + 13), 4)
    pygame.draw.circle(screen, (255, 245, 150), (x + player_width - 14, y + 13), 4)

    pygame.draw.circle(screen, (255, 50, 50), (x + 14, y + player_height - 10), 4)
    pygame.draw.circle(screen, (255, 50, 50), (x + player_width - 14, y + player_height - 10), 4)


def draw_coin(x, y, angle):
    glow = pygame.Surface((60, 60), pygame.SRCALPHA)
    pygame.draw.circle(glow, (255, 220, 0, 60), (30, 30), 28)
    screen.blit(glow, (x - 30, y - 30))

    width = int(coin_radius + math.sin(angle) * 5)
    pygame.draw.ellipse(screen, (210, 130, 0), (x - width, y - coin_radius, width * 2, coin_radius * 2))
    pygame.draw.ellipse(screen, YELLOW, (x - width + 3, y - coin_radius + 3, width * 2 - 6, coin_radius * 2 - 6))
    pygame.draw.circle(screen, (255, 245, 150), (x - 4, y - 5), 4)


def draw_score(coins):
    score_box = pygame.Surface((150, 50), pygame.SRCALPHA)
    pygame.draw.rect(score_box, (0, 0, 0, 120), (0, 0, 150, 50), border_radius=12)
    screen.blit(score_box, (WIDTH - 165, 12))

    text = font.render(f"Coins: {coins}", True, WHITE)
    screen.blit(text, (WIDTH - text.get_width() - 25, 22))


def draw_button(rect, text):
    mouse_pos = pygame.mouse.get_pos()
    color = BUTTON_HOVER if rect.collidepoint(mouse_pos) else BUTTON

    pygame.draw.rect(screen, color, rect, border_radius=14)
    pygame.draw.rect(screen, WHITE, rect, 2, border_radius=14)

    label = menu_font.render(text, True, WHITE)
    screen.blit(label, (rect.centerx - label.get_width() // 2, rect.centery - label.get_height() // 2))


def game_over_menu(coins, best_score):
    if coins > best_score:
        best_score = coins

    play_button = pygame.Rect(125, 380, 250, 60)
    quit_button = pygame.Rect(125, 460, 250, 60)

    while True:
        draw_background()
        draw_road()

        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(overlay, (0, 0, 0, 170), (0, 0, WIDTH, HEIGHT))
        screen.blit(overlay, (0, 0))

        title = big_font.render("GAME OVER", True, RED)
        score_text = font.render(f"Coins: {coins}", True, WHITE)
        best_text = font.render(f"Best Score: {best_score}", True, WHITE)

        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 180))
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 260))
        screen.blit(best_text, (WIDTH // 2 - best_text.get_width() // 2, 300))

        draw_button(play_button, "Play Again")
        draw_button(quit_button, "Quit")

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False, best_score

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    return True, best_score

                if quit_button.collidepoint(event.pos):
                    return False, best_score

        clock.tick(60)


def run_game(best_score):
    global line_offset, coin_angle, trees

    player_x = WIDTH // 2 - player_width // 2
    player_y = HEIGHT - player_height - 25
    player_speed = 7

    enemy_x = random.randint(road_left + 25, road_right - enemy_width - 25)
    enemy_y = -enemy_height
    enemy_color = RED

    coin_x = random.randint(road_left + 40, road_right - 40)
    coin_y = random.randint(-500, -50)

    coins = 0
    line_offset = 0
    coin_angle = 0
    trees = create_trees()

    while True:
        line_offset += enemy_speed
        coin_angle += 0.15

        if line_offset >= 100:
            line_offset = 0

        draw_background()
        draw_road()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False, best_score

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player_x > road_left + 25:
            player_x -= player_speed

        if keys[pygame.K_RIGHT] and player_x + player_width < road_right - 25:
            player_x += player_speed

        enemy_y += enemy_speed
        coin_y += enemy_speed

        if enemy_y > HEIGHT:
            enemy_y = -enemy_height
            enemy_x = random.randint(road_left + 25, road_right - enemy_width - 25)
            enemy_color = random.choice([RED, ORANGE, PURPLE, GRAY])

        if coin_y > HEIGHT:
            coin_y = random.randint(-500, -50)
            coin_x = random.randint(road_left + 40, road_right - 40)

        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
        coin_rect = pygame.Rect(coin_x - coin_radius, coin_y - coin_radius, coin_radius * 2, coin_radius * 2)

        if player_rect.colliderect(enemy_rect):
            game_over_sound.play()
            pygame.time.delay(900)
            return game_over_menu(coins, best_score)

        if player_rect.colliderect(coin_rect):
            coin_sound.play()
            coins += 1
            coin_y = random.randint(-500, -50)
            coin_x = random.randint(road_left + 40, road_right - 40)

        draw_coin(coin_x, coin_y, coin_angle)
        draw_car(enemy_x, enemy_y, enemy_color)
        draw_car(player_x, player_y, BLUE)
        draw_score(coins)

        pygame.display.flip()
        clock.tick(60)


best_score = 0
playing = True

while playing:
    playing, best_score = run_game(best_score)

pygame.quit()
sys.exit()