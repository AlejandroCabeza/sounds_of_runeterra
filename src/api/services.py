# Python Imports
# Third-Party Imports
# Project Imports
from src.api.clients.api_client import ApiClient
from src.api.data_structures.states import GameStates, ExpeditionStates


API_CLIENT: ApiClient = ApiClient()


# STATIC DECKLIST
async def get_active_deck_code() -> str:
    json: dict = await API_CLIENT.fetch_static_decklist()
    return json.get("DeckCode")


async def get_cards_in_deck() -> [{}]:
    json: dict = await API_CLIENT.fetch_static_decklist()
    return json.get("CardsInDeck")


# POSITIONAL RECTANGLES
async def get_player_names() -> dict:
    json: dict = await API_CLIENT.fetch_positional_rectangles()
    return {key: json.get(key) for key in ("PlayerName", "OpponentName")}


async def get_game_state() -> dict:
    json: dict = await API_CLIENT.fetch_positional_rectangles()
    return GameStates.get_state_from_string(json.get("GameState"))


def get_screen_size() -> dict:
    json: dict = await API_CLIENT.fetch_positional_rectangles()
    return json.get("Screen")


def get_rectangles() -> [{}]:
    json: dict = await API_CLIENT.fetch_positional_rectangles()
    return json.get("Rectangles")


# EXPEDITIONS
def get_expedition_is_active() -> bool:
    json: dict = await API_CLIENT.fetch_expeditions_state()
    return json.get("IsActive")


def get_expedition_state() -> ExpeditionStates:
    json: dict = await API_CLIENT.fetch_expeditions_state()
    return ExpeditionStates.get_state_from_string(json.get("State"))


def get_expedition_record() -> [str]:
    json: dict = await API_CLIENT.fetch_expeditions_state()
    return json.get("Record")


def get_expedition_draft_picks() -> []:
    raise NotImplemented


def get_expedition_deck() -> [str]:
    json: dict = await API_CLIENT.fetch_expeditions_state()
    return json.get("Deck")


def get_expedition_games():
    json: dict = await API_CLIENT.fetch_expeditions_state()
    return {key: json.get(key) for key in ("Games", "Wins", "Losses")}


# GAME RESULT
def get_game_result():
    return API_CLIENT.fetch_game_result()
