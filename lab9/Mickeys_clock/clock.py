import pygame
import math
import time

class MickeyClock:
    def __init__(self, center):
        self.center = center

    def draw_hand(self, screen, angle, length, color, width):
        rad = math.radians(angle - 90)
        end_x = self.center[0] + length * math.cos(rad)
        end_y = self.center[1] + length * math.sin(rad)
        pygame.draw.line(screen, color, self.center, (end_x, end_y), width)

    def draw(self, screen):
        current_time = time.localtime()
        seconds = current_time.tm_sec
        minutes = current_time.tm_min

        second_angle = seconds * 6
        minute_angle = minutes * 6 + seconds * 0.1

        self.draw_hand(screen, minute_angle, 90, (0, 0, 0), 6)
        self.draw_hand(screen, second_angle, 110, (255, 0, 0), 4)