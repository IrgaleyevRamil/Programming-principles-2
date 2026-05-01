import pygame
import sys
import math

pygame.init()

WIDTH = 1000
HEIGHT = 700
TOOLBAR_HEIGHT = 90

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Extended - Lab 11")

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

font = pygame.font.SysFont("Arial", 16, bold=True)

canvas = pygame.Surface((WIDTH, HEIGHT - TOOLBAR_HEIGHT))
canvas.fill(WHITE)

current_color = BLACK
current_tool = "brush"
brush_size = 5

drawing = False
start_pos = None

colors = [
    (BLACK, pygame.Rect(15, 20, 32, 32)),
    (RED, pygame.Rect(55, 20, 32, 32)),
    (GREEN, pygame.Rect(95, 20, 32, 32)),
    (BLUE, pygame.Rect(135, 20, 32, 32)),
    (YELLOW, pygame.Rect(175, 20, 32, 32)),
    (PURPLE, pygame.Rect(215, 20, 32, 32)),
    (ORANGE, pygame.Rect(255, 20, 32, 32)),
]

tools = {
    "brush": pygame.Rect(310, 15, 75, 35),
    "eraser": pygame.Rect(390, 15, 75, 35),
    "rect": pygame.Rect(470, 15, 75, 35),
    "circle": pygame.Rect(550, 15, 75, 35),
    "square": pygame.Rect(630, 15, 75, 35),
    "r_triangle": pygame.Rect(710, 15, 95, 35),
    "e_triangle": pygame.Rect(810, 15, 95, 35),
    "rhombus": pygame.Rect(910, 15, 80, 35),
    "clear": pygame.Rect(910, 52, 80, 30),
}

tool_names = {
    "brush": "Brush",
    "eraser": "Eraser",
    "rect": "Rect",
    "circle": "Circle",
    "square": "Square",
    "r_triangle": "Right T",
    "e_triangle": "Equal T",
    "rhombus": "Rhombus",
    "clear": "Clear",
}


def draw_toolbar():
    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, TOOLBAR_HEIGHT))
    pygame.draw.line(screen, DARK_GRAY, (0, TOOLBAR_HEIGHT), (WIDTH, TOOLBAR_HEIGHT), 3)

    for color, rect in colors:
        pygame.draw.rect(screen, color, rect, border_radius=5)

        if color == current_color:
            pygame.draw.rect(screen, BLACK, rect, 3, border_radius=5)
        else:
            pygame.draw.rect(screen, DARK_GRAY, rect, 1, border_radius=5)

    for tool_name, rect in tools.items():
        if tool_name == current_tool:
            pygame.draw.rect(screen, DARK_GRAY, rect, border_radius=8)
            text_color = WHITE
        else:
            pygame.draw.rect(screen, WHITE, rect, border_radius=8)
            text_color = BLACK

        pygame.draw.rect(screen, BLACK, rect, 2, border_radius=8)
        text = font.render(tool_names[tool_name], True, text_color)
        screen.blit(text, (rect.centerx - text.get_width() // 2, rect.centery - text.get_height() // 2))

    size_text = font.render(f"Size: {brush_size}   + / - to change", True, BLACK)
    screen.blit(size_text, (15, 60))


def get_shape_points(tool, start, end):
    x1, y1 = start
    x2, y2 = end

    left = min(x1, x2)
    right = max(x1, x2)
    top = min(y1, y2)
    bottom = max(y1, y2)

    w = abs(x2 - x1)
    h = abs(y2 - y1)

    if tool == "square":
        side = min(w, h)

        if x2 < x1:
            left = x1 - side
            right = x1
        else:
            left = x1
            right = x1 + side

        if y2 < y1:
            top = y1 - side
            bottom = y1
        else:
            top = y1
            bottom = y1 + side

        return [(left, top), (right, top), (right, bottom), (left, bottom)]

    if tool == "r_triangle":
        return [(left, bottom), (left, top), (right, bottom)]

    if tool == "e_triangle":
        return [(left, bottom), ((left + right) // 2, top), (right, bottom)]

    if tool == "rhombus":
        cx = (left + right) // 2
        cy = (top + bottom) // 2
        return [(cx, top), (right, cy), (cx, bottom), (left, cy)]

    return []


def draw_final_shape(surface, tool, start, end):
    x1, y1 = start
    x2, y2 = end

    if tool == "rect":
        rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
        pygame.draw.rect(surface, current_color, rect, brush_size)

    elif tool == "circle":
        radius = int(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
        pygame.draw.circle(surface, current_color, (x1, y1), radius, brush_size)

    elif tool in ["square", "r_triangle", "e_triangle", "rhombus"]:
        points = get_shape_points(tool, start, end)
        if len(points) > 1:
            pygame.draw.polygon(surface, current_color, points, brush_size)


def draw_preview(mouse_pos):
    if not drawing or start_pos is None:
        return

    if current_tool not in ["rect", "circle", "square", "r_triangle", "e_triangle", "rhombus"]:
        return

    preview = canvas.copy()
    end_pos = (mouse_pos[0], mouse_pos[1] - TOOLBAR_HEIGHT)
    draw_final_shape(preview, current_tool, start_pos, end_pos)
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
            if event.key in [pygame.K_EQUALS, pygame.K_PLUS]:
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

                draw_final_shape(canvas, current_tool, start_pos, end_pos)

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