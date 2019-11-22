# Python Imports
import asyncio
# Third-Party Imports
# Project Imports
from audio.audio import AudioPlayer
from cards.utils import create_cards_dictionary
from cards.services import get_card_in_position, get_cards_in_field_by_y_coord
from cards.card import Card
from config import (
    CARDS_MESSAGES,
    CARDS_MESSAGES_PLAYER_PLAYED,
    CARDS_MESSAGES_PLAYER_HAND,
    CARDS_MESSAGES_PLAYER_BATTLEFIELD,
    CARDS_MESSAGES_OPPONENT_BATTLEFIELD,
    CARDS_MESSAGES_OPPONENT_PLAYED,
    CARDS_MESSAGES_OPPONENT_HAND
)
from data_structures import services as data_structure_services
from api.services import get_game_state, get_player_names, get_game_result, get_screen_size
from data_structures.states import GameState
from input.managers import InputManager
from text_to_speech.client import TextToSpeechClient
from input.utils import transform_mouse_position_to_bottom_left_coordinate_axis, get_fields_y_coords, Field
from pynput.keyboard import Key
from utils import generate_field_cards_message


class App:

    def __init__(self):
        self.event_loop = asyncio.get_event_loop()
        self.cards_dictionary = create_cards_dictionary("../resources/cards_field.json", "../resources/cards_data.json")
        self.audio_player = AudioPlayer()
        self.input_manager = InputManager(self.event_loop)
        self.text_to_speech_client = TextToSpeechClient()
        self.flag_stop: bool = False
        self.lock = asyncio.locks.Lock()
        self.use_verbose_mode: bool = True
        self.fields_coords: {} = None
        self.match_events: [] = [
            (Key.space, self.handle_mouse_over_card_event),
            (Key.f1, self.generate_field_event(Field.PLAYER_HAND, CARDS_MESSAGES_PLAYER_HAND)),
            (Key.f2, self.generate_field_event(Field.PLAYER_PLAYED, CARDS_MESSAGES_PLAYER_PLAYED)),
            (Key.f3, self.generate_field_event(Field.PLAYER_BATTLEFIELD, CARDS_MESSAGES_PLAYER_BATTLEFIELD)),
            (Key.f6, self.generate_field_event(Field.OPPONENT_HAND, CARDS_MESSAGES_OPPONENT_HAND)),
            (Key.f5, self.generate_field_event(Field.OPPONENT_PLAYED, CARDS_MESSAGES_OPPONENT_PLAYED)),
            (Key.f4, self.generate_field_event(Field.OPPONENT_BATTLEFIELD, CARDS_MESSAGES_OPPONENT_BATTLEFIELD)),
        ]

    def run(self):
        print("Running...")
        self.input_manager.start()
        asyncio.get_event_loop().run_until_complete(asyncio.gather(
            self.loop(),
            self.audio_player.play(),
        ))

    async def initialise_async_values(self):
        if not self.fields_coords:
            _, y_size = await get_screen_size()
            self.fields_coords = get_fields_y_coords(y_size)
        await self.input_manager.key_subscribe(Key.alt_r, self.handle_verbosity_level_switch_event)

    async def loop(self):
        await self.initialise_async_values()
        while not self.flag_stop:
            game_state: GameState = await get_game_state()
            await self.parse_game_state(game_state)
            await asyncio.sleep(1)
        await self._stop()

    async def parse_game_state(self, game_state: GameState):
        print(f"Parsing Game State: {game_state}")
        if data_structure_services.is_game_state_in_progress(game_state):
            await self.game_state_in_progress_loop()

        elif data_structure_services.is_game_state_in_menus(game_state):
            pass

        elif data_structure_services.is_game_state_in_transition(game_state):
            pass

        else:
            # raise AttributeError
            print(f"Unexpected state encountered: {game_state}")

    async def game_state_in_progress_loop(self):
        print("Begin game")
        await self.play_player_names()
        await self.subscribe_match_events()

        while True:
            game_state: GameState = await get_game_state()
            if not data_structure_services.is_game_state_in_progress(game_state):
                break
            await asyncio.sleep(1)

        await self.unsubscribe_match_events()
        await self.play_scores()

    async def play_player_names(self):
        print("Playing player names")
        audio = self.text_to_speech_client.transform_text_to_audio_as_bytes_io(
            await self.get_player_names_as_text()
        )
        await self.audio_player.add_audio_buffer(audio.getbuffer())

    async def get_player_names_as_text(self):
        players = await get_player_names()
        player_1, player_2 = players.values()
        return f"{player_1} vs {player_2}."

    async def play_scores(self):
        print("Playing scores")
        text: str = f"Game result: {await self.get_game_result_as_text()}."
        audio = self.text_to_speech_client.transform_text_to_audio_as_bytes_io(text)
        await self.audio_player.add_audio_buffer(audio.getbuffer())

    async def get_game_result_as_text(self) -> str:
        game_result: dict = await get_game_result()
        return (
            "You won!"
            if game_result.get("LocalPlayerWon") else
            "You lost."
        )

    async def _stop(self):
        print("Closing")
        await self.input_manager.key_unsubscribe(Key.alt_r, self.handle_verbosity_level_switch_event)
        await self.audio_player.stop()
        await self.input_manager.stop()
        audio = self.text_to_speech_client.transform_text_to_audio_as_bytes_io("Exiting application.")
        await self.audio_player.add_audio_buffer(audio.getbuffer())
        print("Exiting...")

    async def subscribe_match_events(self):
        for key, event in self.match_events:
            await self.input_manager.key_subscribe(key, event)

    async def unsubscribe_match_events(self):
        for key, event in self.match_events:
            await self.input_manager.key_unsubscribe(key, event)

    def generate_field_event(self, field, message_formatter: CARDS_MESSAGES):
        async def handle_function(_: Key):
            y_coord: int = self.fields_coords[field]
            cards_generator = await get_cards_in_field_by_y_coord(y_coord, self.cards_dictionary)
            message: str = generate_field_cards_message(message_formatter, list(cards_generator), self.use_verbose_mode)
            async with self.lock:
                audio = self.text_to_speech_client.transform_text_to_audio_as_bytes_io(message)
            await self.audio_player.add_audio_buffer(audio.getbuffer())
        return handle_function

    async def handle_mouse_over_card_event(self, key: Key):
        print(str(key))
        runeterra_mouse_pos = transform_mouse_position_to_bottom_left_coordinate_axis(
            self.input_manager.get_mouse_pos()
        )
        print(runeterra_mouse_pos)
        card: Card = await get_card_in_position(runeterra_mouse_pos, self.cards_dictionary)
        print(card)
        if card is not None:
            async with self.lock:
                audio = self.text_to_speech_client.transform_text_to_audio_as_bytes_io(
                    card.get_as_string(self.use_verbose_mode)
                )
            await self.audio_player.add_audio_buffer(audio.getbuffer())

    async def handle_verbosity_level_switch_event(self, _: Key):
        async with self.lock:
            self.use_verbose_mode = not self.use_verbose_mode


if __name__ == '__main__':
    print("Loading Credentials")
    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../cred.json"
    print("Initialising required data")
    app = App()
    app.run()
