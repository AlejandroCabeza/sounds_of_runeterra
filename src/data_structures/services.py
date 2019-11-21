# Python Imports
# Third-Party Imports
# Project Imports
from data_structures.states import GameState


def is_game_state_in_progress(game_state: GameState):
    return game_state == GameState.InProgress


def is_game_state_in_menus(game_state: GameState):
    return game_state == GameState.Menus


def is_game_state_in_transition(game_state: GameState):
    return game_state == GameState.Transition
