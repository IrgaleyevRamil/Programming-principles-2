import pygame
import random
import sys
import os

pygame.init()
pygame.mixer.init()

WIDTH = 600
HEIGHT = 600
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake - Lab 11")

clock = pygame.time.Clock()

BLACK = (18, 18, 18)
DARK_GRAY = (28, 28, 28)
GRID = (38, 38, 38)
WHITE = (240, 240, 240)
GREEN = (50, 220, 100)
DARK_GREEN = (20, 150, 70)
HEAD_GREEN = (90, 255, 130)
RED = (230, 50, 50)
YELLOW = (255, 215, 0)
PURPLE = (160, 70, 220)
WALL_COLOR = (100, 100, 110)
WALL_LIGHT = (150, 150, 160)
BUTTON = (45, 45, 45)
BUTTON_HOVER = (70, 70, 70)

font = pygame.font.SysFont("Arial", 24, bold=True)
small_font = pygame.font.SysFont("Arial", 18, bold=True)
big_font = pygame.font.SysFont("Arial", 52, bold=True)
menu_font = pygame.font.SysFont("Arial", 34, bold=True)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

eat_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "sounds", "eat.wav"))
game_over_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "sounds", "game_over.wav"))

FOOD_LIFETIME = 5000


def create_walls():
    walls = []

    for x in range(0, WIDTH, CELL):
        walls.append((x, 0))
        walls.append((x, HEIGHT - CELL))

    for y in range(0, HEIGHT, CELL):
        walls.append((0, y))
        walls.append((WIDTH - CELL, y))

    return walls


def generate_food(snake, walls):
    while True:
        x = random.randrange(CELL, WIDTH - CELL, CELL)
        y = random.randrange(CELL, HEIGHT - CELL, CELL)

        if (x, y) not in snake and (x, y) not in walls:
            food_type = random.choice([
                {"value": 1, "color": RED},
                {"value": 2, "color": YELLOW},
                {"value": 3, "color": PURPLE}
            ])

            food_type["pos"] = (x, y)
            food_type["spawn_time"] = pygame.time.get_ticks()

            return food_type


def draw_background():
    screen.fill(BLACK)

    for y in range(0, HEIGHT, CELL):
        for x in range(0, WIDTH, CELL):
            color = DARK_GRAY if (x // CELL + y // CELL) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (x, y, CELL, CELL))

    for x in range(0, WIDTH, CELL):
        pygame.draw.line(screen, GRID, (x, 0), (x, HEIGHT))

    for y in range(0, HEIGHT, CELL):
        pygame.draw.line(screen, GRID, (0, y), (WIDTH, y))


def draw_walls(walls):
    for wall in walls:
        x, y = wall
        pygame.draw.rect(screen, WALL_COLOR, (x, y, CELL, CELL), border_radius=4)
        pygame.draw.rect(screen, WALL_LIGHT, (x + 3, y + 3, CELL - 6, CELL - 6), 1, border_radius=3)


def draw_snake(snake):
    for i, part in enumerate(snake):
        x, y = part

        if i == 0:
            color = HEAD_GREEN
        else:
            color = GREEN if i % 2 == 0 else DARK_GREEN

        pygame.draw.rect(screen, color, (x + 1, y + 1, CELL - 2, CELL - 2), border_radius=7)

        if i == 0:
            pygame.draw.circle(screen, BLACK, (x + 6, y + 7), 3)
            pygame.draw.circle(screen, BLACK, (x + 14, y + 7), 3)


def draw_food(food):
    x, y = food["pos"]
    value = food["value"]
    color = food["color"]

    pygame.draw.circle(screen, color, (x + CELL // 2, y + CELL // 2), CELL // 2 - 2)

    text = small_font.render(str(value), True, BLACK)
    screen.blit(text, (x + CELL // 2 - text.get_width() // 2, y + CELL // 2 - text.get_height() // 2))


def draw_score(score, level, food):
    panel = pygame.Surface((330, 42), pygame.SRCALPHA)
    pygame.draw.rect(panel, (0, 0, 0, 140), (0, 0, 330, 42), border_radius=12)
    screen.blit(panel, (15, 15))

    time_left = max(0, (FOOD_LIFETIME - (pygame.time.get_ticks() - food["spawn_time"])) // 1000)

    text = font.render(f"Score: {score}   Level: {level}   Food: {time_left}s", True, WHITE)
    screen.blit(text, (30, 23))


def draw_button(rect, text):
    mouse_pos = pygame.mouse.get_pos()
    color = BUTTON_HOVER if rect.collidepoint(mouse_pos) else BUTTON

    pygame.draw.rect(screen, color, rect, border_radius=14)
    pygame.draw.rect(screen, WHITE, rect, 2, border_radius=14)

    label = menu_font.render(text, True, WHITE)
    screen.blit(label, (rect.centerx - label.get_width() // 2, rect.centery - label.get_height() // 2))


def game_over_menu(score, level, best_score):
    if score > best_score:
        best_score = score

    play_button = pygame.Rect(175, 330, 250, 60)
    quit_button = pygame.Rect(175, 410, 250, 60)

    while True:
        draw_background()

        title = big_font.render("GAME OVER", True, RED)
        score_text = font.render(f"Your Score: {score}   Level: {level}", True, WHITE)
        best_text = font.render(f"Best Score: {best_score}", True, WHITE)

        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 160))
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 235))
        screen.blit(best_text, (WIDTH // 2 - best_text.get_width() // 2, 270))

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
    snake = [(300, 300), (280, 300), (260, 300)]
    direction = "RIGHT"
    next_direction = "RIGHT"

    score = 0
    level = 1
    speed = 8

    walls = create_walls()
    food = generate_food(snake, walls)

    while True:
        if pygame.time.get_ticks() - food["spawn_time"] > FOOD_LIFETIME:
            food = generate_food(snake, walls)

        draw_background()
        draw_walls(walls)
        draw_food(food)
        draw_snake(snake)
        draw_score(score, level, food)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False, best_score

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    next_direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    next_direction = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    next_direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    next_direction = "RIGHT"

        direction = next_direction

        head_x, head_y = snake[0]

        if direction == "UP":
            head_y -= CELL
        elif direction == "DOWN":
            head_y += CELL
        elif direction == "LEFT":
            head_x -= CELL
        elif direction == "RIGHT":
            head_x += CELL

        new_head = (head_x, head_y)

        if new_head in walls or new_head in snake:
            game_over_sound.play()
            pygame.time.delay(900)
            return game_over_menu(score, level, best_score)

        snake.insert(0, new_head)

        if new_head == food["pos"]:
            eat_sound.play()

            score += food["value"]

            if score % 4 == 0:
                level += 1
                speed += 2

            food = generate_food(snake, walls)
        else:
            snake.pop()

        clock.tick(speed)


best_score = 0
playing = True

while playing:
    playing, best_score = run_game(best_score)

pygame.quit()
sys.exit()