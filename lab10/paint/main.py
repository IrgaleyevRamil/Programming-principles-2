import pygame
import sys

pygame.init()

WIDTH = 900
HEIGHT = 650
TOOLBAR_HEIGHT = 80

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (210, 210, 210)
DARK_GRAY = (80, 80, 80)
RED = (230, 40, 40)
GREEN = (40, 180, 80)
BLUE = (40, 100, 230)
YELLOW = (240, 210, 40)
PURPLE = (150, 70, 220)
ORANGE = (240, 130, 30)

font = pygame.font.SysFont("Arial", 20, bold=True)

canvas = pygame.Surface((WIDTH, HEIGHT - TOOLBAR_HEIGHT))
canvas.fill(WHITE)

current_color = BLACK
current_tool = "brush"
brush_size = 6

drawing = False
start_pos = None

colors = [
    (BLACK, pygame.Rect(20, 20, 35, 35)),
    (RED, pygame.Rect(65, 20, 35, 35)),
    (GREEN, pygame.Rect(110, 20, 35, 35)),
    (BLUE, pygame.Rect(155, 20, 35, 35)),
    (YELLOW, pygame.Rect(200, 20, 35, 35)),
    (PURPLE, pygame.Rect(245, 20, 35, 35)),
    (ORANGE, pygame.Rect(290, 20, 35, 35)),
]

tools = {
    "brush": pygame.Rect(370, 18, 90, 40),
    "rect": pygame.Rect(470, 18, 90, 40),
    "circle": pygame.Rect(570, 18, 90, 40),
    "eraser": pygame.Rect(670, 18, 90, 40),
    "clear": pygame.Rect(770, 18, 90, 40),
}


def draw_toolbar():
    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, TOOLBAR_HEIGHT))
    pygame.draw.line(screen, DARK_GRAY, (0, TOOLBAR_HEIGHT), (WIDTH, TOOLBAR_HEIGHT), 3)

    for color, rect in colors:
        pygame.draw.rect(screen, color, rect, border_radius=6)

        if color == current_color:
            pygame.draw.rect(screen, BLACK, rect, 3, border_radius=6)
        else:
            pygame.draw.rect(screen, DARK_GRAY, rect, 1, border_radius=6)

    for tool_name, rect in tools.items():
        if tool_name == current_tool:
            pygame.draw.rect(screen, DARK_GRAY, rect, border_radius=10)
            text_color = WHITE
        else:
            pygame.draw.rect(screen, WHITE, rect, border_radius=10)
            text_color = BLACK

        pygame.draw.rect(screen, BLACK, rect, 2, border_radius=10)

        text = font.render(tool_name.capitalize(), True, text_color)
        screen.blit(text, (rect.centerx - text.get_width() // 2, rect.centery - text.get_height() // 2))

    size_text = font.render(f"Size: {brush_size}", True, BLACK)
    screen.blit(size_text, (20, 58))


def draw_preview(mouse_pos):
    if not drawing or start_pos is None:
        return

    if current_tool not in ["rect", "circle"]:
        return

    preview = canvas.copy()
    x1, y1 = start_pos
    x2, y2 = mouse_pos[0], mouse_pos[1] - TOOLBAR_HEIGHT

    if current_tool == "rect":
        rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
        pygame.draw.rect(preview, current_color, rect, brush_size)

    elif current_tool == "circle":
        radius = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
        pygame.draw.circle(preview, current_color, (x1, y1), radius, brush_size)

    screen.blit(preview, (0, TOOLBAR_HEIGHT))


running = True

while running:
    screen.fill(WHITE)
    screen.blit(canvas, (0, TOOLBAR_HEIGHT))
    draw_toolbar()

    mouse_pos = pygame.mouse.get_pos()
    draw_preview(mouse_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS or event.key == pygame.K_PLUS:
                brush_size += 1

            if event.key == pygame.K_MINUS and brush_size > 1:
                brush_size -= 1

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if mouse_pos[1] < TOOLBAR_HEIGHT:
                    for color, rect in colors:
                        if rect.collidepoint(mouse_pos):
                            current_color = color
                            current_tool = "brush"

                    for tool_name, rect in tools.items():
                        if rect.collidepoint(mouse_pos):
                            if tool_name == "clear":
                                canvas.fill(WHITE)
                            else:
                                current_tool = tool_name
                else:
                    drawing = True
                    start_pos = (mouse_pos[0], mouse_pos[1] - TOOLBAR_HEIGHT)

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                end_pos = (mouse_pos[0], mouse_pos[1] - TOOLBAR_HEIGHT)

                if current_tool == "rect":
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
                    pygame.draw.rect(canvas, current_color, rect, brush_size)

                elif current_tool == "circle":
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    radius = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
                    pygame.draw.circle(canvas, current_color, (x1, y1), radius, brush_size)

                drawing = False
                start_pos = None

        if event.type == pygame.MOUSEMOTION:
            if drawing and mouse_pos[1] >= TOOLBAR_HEIGHT:
                x = mouse_pos[0]
                y = mouse_pos[1] - TOOLBAR_HEIGHT

                if current_tool == "brush":
                    pygame.draw.circle(canvas, current_color, (x, y), brush_size)

                elif current_tool == "eraser":
                    pygame.draw.circle(canvas, WHITE, (x, y), brush_size + 8)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()