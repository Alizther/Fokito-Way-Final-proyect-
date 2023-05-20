"""
Group: DJ-TKD
Project: Fokito Way

Authors: Gerardo Montes, Alberto Calderón
gm5072@gmail.com, alizther13@gmail.com

This file contains the CollidableMixin.
"""
from typing import Any

import pygame


class CollidableMixin:
    def get_collision_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def collides(self, another: Any) -> bool:
        return self.get_collision_rect().colliderect(another.get_collision_rect())
   
    def collides_others(self, rect: pygame.Rect, anotherother: any) -> bool:
        return rect.colliderect(anotherother.get_collision_rect())
