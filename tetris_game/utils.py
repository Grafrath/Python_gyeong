# 파티클 효과, 텍스트 매니저 등 보조 클래스

import pygame
import random
from constants import WHITE

class Particle:
    def __init__(self, x, y, color):
        self.x, self.y, self.color = x, y, color
        self.vx, self.vy = random.uniform(-5, 5), random.uniform(-5, 5)
        self.gravity, self.life, self.age = 0.2, random.randint(20, 40), 0
        self.size = random.randint(2, 5)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += self.gravity
        self.age += 1

    def draw(self, surf):
        alpha = max(0, 255 - (self.age * 255 // self.life))
        p_surf = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        p_surf.fill((*self.color, alpha))
        surf.blit(p_surf, (int(self.x), int(self.y)))

class TextManager:
    def __init__(self):
        self.fonts = {
            "title": pygame.font.SysFont("arial", 16, bold=True),
            "val": pygame.font.SysFont("consolas", 20, bold=True),
            "large": pygame.font.SysFont("arial", 45, bold=True),
            "bsod_lg": pygame.font.SysFont("malgungothic", 120, bold=True),
            "bsod_md": pygame.font.SysFont("malgungothic", 40, bold=True),
            "bsod_sm": pygame.font.SysFont("malgungothic", 25)
        }
        self.cache = {}
        self.static_labels = {
            "NEXT": self.fonts["title"].render("NEXT", True, WHITE),
            "HOLD": self.fonts["title"].render("HOLD", True, WHITE),
            "SCORE": self.fonts["title"].render("SCORE", True, WHITE),
            "LEVEL": self.fonts["title"].render("LEVEL", True, WHITE),
            "COMBO": self.fonts["title"].render("COMBO", True, WHITE),
            "PAUSED": self.fonts["large"].render("PAUSED", True, WHITE),
            "GAME OVER": self.fonts["large"].render("GAME OVER", True, WHITE)
        }

    def get_val_surf(self, text, color):
        key = f"{text}_{color}"
        if key not in self.cache:
            self.cache[key] = self.fonts["val"].render(str(text), True, color)
        return self.cache[key]