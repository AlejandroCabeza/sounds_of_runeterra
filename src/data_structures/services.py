# Python Imports
# Third-Party Imports
# Project Imports
from data_structures.states import GameStates


def is_game_state_in_progress(game_state: GameStates):
    return game_state == GameStates.InProgress


def is_game_state_in_menus(game_state: GameStates):
    return game_state == GameStates.Menus


def is_game_state_in_transition(game_state: GameStates):
    return game_state == GameStates.Transition
