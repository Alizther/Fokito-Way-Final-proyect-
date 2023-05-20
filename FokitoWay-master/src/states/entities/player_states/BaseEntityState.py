"""
Group: DJ-TKD
Project: Fokito Way

Authors: Gerardo Montes, Alberto Calderón
gm5072@gmail.com, alizther13@gmail.com

This file contains the base class BaseEntityState.
"""
from typing import TypeVar

from gale.state import BaseState, StateMachine


class BaseEntityState(BaseState):
    def __init__(
        self, entity: TypeVar("GameEntity"), state_machine: StateMachine
    ) -> None:
        super().__init__(state_machine)
        self.entity = entity
