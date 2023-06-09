"""
Group: DJ-TKD
Project: Fokito Way

Authors: Gerardo Montes, Alberto Calderón
gm5072@gmail.com, alizther13@gmail.com

This file contains the class IdleState for player.
"""
from gale.input_handler import InputData
from random import randint

from gale.timer import Timer
import pygame
import random
import time

from src.states.entities.enemy_states.BaseEntityState import BaseEntityState


class IdleState(BaseEntityState):
    def enter(self, direction: str) -> None:
        self.entity.vx = 0
        self.entity.vy = 0
        if direction == "idle":
            self.time_wait = randint(2,4)
        else:
            self.time_wait = randint(0,6)

        #Set a clock and select a time in case of ocurr a collision
        #Set a random time to change de move
        #And take Time 0 for then calculate _dt
        self.reloj = pygame.time.Clock()
        self.reloj.tick(60)
        self.t0 = pygame.time.get_ticks() /1000

        self.entity.change_animation("idle")


    def update(self, dt: float) -> None:
        #rint("ENTER IDLE")
        self.t1 = pygame.time.get_ticks() / 1000
        dt = self.t1 - self.t0

        if dt >= self.time_wait:
            self.t0 = self.t1
            temp = random.choice(["left", "right", "up", "down"])
            self.entity.change_state("walk", temp)
        else:
            pass

    def on_input(self, input_id: str, input_data: InputData) -> None:
        pass